from django.db import models
from faker import Faker

class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)


    def __str__(self):
        return self.name

    def get_phones_7(self):
        return Phone.objects.filter(phone_number__endswith='7')

    def get_phones_985(self):
        return Phone.objects.filter(phone_number__endswith='985')

    def get_all_phones(self):
        return Phone.objects.all()

def create_fake_phone_numbers(n):
    fake = Faker()
    for i in range(n):
        name = fake.name()
        phone_number = fake.phone_number()
        Phone.objects.create(name=name, phone_number=phone_number)