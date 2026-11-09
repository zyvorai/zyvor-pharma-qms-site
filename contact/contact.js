(function () {
  var form = document.getElementById("contact");
  if (!form) return;
  try {
    var q = new URLSearchParams(location.search);
    ["region", "topic"].forEach(function (k) {
      var v = q.get(k), el = form.elements[k];
      if (v && el) for (var i = 0; i < el.options.length; i++) if (el.options[i].value === v) el.selectedIndex = i;
    });
  } catch (e) {}
  function label(el) { return el.options && el.selectedIndex > 0 ? el.options[el.selectedIndex].text : (el.value || "").trim(); }
  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    var f = form.elements;
    var lines = [
      "Name: " + f.name.value.trim(), "Role: " + label(f.role), "Organisation: " + f.org.value.trim(),
      "Market: " + label(f.region), "Size: " + label(f.size), "Interest: " + label(f.topic), "Timing: " + label(f.when), "",
      f.msg.value.trim(), "", "(Sent from the Zyvor Pharma QMS website. No batch or patient data.)"
    ];
    var topic = label(f.topic) || "Pharma QMS";
    location.href = "mailto:sales@zyvor.dev?subject=" + encodeURIComponent("Pharma QMS: " + topic) + "&body=" + encodeURIComponent(lines.join("\n"));
  });
})();
