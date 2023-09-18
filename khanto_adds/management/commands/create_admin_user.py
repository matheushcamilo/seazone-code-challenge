from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Creates a user with admin permissions"

    def handle(self, *args, **options):
        from django.contrib.auth.models import User

        User.objects.filter(username="admin").delete()

        User.objects.create_superuser(
            username="admin",
            email="admin@seazone.com",
            password="admin",
        )

        self.stdout.write(self.style.SUCCESS("Admin user created successfully"))
        self.stdout.write(self.style.SUCCESS("Username: admin\nPassword: admin"))


