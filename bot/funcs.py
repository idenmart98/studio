from passlib.hash import django_pbkdf2_sha256

def check_password(password, hashed_password):
    return django_pbkdf2_sha256.verify(password, hashed_password)