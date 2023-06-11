import django
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "s25.settings")
django.setup()
from web import models

models.UserInfo.objects.create(username='陈硕', email='chengshuo@163.com', mobile_phone='13183838381', password='123123')
