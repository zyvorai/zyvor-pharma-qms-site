(function () {
  var group = document.querySelector(".oseg");
  if (!group) return;
  var panels = [].slice.call(document.querySelectorAll(".os-panel"));
  var guess = "mac";
  var ua = navigator.userAgent || "";
  if (/Windows/i.test(ua)) guess = "windows";
  else if (/Linux/i.test(ua)) guess = "linux";
  function show(os) {
    [].forEach.call(group.querySelectorAll('[role="radio"]'), function (b) {
      var on = b.getAttribute("data-value") === os;
      b.setAttribute("aria-checked", on ? "true" : "false");
    });
    panels.forEach(function (p) {
      var on = p.getAttribute("data-os") === os;
      if (on) p.removeAttribute("hidden"); else p.setAttribute("hidden", "");
    });
  }
  show(guess);
  [].forEach.call(group.querySelectorAll('[role="radio"]'), function (b) {
    b.addEventListener("click", function () { show(b.getAttribute("data-value")); });
  });
  [].forEach.call(document.querySelectorAll(".copy"), function (btn) {
    btn.addEventListener("click", function () {
      var id = btn.getAttribute("data-copy");
      var el = document.getElementById(id);
      if (!el) return;
      var text = el.textContent;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () { btn.textContent = "Copied"; setTimeout(function () { btn.textContent = "Copy"; }, 1200); });
      }
    });
  });
})();
