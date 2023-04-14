from django.shortcuts import render
from .models import Phone

def phones_7_view(request):
    phones_7 = Phone.objects.filter(phone_number__endswith='7')
    return render(request, 'phone_numbers/phone_numbers_7.html', {'phone_numbers': phones_7})

def phones_985_view(request):
    phones_985 = Phone.objects.filter(phone_number__endswith='985')
    return render(request, 'phone_numbers/phone_numbers_985.html', {'phone_numbers': phones_985})

def all_phones_view(request):
    all_phones = Phone.objects.all()
    return render(request, 'phone_numbers/all_phone_numbers.html', {'phone_numbers': all_phones})
