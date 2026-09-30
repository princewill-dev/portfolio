"""Seed data for the original portfolio projects and skills.

Kept in one place so both the initial data migration and the
``seed_projects`` management command can use it.
"""

PROJECTS = [
    {
        "title": "API Terminal (simulation)",
        "slug": "api-terminal-simulation",
        "description": (
            "A sample API terminal web app that queries API endpoints with "
            "specific commands and displays the results in the terminal interface"
        ),
        "static_image": "images/terminal.png",
        "link": "https://princewilldev.com/terminal",
        "order": 1,
        "is_published": False,
    },
    {
        "title": "Bixmerchant",
        "slug": "bixmerchant",
        "description": (
            "Bixmerchant is the easiest payment gateway to pay for goods and "
            "services using cryptocurrency. Sign up and get started today."
        ),
        "static_image": "images/bix-home.png",
        "link": "https://bixmerchant.com/",
        "order": 2,
        "is_published": True,
    },
    {
        "title": "SHT.CX",
        "slug": "sht-cx",
        "description": (
            "Shorten URLs, Create Custom Links, and Track Performance Like a "
            "Pro. Spruce up your link with a custom name. Stand out in the crowd."
        ),
        "static_image": "images/sht-home.png",
        "link": "https://sht.up.railway.app",
        "order": 3,
        "is_published": True,
    },
    {
        "title": "Email Verification",
        "slug": "email-verification",
        "description": (
            "Secure Your Success, One Verified Email at a Time - Simplifying "
            "Email Marketing with OTP Validation!"
        ),
        "static_image": "images/email-home.png",
        "link": "https://veriflux.fly.dev/",
        "order": 4,
        "is_published": True,
    },
    {
        "title": "Notes",
        "slug": "notes",
        "description": (
            "This is a note taking web app that that allows you to priavtely "
            "save and retrieve notes anonymously with a 4 digit code."
        ),
        "static_image": "images/notes-home.png",
        "link": "https://notery.cc/",
        "order": 5,
        "is_published": True,
    },
    {
        "title": "Tasker",
        "slug": "tasker",
        "description": (
            "A multi-purpose web platform that allows to organize personal "
            "notes, shorten URLs, save and share files easily."
        ),
        "static_image": "images/task-home.png",
        "link": "https://task.princewilldev.com/",
        "order": 6,
        "is_published": False,
    },
    {
        "title": "QR",
        "slug": "qr",
        "description": (
            "convenient and user-friendly platform that allows you to "
            "effortlessly convert texts and links into QR codes,."
        ),
        "static_image": "images/qr-home.png",
        "link": "https://getqrcode.fly.dev/",
        "order": 7,
        "is_published": True,
    },
]

SKILLS = [
    {"name": "HTML5", "static_icon": "assets/images/icons/icons-18.png", "order": 1},
    {"name": "CSS", "static_icon": "assets/images/icons/css-icon.png", "order": 2},
    {
        "name": "JavaScript",
        "static_icon": "assets/images/icons/javascript.png",
        "order": 3,
    },
    {
        "name": "Bootstrap",
        "static_icon": "assets/images/icons/bootstrap.png",
        "order": 4,
    },
    {"name": "GitHub", "static_icon": "assets/images/icons/github.png", "order": 5},
    {"name": "PHP", "static_icon": "assets/images/icons/php.png", "order": 6},
    {"name": "Laravel", "static_icon": "assets/images/icons/laravel.jpeg", "order": 7},
    {"name": "Python", "static_icon": "assets/images/icons/python-icon.png", "order": 8},
    {"name": "Django", "static_icon": "assets/images/icons/django-icon.svg", "order": 9},
]
