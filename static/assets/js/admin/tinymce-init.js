(function () {
    "use strict";

    function init() {
        if (typeof tinymce === "undefined") {
            return;
        }
        tinymce.init({
            selector: "textarea.tinymce-editor",
            license_key: "gpl",
            height: 340,
            menubar: false,
            branding: false,
            promotion: false,
            plugins: "lists link code",
            toolbar:
                "undo redo | bold italic underline | bullist numlist | link | removeformat | code",
            content_style:
                "body{font-family:Inter,Arial,sans-serif;font-size:14px;line-height:1.6;}",
        });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", init);
    } else {
        init();
    }
})();
