import django_filters
from django.forms import DateInput
from django import forms

from .models import Product


class ProductFilter(django_filters.FilterSet):

    # filters.LOOKUP_TYPES = [
    #     ('', '---------'),
    #     ('exact', 'Is equal to'),
    #     ('not_exact', 'Is not equal to'),
    #     ('lt', 'Lesser than'),
    #     ('gt', 'Greater than'),
    #     ('gte', 'Greater than or equal to'),
    #     ('lte', 'Lesser than or equal to'),
    #     ('startswith', 'Starts with'),
    #     ('endswith', 'Ends with'),
    #     ('contains', 'Contains'),
    #     ('not_contains', 'Does not contain'),
    # ]
    #
    # STATUS_CHOICES = (
    #     (0, 'Regular'),
    #     (1, 'Manager'),
    #     (2, 'Admin'),
    # )
    #
    # class F(FilterSet):
    #     status = ChoiceFilter(choices=STATUS_CHOICES)

    class DateInput(forms.DateInput):
        input_type = 'date'

    name = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(lookup_expr='icontains')
    publish_date = django_filters.DateFilter(lookup_expr='icontains')
    widgets = {
        'publish_date': DateInput(),
    }
    class Meta:
        model = Product
        fields = ['name','category','publish_date']
