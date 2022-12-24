from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import forms
from . models import Projects
from django.views.generic import TemplateView


# Create your views here.

def homepage(request):
    return render(request, "homepage.html")


def income(request):
    return render(request, "passive_income.html")


@csrf_exempt
def calculate(request):
    games = request.POST["numeric"]
    res = eval("{} * 50".format(str(abs(int(games)))))
    context = {
        "result": res,
        "games": str(abs(int(games)))
         }
    return render(request, "result.html", context)


def contact_form(request):
    form_for_contact = forms.FeedbackForm
    context = {
        "form_for_contact": form_for_contact
    }
    return render(request, "contact_form.html", context)


@csrf_exempt
def contact_sent(request):
    form = forms.FeedbackForm(request.POST)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        print(data)
        form.save()
        context = {
            "msg": "Thank you for your message. We will be in touch with you soon"
        }
        return render(request, "sent.html", context)
    else:
        context = {
            "form_for_contact": form
        }
        return render(request, "contact_form.html", context)


class Objects(TemplateView):
    template_name = "our_apps.html"

    def get(self, request, *args, **kwargs):
        all_apps = Projects.objects.all()

        context = {
            "all_projects": all_apps
        }
        return render(request, self.template_name, context)