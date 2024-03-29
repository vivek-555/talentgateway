from django.contrib.auth.decorators import user_passes_test


def group_required(group_names=None, redirect_url=None):
    """Requires user membership in at least one of the groups passed in."""

    def in_groups(u):
        if u.is_superuser or bool(u.groups.filter(name__in=group_names)):
            return True
        return False

    return user_passes_test(in_groups, login_url=redirect_url)
