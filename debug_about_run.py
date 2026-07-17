import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','kashi_ganga.settings')
import django
django.setup()
from django.conf import settings
if 'testserver' not in settings.ALLOWED_HOSTS:
    settings.ALLOWED_HOSTS.append('testserver')
from django.test import Client
c = Client()
resp = c.get('/about/', HTTP_HOST='testserver')
print('STATUS', resp.status_code)
html = resp.content.decode('utf-8')
print('HAS ABOUT SECTION:', 'About Our Site' in html)
# print a short snippet around the section
idx = html.find('About Our Site')
if idx!=-1:
    print(html[idx-200:idx+200])
else:
    print(html[:800])
