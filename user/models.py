from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserRoleChoices(models.TextChoices):
    ADMIN = "Admin", _("Admin")
    USER = "User", _("User")

class User(models.Model):
    email = models.EmailField(max_length=255, primary_key=True)
    username = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    address = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(
        max_length=255, null=False, blank=False, choices=UserRoleChoices.choices
    )
    class Meta:
        indexes = [models.Index(fields=["email"], name="pblc_usr_signp_email_idx_0001")]
        db_table = 'users'
