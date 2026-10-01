from django.contrib import admin
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.html import format_html

from .models import Project, SiteProfile, Skill
from .widgets import RichTextWidget

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


@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {"widget": RichTextWidget}}

    fieldsets = (
        (
            "Hero text",
            {
                "fields": ("greeting", "headline", "description"),
            },
        ),
        (
            "Contact",
            {
                "fields": ("contact_heading", "email"),
            },
        ),
        (
            "Profile photo",
            {
                "fields": ("profile_image", "static_image", "image_preview"),
                "description": (
                    "Upload a photo, or leave empty to use the static fallback "
                    "path (relative to the static/ folder)."
                ),
            },
        ),
        (
            "Social & footer",
            {
                "fields": (
                    "github_url",
                    "twitter_url",
                    "linkedin_url",
                    "footer_text",
                ),
            },
        ),
        (
            "CV / Resume",
            {
                "fields": ("resume_file", "current_resume"),
                "description": (
                    "Upload a PDF, DOC or DOCX file (max 10 MB). Uploading a "
                    "new file replaces the current one. The button is hidden "
                    "on the site until a file is present."
                ),
            },
        ),
        ("Last updated", {"fields": ("updated_at",)}),
    )
    readonly_fields = ("image_preview", "current_resume", "updated_at")

    def has_add_permission(self, request):
        # Singleton: only allow adding when no row exists yet.
        return not SiteProfile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        # Skip the one-row list; go straight to the editor.
        obj = SiteProfile.get_solo()
        return redirect(
            reverse("admin:portfolio_siteprofile_change", args=[obj.pk])
        )

    @admin.display(description="Current photo")
    def image_preview(self, obj):
        url = obj.display_image
        if not url:
            return "No photo set."
        return format_html(
            '<img src="{}" style="max-height:160px;border-radius:6px;" />',
            url,
        )

    @admin.display(description="Current CV")
    def current_resume(self, obj):
        if not obj.resume_file:
            return "No CV uploaded yet — the button is hidden on the site."
        return format_html(
            '<a href="{}" target="_blank">Download current CV ({})</a>',
            obj.resume_file.url,
            obj.resume_file.name.rsplit("/", 1)[-1],
        )
