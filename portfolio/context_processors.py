from .models import SiteProfile


def site_profile(request):
    """Expose the editable homepage content to every template as ``site``."""
    return {"site": SiteProfile.get_solo()}
