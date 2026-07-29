from django.contrib import admin
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _("Django administration")
admin.site.site_title = _("Django admin")
admin.site.index_title = _("Django management dashboard")
