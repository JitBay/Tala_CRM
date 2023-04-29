from django.contrib import admin
from .models import Lead, Agent, User, UserProfile, Category

admin.site.register(Lead)
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(User)
admin.site.register(Agent)

admin.site.site_header = 'TALA Administration'

admin.site.index_title = "TALA Administration"