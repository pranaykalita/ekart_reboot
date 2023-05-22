!function (e) {
    "use strict";

    function i() {}

    i.prototype.init = function () {
        new SimpleMDE({element: document.getElementsByClassName("simplemde"), spellChecker: !1, autosave: {enabled: !0, unique_id: "simplemd"}})
    },
        e.SimpleMDEEditor = new i, e.SimpleMDEEditor.Constructor = i
}(window.jQuery), function () {
    "use strict";
    window.jQuery.SimpleMDEEditor.init()
}();