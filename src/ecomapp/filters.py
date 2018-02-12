import django_filters
from django_filters import FilterSet
from .models import Product
from django_filters import filters
from django_filters.widgets import LinkWidget

filters.LOOKUP_TYPES = ['gt', 'gte', 'lt', 'lte', 'custom_lookup_type']


class ProductFilter(FilterSet):

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

    # BOOLEAN_CHOICES = (('false', 'False'), ('true', 'True'),)
    # category = django_filters.TypedChoiceFilter(choices=BOOLEAN_CHOICES,coerce=strtobool)

    categories = Product.objects.values_list('category','category')

    # f = ProductFilter({'price_0': '5', 'price_1': '15'}, queryset=qs)

    price = django_filters.RangeFilter()
    name = django_filters.CharFilter(lookup_expr='icontains')

    # category = django_filters.CharFilter()

    category = django_filters.ChoiceFilter(
        label="Choose the categories",
        choices=categories,
        widget=LinkWidget
    )

    class Meta:
        model = Product
        fields = ['name','price','category']

qs = Product.objects.all().order_by('name')
f = ProductFilter("{price_0': '0', 'price_1': '400000000'}",queryset=qs)