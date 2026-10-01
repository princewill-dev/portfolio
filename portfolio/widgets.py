from django import forms


class RichTextWidget(forms.Textarea):
    """A textarea enhanced with the TinyMCE editor loaded from a CDN.

    No Python dependency is required, so this keeps working regardless of the
    Django/Python version. The companion ``tinymce-init.js`` wires the editor
    to any element carrying the ``tinymce-editor`` class.
    """

    def __init__(self, attrs=None):
        default_attrs = {"class": "tinymce-editor", "rows": 10}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

    class Media:
        js = (
            "https://cdn.jsdelivr.net/npm/tinymce@7/tinymce.min.js",
            "assets/js/admin/tinymce-init.js",
        )
