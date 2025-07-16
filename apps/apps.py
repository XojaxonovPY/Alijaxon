from django.apps import AppConfig


class AppsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps'

    def ready(self):
        from apps.models import User
        import apps.signals
        SUPER_PHONE = '9987'
        SUPER_PASS = '1'

        if SUPER_PHONE and SUPER_PASS:
            if not User.objects.filter(phone_number=SUPER_PHONE).exists():
                User.objects.create_superuser(
                    phone_number=SUPER_PHONE,
                    password=SUPER_PASS,
                    is_staff=True,
                    is_superuser=True
                )
                print(f"✅ Superuser created: {SUPER_PHONE}")
            else:
                print("ℹ️ Superuser already exists.")
