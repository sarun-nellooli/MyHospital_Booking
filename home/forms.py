from cProfile import label
from datetime import date
from tkinter import Widget
from django import forms
from .models import Booking

class DateInput(forms.DateInput):
     input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
          model = Booking
          fields = '__all__'
          widgets= {
            'booking_date':DateInput(), 
          }
          labels={
            'p_name':'Name',
            'p_phone':'Phone',
            'p_email':'E-mail',
            'doc_name':'Doctor Name',
            'booking_date':'Booking Date',
            
          }