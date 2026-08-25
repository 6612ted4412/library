/* ---------------------------------------------------------------
   dc-runtime — 讓 design-canvas 樣板可以離線預覽的極簡執行環境
   支援：{{ 綁定 }}、<sc-if>、<sc-for>、onClick / onChange、style-hover
   --------------------------------------------------------------- */
(function (global) {
  "use strict";

  var comp = null, root = null, tpl = null;
  var hoverStyleEl = null, hoverMap = Object.create(null), hoverSeq = 0;
  var scheduled = false;

  function DCLogic() {}
  DCLogic.prototype.setState = function (patch) {
    var next = typeof patch === "function" ? patch(this.state) : patch;
    this.state = Object.assign({}, this.state, next);
    schedule();
  };
  global.DCLogic = DCLogic;

  /* ---------- 運算式：只支援 a、a.b.c、true、false、數字 ---------- */
  function evalExpr(raw, scope) {
    var expr = String(raw).trim();
    if (expr === "true") return true;
    if (expr === "false") return false;
    if (/^-?\d+(\.\d+)?$/.test(expr)) return Number(expr);
    var parts = expr.split(".");
    var v = scope[parts[0]];
    for (var i = 1; i < parts.length && v != null; i++) v = v[parts[i]];
    return v;
  }

  var BINDING = /\{\{([^}]*)\}\}/g;
  var PURE = /^\s*\{\{([^}]*)\}\}\s*$/;

  function interpolate(str, scope) {
    return String(str).replace(BINDING, function (_, e) {
      var v = evalExpr(e, scope);
      return v == null || v === false ? "" : String(v);
    });
  }
  function pureValue(str, scope) {
    var m = PURE.exec(str);
    return m ? evalExpr(m[1], scope) : undefined;
  }

  /* ---------- style-hover → 產生 :hover class ---------- */
  function hoverClass(cssText) {
    if (hoverMap[cssText]) return hoverMap[cssText];
    var cls = "dc-h" + ++hoverSeq;
    var decls = cssText
      .split(";")
      .map(function (d) { return d.trim(); })
      .filter(Boolean)
      .map(function (d) { return d.replace(/\s*!important\s*$/i, "") + " !important"; })
      .join(";");
    try {
      hoverStyleEl.sheet.insertRule("." + cls + ":hover{" + decls + "}", hoverStyleEl.sheet.cssRules.length);
    } catch (e) { /* 無效宣告就略過 */ }
    hoverMap[cssText] = cls;
    return cls;
  }

  /* ---------- 樣板 → DOM ---------- */
  function renderChildren(tplNode, scope, out, ctx) {
    var kids = tplNode.childNodes;
    for (var i = 0; i < kids.length; i++) renderNode(kids[i], scope, out, ctx);
  }

  function renderNode(node, scope, out, ctx) {
    /* 文字 */
    if (node.nodeType === 3) {
      var txt = node.nodeValue;
      out.appendChild(document.createTextNode(BINDING.test(txt) ? interpolate(txt, scope) : txt));
      BINDING.lastIndex = 0;
      return;
    }
    if (node.nodeType !== 1) return;

    var tag = node.tagName.toLowerCase();

    /* 條件 */
    if (tag === "sc-if") {
      var cond = pureValue(node.getAttribute("value") || "", scope);
      if (cond) renderChildren(node, scope, out, ctx);
      return;
    }

    /* 迴圈 */
    if (tag === "sc-for") {
      var list = pureValue(node.getAttribute("list") || "", scope) || [];
      var alias = node.getAttribute("as") || "item";
      for (var i = 0; i < list.length; i++) {
        var childScope = Object.create(scope);
        childScope[alias] = list[i];
        childScope[alias + "Index"] = i;
        renderChildren(node, childScope, out, ctx);
      }
      return;
    }

    /* 一般元素 */
    var el = document.createElement(tag);
    var attrs = node.attributes;
    var needsCursor = false;
    for (var a = 0; a < attrs.length; a++) {
      var name = attrs[a].name.toLowerCase();
      var val = attrs[a].value;

      if (name.indexOf("hint-") === 0) continue;

      if (name === "onclick") {
        var fn = pureValue(val, scope);
        if (typeof fn === "function") {
          el.addEventListener("click", fn);
          /* 讓 role="button" 的元素也能用鍵盤操作 */
          el.addEventListener("keydown", function (handler) {
            return function (e) {
              if (e.key === "Enter" || e.key === " " || e.key === "Spacebar") {
                e.preventDefault();
                handler(e);
              }
            };
          }(fn));
          if (!/cursor\s*:/.test(node.getAttribute("style") || "")) needsCursor = true;
        }
        continue;
      }
      if (name === "onchange") {
        var handler = pureValue(val, scope);
        if (typeof handler === "function") el.addEventListener("input", handler);
        continue;
      }
      if (name === "style-hover") {
        el.classList.add(hoverClass(interpolate(val, scope)));
        continue;
      }
      if (name === "value" && (tag === "input" || tag === "textarea" || tag === "select")) {
        var v = interpolate(val, scope);
        el.value = v;
        el.setAttribute("data-dc-key", val + "#" + (ctx.keys[val] = (ctx.keys[val] || 0) + 1));
        continue;
      }
      el.setAttribute(name, interpolate(val, scope));
    }

    if (needsCursor) el.style.cursor = "pointer";
    renderChildren(node, scope, el, ctx);
    out.appendChild(el);
  }

  /* ---------- render / 焦點與捲動保留 ---------- */
  function render() {
    var vals = comp.renderVals();

    var act = document.activeElement;
    var focusKey = act && act.getAttribute ? act.getAttribute("data-dc-key") : null;
    var selStart = focusKey ? act.selectionStart : null;
    var selEnd = focusKey ? act.selectionEnd : null;
    var scrollY = window.scrollY;

    var frag = document.createDocumentFragment();
    renderChildren(tpl, vals, frag, { keys: Object.create(null) });
    root.replaceChildren(frag);

    if (focusKey) {
      var back = root.querySelector('[data-dc-key="' + focusKey.replace(/"/g, '\\"') + '"]');
      if (back) {
        back.focus({ preventScroll: true });
        try { back.setSelectionRange(selStart, selEnd); } catch (e) {}
      }
    }
    window.scrollTo(0, scrollY);
  }

  function schedule() {
    if (scheduled) return;
    scheduled = true;
    requestAnimationFrame(function () { scheduled = false; render(); });
  }

  global.DC = {
    mount: function (instance, rootEl, templateEl) {
      comp = instance;
      root = rootEl;
      tpl = templateEl.content || templateEl;
      hoverStyleEl = document.createElement("style");
      document.head.appendChild(hoverStyleEl);
      render();
    },
    rerender: schedule
  };
})(window);
