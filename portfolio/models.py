from django.db import models
from django.templatetags.static import static
from django.utils.text import slugify


class Project(models.Model):
    """A portfolio project rendered on the landing page.

    ``image`` holds images uploaded through the admin. ``static_image`` is a
    fallback path (relative to the ``static/`` directory) used for the projects
    that shipped with the original static site, so the page renders identically
    before any uploads exist.
    """

    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    description = models.TextField(help_text="Short summary shown on the card.")
    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True,
        help_text="Upload a thumbnail. Falls back to the static image below.",
    )
    static_image = models.CharField(
        max_length=255,
        blank=True,
        help_text="Fallback path under static/ (e.g. images/bix-home.png).",
    )
    link = models.URLField(help_text="External URL opened by 'view project'.")
    order = models.PositiveIntegerField(
        default=0, help_text="Lower numbers appear first."
    )
    is_published = models.BooleanField(
        default=True, help_text="Uncheck to hide from the site."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:140] or "project"
            slug = base
            counter = 2
            while (
                Project.objects.filter(slug=slug).exclude(pk=self.pk).exists()
            ):
                slug = f"{base}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    @property
    def display_image(self):
        if self.image:
            return self.image.url
        if self.static_image:
            return static(self.static_image)
        return ""


class Skill(models.Model):
    """An icon in the 'Primary Skills on' strip."""

    name = models.CharField(max_length=80)
    icon = models.ImageField(
        upload_to="skills/",
        blank=True,
        null=True,
        help_text="Upload an icon. Falls back to the static icon below.",
    )
    static_icon = models.CharField(
        max_length=255,
        blank=True,
        help_text="Fallback path under static/ (e.g. assets/images/icons/php.png).",
    )
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers first.")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name

    @property
    def display_icon(self):
        if self.icon:
            return self.icon.url
        if self.static_icon:
            return static(self.static_icon)
        return ""
