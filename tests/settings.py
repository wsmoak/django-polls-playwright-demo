from config.settings import *  # Import base settings

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_polls_playwright_demo",
        "USER": "demo_app_tester",
        "PASSWORD": "verysecret",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
