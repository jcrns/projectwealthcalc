from django.contrib import admin

from .models import Assets, Liabilities, Expenses

admin.site.register(Assets)
admin.site.register(Liabilities)
admin.site.register(Expenses)
