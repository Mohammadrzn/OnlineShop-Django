from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import AbstractUser, Group


class Customer(AbstractUser, BaseModel):
    mobile = models.CharField("موبایل", max_length=11,  help_text="مثال: 9123456789", null=True, blank=True)
    telephone = models.SmallIntegerField("تلفن", help_text="شماره کامل همراه با کد شهر", null=True, blank=True)
    national_id = models.CharField("کد ملی", max_length=10, null=True, blank=True)
    age = models.SmallIntegerField("سن", null=True, blank=True)
    created_at = None

    ROLE_CHOICES = (
        ("A", "ادمین"),
        ("O", "ناظر"),
        ("C", "مشتری")
    )
    role = models.CharField("نقش", choices=ROLE_CHOICES, max_length=1, default="C", null=False, blank=False)

    GENDER_CHOICES = (
        ("M", "آقا"),
        ("F", "خانم")
    )
    gender = models.CharField("جنسیت", choices=GENDER_CHOICES, max_length=1, null=True, blank=True)

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.username


class Address(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses', related_query_name='address')
    state = models.CharField("استان", max_length=75, null=False, blank=False)
    city = models.CharField("شهر", max_length=100, null=False, blank=False)
    full_address = models.TextField("آدرس", help_text="آدرس کامل همراه با شماره پلاک و واحد", null=False, blank=False)
    postal_code = models.SmallIntegerField("کد پستی", null=False, blank=False)
    is_default = models.BooleanField("آدرس پیش فرض", null=True, blank=True)
    is_deleted = None

    class Meta:
        verbose_name = "آدرس"
        verbose_name_plural = "آدرس ها"

    def __str__(self):
        return f"{self.customer_id}"
