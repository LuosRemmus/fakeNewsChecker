from django.contrib import admin

from src.users.models import User

admin.site.register(User)
admin.site.site_title = "Администрирование"
admin.site.site_header = "Администрирование FakeNewsChecker"
admin.site.index_title = "FakeNewsChecker"
