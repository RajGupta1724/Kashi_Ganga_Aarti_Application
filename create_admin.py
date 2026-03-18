import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kashi_ganga.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
username = "admin"
password = "kashiganga"
email = "admin@kashigangaaarti.in"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Admin user created.")
else:
    print("Admin user already exists.")
