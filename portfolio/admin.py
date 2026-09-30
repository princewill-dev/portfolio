from django.contrib import admin
from django.utils.html import format_html

from .models import Project, Skill

admin.site.site_header = "Princewill Portfolio Admin"
admin.site.site_title = "Princewill Portfolio"
admin.site.index_title = "Manage your portfolio"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "thumbnail",
        "title",
        "order",
        "is_published",
        "created_at",
    )
    list_display_links = ("title",)
    list_editable = ("order", "is_published")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "description", "link")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("preview", "created_at", "updated_at")
    ordering = ("order", "-created_at")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "slug",
                    "description",
                    "link",
                )
            },
        ),
        (
            "Thumbnail",
            {
                "fields": ("image", "static_image", "preview"),
                "description": (
                    "Upload an image, or leave empty to use the static "
                    "fallback path (relative to the static/ folder)."
                ),
            },
        ),
        (
            "Visibility",
            {"fields": ("order", "is_published", "created_at", "updated_at")},
        ),
    )

    @admin.display(description="Preview")
    def thumbnail(self, obj):
        url = obj.display_image
        if not url:
            return "—"
        return format_html(
            '<img src="{}" style="height:44px;width:66px;object-fit:cover;'
            'border-radius:4px;" />',
            url,
        )

    @admin.display(description="Current image")
    def preview(self, obj):
        url = obj.display_image
        if not url:
            return "No image set."
        return format_html(
            '<img src="{}" style="max-height:160px;border-radius:6px;" />',
            url,
        )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("icon_thumbnail", "name", "order", "is_active")
    list_display_links = ("name",)
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)
    ordering = ("order", "id")

    @admin.display(description="Icon")
    def icon_thumbnail(self, obj):
        url = obj.display_icon
        if not url:
            return "—"
        return format_html(
            '<img src="{}" style="height:30px;width:30px;object-fit:contain;" />',
            url,
        )
