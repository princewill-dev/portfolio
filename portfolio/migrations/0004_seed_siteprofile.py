from django.db import migrations

DEFAULTS = {
    "greeting": "Hi, my name is Princewill",
    "headline": "I build solutions for the web.",
    "description": (
        "I'm a software developer based in Lagos, Nigeria. I craft API, "
        "websites and digital services that prioritizes the user's experience "
        "by removing ununnecessary bottlenecks and frictions."
    ),
    "contact_heading": "Get in touch",
    "email": "dev.princewill@gmail.com",
    "static_image": "images/user_icon.jpg",
    "github_url": "https://github.com/princewill-dev",
    "twitter_url": "https://twitter.com/princewill_dev",
    "linkedin_url": "https://www.linkedin.com/in/princewilldev",
    "footer_text": "princewilldev.com",
}


def seed(apps, schema_editor):
    SiteProfile = apps.get_model("portfolio", "SiteProfile")
    SiteProfile.objects.update_or_create(pk=1, defaults=DEFAULTS)


def unseed(apps, schema_editor):
    SiteProfile = apps.get_model("portfolio", "SiteProfile")
    SiteProfile.objects.filter(pk=1).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0003_siteprofile"),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
