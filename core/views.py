from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from .models import *
from .forms import *


def home(request):
    if request.user.is_authenticated:
        obj = EmailAdd.objects.all().order_by('-id')
        history = MessageSendHistory.objects.all()
        historys = MessageSendHistory.objects.all()
        user = User.objects.all()
        uCategory = dict()
        for unique in obj:
            if unique.category in uCategory:
                uCategory[unique.category] += 1
            else:
                uCategory[unique.category] = 1

        context = {
            'email': obj,
            'len': len(obj),
            'category': uCategory,
            'totalcategory': len(uCategory),
            'countuser': len(user),
            'history': len(history),
            'historys': historys
        }
        return render(request, 'home/index.html', context)
    else:
        return redirect("/signin")


def sendMail(request):
    obj = EmailAdd.objects.all()
    historys = MessageSendHistory.objects.all()
    uCategory = dict()
    for unique in obj:
        if unique.category in uCategory:
            uCategory[unique.category] += 1
        else:
            uCategory[unique.category] = 1
    context = {
        'category': uCategory,
        'historys': historys
    }
    if request.method == 'POST':
        from_ = request.POST.get('from')
        get_to = request.POST.get('to')
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        text_convert = strip_tags(body)
        toemail = EmailAdd.objects.filter(category=get_to)
        for to in toemail:
            email = EmailMultiAlternatives(
                subject, text_convert, from_, [to.email])
            email.attach_alternative(body, 'text/html')
            email.send()
            history = MessageSendHistory(
                message="Message sent successfully", category=to.category)
            history.save()
    return render(request, 'home/sendmail.html', context)


def tableview(request):
    obj = EmailAdd.objects.all().order_by('-id')
    historys = MessageSendHistory.objects.all()
    uCategory = dict()
    for unique in obj:
        if unique.category in uCategory:
            uCategory[unique.category] += 1
        else:
            uCategory[unique.category] = 1

    context = {
        'email': obj,
        'len': len(obj),
        'category': uCategory,
        'totalcategory': len(uCategory),
        'historys': historys
    }
    return render(request, 'home/tables.html', context)


def categoryTable(request, category):
    categoryTable = EmailAdd.objects.filter(category=category)
    historys = MessageSendHistory.objects.all()
    obj = EmailAdd.objects.all()
    uCategory = dict()
    for unique in obj:
        if unique.category in uCategory:
            uCategory[unique.category] += 1
        else:
            uCategory[unique.category] = 1

    context = {
        'table': categoryTable,
        'category': uCategory,
        'title': category,
        'historys': historys
    }
    return render(request, 'home/categorytable.html', context)


def addemail(request):
    historys = MessageSendHistory.objects.all()
    form = AddEmailForm()
    obj = EmailAdd.objects.all()
    uCategory = dict()
    for unique in obj:
        if unique.category in uCategory:
            uCategory[unique.category] += 1
        else:
            uCategory[unique.category] = 1

    context = {
        'category': uCategory,
        'form': form,
        'historys': historys
    }
    if request.method == 'POST':
        form = AddEmailForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            category = form.cleaned_data['category'].upper()
            data = EmailAdd(email=email, category=category)
            data.save()
            return redirect('/add-email')
    return render(request, 'home/addemail.html', context)


def updateemail(request, id):
    get_id = EmailAdd.objects.get(id=id)
    form = AddEmailForm(instance=get_id)
    obj = EmailAdd.objects.all()
    historys = MessageSendHistory.objects.all()
    uCategory = dict()
    for unique in obj:
        if unique.category in uCategory:
            uCategory[unique.category] += 1
        else:
            uCategory[unique.category] = 1
    context = {
        'category': uCategory,
        'form': form,
        'historys': historys
    }
    if request.method == 'POST':
        form = AddEmailForm(request.POST, request.FILES, instance=get_id)
        if form.is_valid():
            email = form.cleaned_data['email']
            category = form.cleaned_data['category'].upper()
            data = EmailAdd(id=20, email=email, category=category)
            data.save()
            return redirect('/tables')
    return render(request, 'home/updateemail.html', context)


def delete(request, pk):
    id = pk
    obj = EmailAdd.objects.get(id=id)
    obj.delete()
    return redirect("/tables")


def history(request):
    history = MessageSendHistory.objects.all()
    historys = MessageSendHistory.objects.all()
    obj = EmailAdd.objects.all()
    uCategory = dict()
    for unique in obj:
        if unique.category in uCategory:
            uCategory[unique.category] += 1
        else:
            uCategory[unique.category] = 1
    context = {
        'history': history,
        'historys': historys,
        'category': uCategory,
    }
    return render(request, 'home/history.html', context)


def historydelete(request, pk):
    id = pk
    obj = MessageSendHistory.objects.get(id=id)
    obj.delete()
    return redirect("/history")
