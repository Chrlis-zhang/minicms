from .models import Column

nav_display_columns = Column.objects.filter(nav_display=True)


def nav_column(request):
    return {'nav_display+columns':nav_display_columns}
