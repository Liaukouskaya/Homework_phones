from django.urls import path
from .views import phones_7_view, phones_985_view, all_phones_view

urlpatterns = [
    path('phone_numbers/ends-with-7/', phones_7_view, name='phones_7'),
    path('phone_numbers/ends-with-985/', phones_985_view, name='phones_985'),
    path('phone_numbers/all_phones/', all_phones_view, name='all_phones'),
]
