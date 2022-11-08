REDIRECT_FIELD_NAME = "next"
# NÃO TERMINADO!!!
from django.contrib.auth.decorators import user_passes_test
def logout_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None
):
    """
    Decorator for views that checks that the user is logged out, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: not u.is_authenticated,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator