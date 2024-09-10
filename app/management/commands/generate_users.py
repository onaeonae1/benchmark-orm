from django.core.management.base import BaseCommand
from app.models import User
from faker import Faker


class Command(BaseCommand):
    help = "Generates a large number of fake users"

    def handle(self, *args, **kwargs):
        fake = Faker()
        bulk_user_list = [
            User(name=fake.name(), email=fake.email()) for _ in range(50000)
        ]
        User.objects.bulk_create(bulk_user_list)
        self.stdout.write(self.style.SUCCESS("Successfully generated 50000 users"))
