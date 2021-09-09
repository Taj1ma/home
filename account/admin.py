from django.contrib import admin
from django.contrib.auth import get_user_model
# работа с админ панелью

User = get_user_model()

admin.site.register(User)