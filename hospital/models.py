from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.forms import BooleanField, CharField, DecimalField, IntegerField, Textarea
import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from unicodedata import normalize


class Hospital(models.Model):
    okpo = models.CharField(max_length=4, db_index=True, verbose_name='ОКПО', unique=True)
    CHOICES = (
    ('Чуй', 'Чуй'),
    ('Иссык-Куль', 'Иссык-Куль'),
    ('Нарын', 'Нарын'),
    ('Талас', 'Талас'),
    ('Ош', 'Ош'),
    ('Жалал-Абад', 'Жалал-Абад'),
    ('Баткен', 'Баткен'))
    choice = models.CharField(max_length=255, choices=CHOICES)
    max_person = models.DecimalField(max_digits=2, decimal_places=0)
    CHOICE_HOSPITAL = (
        (1, 'Государственная'),
        (0, 'Частная'))
    type_of_hospital = models.BooleanField(choices=CHOICE_HOSPITAL)
    main_doctor = models.OneToOneField('MainDoctor', on_delete=models.CASCADE)


class MainDoctor(models.Model):
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    position = models.CharField(max_length=200)
    bio = models.CharField(max_length=2000)
    d_file = models.FileField(  # models.ImageField - > FileField
        upload_to='files/%Y/%m/%d',
        blank=True,
    )
    pin_passport = models.IntegerField(verbose_name='ПИН КОД паспорта')
    age = models.IntegerField(verbose_name='Возраст')
    skill = models.CharField(max_length=255, verbose_name='Опыт работы')
    number = models.IntegerField(verbose_name='Номер телефона')
    treat_doctor = models.ForeignKey('TreatDoctor', on_delete=models.CASCADE)
    nurse = models.ForeignKey('Nurse', on_delete=models.CASCADE)

    def __str__(self):
        return self.fio

    # def get_absolute_url(self):
    #     return self.pk

class TreatDoctor(models.Model):
    CHOICES = (('Терапевт', 'Терапевт'), ('Хирург', 'Хирург'))
    choice = models.CharField(max_length=255, choices=CHOICES)
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    position = models.CharField(max_length=200)
    bio = models.CharField(max_length=2000)
    d_file = models.FileField(  # models.ImageField - > FileField
        upload_to='files/%Y/%m/%d',
        blank=True,
    )
    pin_passport = models.IntegerField(verbose_name='ПИН КОД паспорта')
    age = models.IntegerField(verbose_name='Возраст')
    skill = models.CharField(max_length=255, verbose_name='Опыт работы')
    number = models.IntegerField(verbose_name='Номер телефона')

    def __str__(self):
        return self.fio

class Nurse(models.Model):
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    pin_passport = models.IntegerField(verbose_name='ПИН КОД паспорта')
    age = models.IntegerField(verbose_name='Возраст')
    number = models.IntegerField(verbose_name='Номер телефона')


class Patient(models.Model):
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    pin_passport = models.IntegerField(verbose_name='ПИН КОД паспорта')
    age = models.IntegerField(verbose_name='Возраст')
    number = models.IntegerField(verbose_name='Номер телефона')
    problem = models.TextField(verbose_name='Причина обращения в больницу')
    gender = models.CharField(max_length=2, choices=(('m', 'male'), ('f', 'female')))

class Customer(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    subject = models.CharField(max_length=200, blank=True)
    text = models.CharField(max_length=500, blank=True)
    status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return self.subject

DOCTOR_CHOICES = (
    ('Black Bull', 'BLACK BULL'),
    ('Brads Bar', 'BRADS BAR'),
    ('Ivy House', 'IVY HOUSE'),
)

TIME_CHOICES = (
    ('9:00 - 9:30', '9:00 - 9:30'),
    ('9:31 - 10:00', '9:31 - 10:00'),
    ('10:31 - 11:00', '10:31 - 11:00'),
    ('11:01 - 11:30', '11:01 - 11:30'),
    ('11:31 - 12:30', '11:31 - 12:30'),
    ('12:31 - 13:00', '12:31 - 13:00'),
    ('13:01 - 13:30', '13:01 - 13:30'),
    ('13:31 - 14:00', '13:31 - 14:00'),
    ('14:01 - 14:30', '14:01 - 14:30'),
    ('14:31 - 15:00', '14:31 - 15:00'),
    ('15:01 - 15:30', '15:01 - 15:30'),
    ('15:31 - 16:00', '15:31 - 16:00'),
    ('16:01 - 16:30', '16:01 - 16:30'),
    ('16:31 - 17:00', '16:31 - 17:00'),
    ('17:01 - 17:30', '17:01 - 17:30'),
    ('17:31 - 18:00', '17:31 - 18:00'),
)

DAY_CHOICES = (
    ('Monday', 'MONDAY'),
    ('Tuesday', 'TUESDAY'),
    ('Wednesday', 'WEDNESDAY'),
    ('Thursday', 'THURSDAY'),
    ('Friday', 'FRIDAY'),
    ('Saturday', 'SATURDAY'),
    ('Sunday', 'SUNDAY'),
)

class Appointment(models.Model):
    cname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    day = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    doctor = models.CharField(max_length=255)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.cname

# class Appointment(models.Model):
#     cname = models.CharField(max_length=100, blank=True)
#     email = models.EmailField(max_length=254,)
#     day = models.CharField(max_length=9, choices=DAY_CHOICES, blank=True)
#     time = models.CharField(max_length=13, choices=TIME_CHOICES, default='09:00',
#                             help_text='Please select a time in 24hr clock format (HH:MM) from the drop down.',
#                             blank=True)
#     doctor = models.CharField(max_length=255, choices=DOCTOR_CHOICES, help_text="", blank=True)
#     text = models.CharField(max_length=500)

    # def __str__(self):
    #     return self.cname