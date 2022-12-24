from django.forms import ModelForm, Form
from . import models
#from .models import Feedback
from django import forms
from django.http import HttpResponse


class FeedbackForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["subject"].empty_label = "Subject is not chosen"


    class Meta:
        model = models.Feedback
        fields = ["name",
                  "surname",
                  "email",
                  "mobile",
                  "subject",
                  "text"
                  ]
        widgets = {
            "name": forms.TextInput(attrs={
                'style': 'width: 300px',
            }),
            "surname": forms.TextInput(attrs={
                'style': 'width: 280px',
            }),
            "email": forms.TextInput(attrs={
                'style': 'width: 300px',
            }),
            "mobile": forms.TextInput(attrs={
                'style': 'width: 290px',
            }),
            "subject": forms.Select(attrs={
                'style': 'width: 295px',
            }),
            "text": forms.Textarea(attrs={
                'cols': 80,
                "rows": 15
            })
        }
