from django.core.validators import FileExtensionValidator
from django.db import models
from django.templatetags.static import static
from django.urls import reverse
from django.utils.text import slugify

from .validators import validate_cv_size


class Project(models.Model):
    """A portfolio project rendered on the landing page.

    ``image`` holds images uploaded through the admin. ``static_image`` is a
    fallback path (relative to the ``static/`` directory) used for the projects
    that shipped with the original static site, so the page renders identically
    before any uploads exist.
    """

    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    description = models.TextField(
        help_text="Brief summary shown on the home page card."
    )
    content = models.TextField(
        blank=True,
        help_text=(
            "Full project details shown on the project page. Supports rich "
            "text: headings, bold, links, lists, images and code."
        ),
    )
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

    def get_absolute_url(self):
        return reverse("portfolio:project_detail", args=[self.slug])

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


class SiteProfile(models.Model):
    """Singleton row holding the editable homepage (hero) content.

    Always stored with ``pk=1`` so there is exactly one profile. Managed from
    the admin as a single "Site Content" entry.
    """

    greeting = models.CharField(
        max_length=150,
        default="Hi, my name is Princewill",
        help_text="Small line above the headline.",
    )
    headline = models.CharField(
        max_length=200,
        default="I build solutions for the web.",
        help_text="Main tagline shown as the page heading.",
    )
    description = models.TextField(
        help_text="Intro paragraph. Supports bold, links and lists.",
    )
    contact_heading = models.CharField(
        max_length=100, default="Get in touch"
    )
    email = models.EmailField(blank=True)
    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True,
        help_text="Upload a photo. Falls back to the static image below.",
    )
    static_image = models.CharField(
        max_length=255,
        blank=True,
        help_text="Fallback path under static/ (e.g. images/user_icon.jpg).",
    )
    github_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    footer_text = models.CharField(
        max_length=120, blank=True, default="princewilldev.com"
    )
    resume_file = models.FileField(
        upload_to="resume/",
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(["pdf", "doc", "docx"]),
            validate_cv_size,
        ],
        help_text="PDF, DOC or DOCX (max 10 MB). Upload a new file to replace.",
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Content"
        verbose_name_plural = "Site Content"

    def __str__(self):
        return "Site Content"

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    def save(self, *args, **kwargs):
        self.pk = 1
        previous = SiteProfile.objects.filter(pk=1).first()
        previous_image = previous.profile_image if previous else None
        previous_resume = previous.resume_file if previous else None

        super().save(*args, **kwargs)

        if (
            previous_image
            and previous_image.name
            and previous_image.name != self.profile_image.name
        ):
            previous_image.delete(save=False)
        if (
            previous_resume
            and previous_resume.name
            and previous_resume.name != self.resume_file.name
        ):
            previous_resume.delete(save=False)

    @property
    def display_image(self):
        if self.profile_image:
            return self.profile_image.url
        if self.static_image:
            return static(self.static_image)
        return ""
