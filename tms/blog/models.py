from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class SettingModel(models.Model):
    company_name = models.CharField(max_length=200)
    company_email = models.CharField(max_length=200)
    company_phone = models.CharField(max_length=100)
    company_address = models.CharField(max_length=200)
    company_logo = models.ImageField(upload_to='logo', null=True)
    company_fax = models.IntegerField(null=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'setting'


class Slider(models.Model):
    is_first_option = (
        ('y', 'Yes'),
        ('n', 'No')
    )
    title = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='slider')
    description = RichTextField()
    status = models.BooleanField(default=0)
    is_first = models.CharField(max_length=1, choices=is_first_option)

    def __str__(self):
        return self.title


class BlogCategory(models.Model):
    status = models.BooleanField(default=0)
    cat_name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='category', null=False)
    description = RichTextField()

    def __str__(self):
        return self.cat_name


class BlogNews(models.Model):
    created_at = models.DateTimeField(timezone.now())
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=0)
    cat_id = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='blog', null=False)
    description = RichTextField()
    page_visit = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='about')
    description = RichTextField()


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    message = models.TextField()


class Package(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='package')
    description = RichTextField()

    def __str__(self):
        return self.title

    def get_price(self):
        return "{0:.2f}".format(self.price / 100)


class Hotel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='hotel')
    description = RichTextField()

    def __str__(self):
        return self.title

    def get_price(self):
        return "{0:.2f}".format(self.price / 100)


class Booking(models.Model):
    booking_date = models.DateField()
    package_id = models.ForeignKey(Package, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=0)


class HotelBooking(models.Model):
    booking_date = models.DateField()
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=0)


class Terms(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()


class Policy(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()


class Enquiry(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    details = models.CharField(max_length=255)
