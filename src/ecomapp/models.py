from django.db import models
from django.urls import reverse


CATEGORIES = (
    ('food','Food'),
    ('misc', 'Miscellaneous'),
    ('daily','Daily'),
    ('basic','Basic'),
    ('unk','Unknown'),
)


class Product(models.Model):

    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=250)
    category = models.CharField(max_length=50, choices=CATEGORIES, default='food')
    images = models.FileField(default='')
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    user = models.CharField(max_length=30)
    publish_date = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - ' + self.category

    def get_absolute_url(self):
        return reverse("ecomapp:detail", kwargs= {"pk": self.pk})
