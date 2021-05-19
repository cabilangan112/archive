from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
 
        if not email:
            raise ValueError("Email is required.")

        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password=None, **kwargs):
        user = self.create_user(username, password, **kwargs)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user