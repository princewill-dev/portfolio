from django.core.management.base import BaseCommand
from django.db import transaction

from portfolio.models import Project, Skill
from portfolio.seed_data import PROJECTS, SKILLS


class Command(BaseCommand):
    help = (
        "Seed the original portfolio projects and skills into the database. "
        "Idempotent: re-running updates existing rows instead of duplicating."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Delete all existing Projects and Skills before seeding.",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        if options["flush"]:
            deleted_p, _ = Project.objects.all().delete()
            deleted_s, _ = Skill.objects.all().delete()
            self.stdout.write(
                self.style.WARNING(
                    f"Flushed {deleted_p} project row(s) and {deleted_s} skill row(s)."
                )
            )

        created_p = updated_p = 0
        for data in PROJECTS:
            _, created = Project.objects.update_or_create(
                slug=data["slug"], defaults=data
            )
            created_p += created
            updated_p += not created

        created_s = updated_s = 0
        for data in SKILLS:
            _, created = Skill.objects.update_or_create(
                name=data["name"],
                defaults={
                    "static_icon": data["static_icon"],
                    "order": data["order"],
                    "is_active": True,
                },
            )
            created_s += created
            updated_s += not created

        self.stdout.write(
            self.style.SUCCESS(
                f"Projects: {created_p} created, {updated_p} updated. "
                f"Skills: {created_s} created, {updated_s} updated."
            )
        )
