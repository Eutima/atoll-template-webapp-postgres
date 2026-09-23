from .base import *  # noqa: F401,F403

DEBUG = False

ALLOWED_HOSTS = ["testserver"]

# Hardcoded, not env-derived: tests must not depend on a developer's local .env.
MFA_ENABLED = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
