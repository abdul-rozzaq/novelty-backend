import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from accounts.models import User
from faker import Faker



fake = Faker()


for x in range(20):
    name = [y for y in fake.name().split(' ') if y != 'Dr.']

    
    num = fake.random_number(digits=8)
    user = User.objects.create(first_name=name[0], last_name=name[1], phone=f"+9989{num}")
    
    # +9989 12345678
