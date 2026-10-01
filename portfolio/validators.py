from django.core.exceptions import ValidationError

MAX_CV_SIZE = 10 * 1024 * 1024  # 10 MB


def validate_cv_size(file):
    """Reject CV uploads larger than MAX_CV_SIZE."""
    if file.size > MAX_CV_SIZE:
        raise ValidationError(
            f"File is too large ({file.size / (1024 * 1024):.1f} MB). "
            f"Maximum allowed size is {MAX_CV_SIZE // (1024 * 1024)} MB."
        )
