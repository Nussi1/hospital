from django import forms
from .models import Customer, Appointment
from django.forms import ModelForm
from django import forms
from unicodedata import normalize
from django.core.exceptions import ValidationError

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Name'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Email'}
            ),
            'phone': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Phone'}
            ),
            'subject': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Subject'}
            ),
            'text': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Text'}
            ),
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        # widgets = {
        #     'cname' : forms.TextInput(
        #         attrs={'class': 'form-control', 'placeholder': 'Name'}
        #     ),
        #     'email': forms.EmailInput(
        #         attrs={'class': 'form-control', 'placeholder': 'Email'}
        #     ),
        #     'day': forms.TextInput(
        #         attrs={'class': 'form-control', 'placeholder': 'Date'}
        #     ),
        #     'time': forms.TextInput(
        #         attrs={'class': 'form-control', 'placeholder': 'Time'}
        #     ),
        #     'doctor': forms.TextInput(
        #         attrs={'class': 'form-control', 'placeholder': 'Doctor'}
        #     ),
        #     'text': forms.Textarea(
        #         attrs={'class': 'form-control', 'placeholder': 'Text'}
        #     ),
        # }



# class UserModelForm(ModelForm):
#     class Meta:
#         model = UserDetails
#         fields = '__all__'
#
#     def clean_BookingName(self):
#         BookingName = self.cleaned_data.get('BookingName')
#         PubName = self.cleaned_data.get('PubName')
#
#         if (BookingName == ""):
#             raise ValidationError('The Booking Name field cannot be left blank.')
#
#         for instance in UserDetails.objects.all():
#             if instance.PubName == PubName:
#                 if instance.BookingName == BookingName:
#                     raise ValidationError(BookingName + ' already has a booking.')
#         return BookingName
#
#     def clean_TableNo(self):
#         PubName = self.cleaned_data.get('PubName')
#         TableNo = self.cleaned_data.get('TableNo')
#         Day = self.cleaned_data.get('Day')
#         Time = self.cleaned_data.get('Time')
#
#         if (Day == ""):
#             raise ValidationError("Please select a day.")
#
#         if (Time == ""):
#             raise ValidationError("Please select a timeslot.")
#
#         if (PubName == ""):
#             raise ValidationError("Please select a pub.")
#
#         if (TableNo == ""):
#             raise ValidationError("Please select a table.")
#
#         for instance in UserDetails.objects.all():
#             if instance.PubName == PubName:
#                 if instance.TableNo == TableNo:
#                     if instance.Day == Day:
#                         if instance.Time == Time:
#                             raise ValidationError(
#                                 'This table is already booked at that time, please change table number or try another time.')
#         return TableNo