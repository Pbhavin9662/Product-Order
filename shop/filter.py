import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


# class OrderFilter(django_filters.FilterSet):
#     start_date = DateFilter(field_name="date_created", lookup_expr='gte')
#     end_date = DateFilter(field_name="date_created", lookup_expr='lte')
#     product_id = CharFilter(field_name='product', lookup_expr='icontains')
#
#     class Meta:
#         model = Order
#         fields = ('product_id')
#         exclude = ['customer', 'date_created']
