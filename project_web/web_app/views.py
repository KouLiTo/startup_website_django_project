from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import forms
from . models import Projects, Basic, Standard, Premium
from django.views.generic import TemplateView
from django.core.paginator import Paginator
import smtplib
from .static import passwords as p


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


def send_mail(msg: str):
    sender_mail = p.sender_mail
    password = p.sender_mail_password
    server = smtplib.SMTP("smtp.office365.com", 587)
    server.starttls()
    try:
        server.login(sender_mail, password)
        print("Login success")
        server.sendmail(sender_mail, p.receiver_mail, msg)
        print(f"Email has been sent")
    except BaseException as E:
        print(E, "Error! We failed to send email! Check configurations")


@csrf_exempt
def contact_sent(request):
    form = forms.FeedbackForm(request.POST)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        form.save()
        if data["subject"] == "technical question":
            msg = "\n" * 4 + "Customer's mail address: " + data["email"] + "\n" * 2 + data["text"]
            send_mail(msg=msg)
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
        all_apps = Projects.objects.all().order_by("-id")
        paginator = Paginator(all_apps, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {
            "page_obj": page_obj,
            "all_projects": all_apps
        }
        return render(request, self.template_name, context)



class TableData(TemplateView):
    template_name = "services.html"

    def get(self, request, *args, **kwargs):
        try:
            basics = Basic.objects.all().order_by("-id")[0]
            standards = Standard.objects.all().order_by("-id")[0]
            premiums = Premium.objects.all().order_by("-id")[0]
            context = {
                "basics": basics,
                "standards": standards,
                "premiums": premiums
            }
            return render(request, self.template_name, context)
        except Exception:
            return HttpResponse("There are no data yet. Site is being updated, please wait")


