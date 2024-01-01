from django import forms
from django.core import validators
from django.forms.widgets import NumberInput
import datetime

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']


FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
class contactForm(forms.Form):
    name = forms.CharField(label="Name", initial='Hasib Hasan', required = True,)
    email = forms.EmailField(label = "Email",  required = True,)
    comments = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    upload_file = forms.FileField()
    File_path = forms.FilePathField(path ="E:\Batch 3\Software Devolepment Project")
    upload_image = forms.ImageField()
    Your_portfolio_link = forms.URLField()
    agree = forms.BooleanField(label="Agree with condition",initial=False)
    date = forms.DateField(label="Today is:",initial=datetime.date.today)
    birth_date = forms.DateField(label="Your Birth date",widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(label="Your Birth Year",widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    Rating = forms.DecimalField(label="Rate our website")
    message = forms.CharField(label="Write a short message within 10 word",
	max_length = 10,
    )
    favorite_color = forms.ChoiceField(label="Your favourite color",choices=FAVORITE_COLORS_CHOICES)

    Choice_color = forms.ChoiceField(label="Choose any of color",widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    Multiple_colors = forms.MultipleChoiceField(label="Your can mark multiple color",choices=FAVORITE_COLORS_CHOICES)
    colors_select = forms.MultipleChoiceField(label="Select more than one color",widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
    duration = forms.DateField()
    

class inputForm(forms.Form):
    first_name = forms.CharField(label="Max length less than 20",max_length=20)
    last_name = forms.CharField(label="Max length less than 20",max_length=200)
    roll_number = forms.IntegerField(
        help_text="Enter 6 digit roll number"
    )
    password = forms.CharField( help_text="At least 8 digit", widget=forms.PasswordInput())
