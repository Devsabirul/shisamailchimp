from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import pandas as pd
import os


def home(request):
    if request.user.is_authenticated:
        obj = EmailAdd.objects.all().order_by('-id')
        history = MessageSendHistory.objects.all()
        historys = MessageSendHistory.objects.all().order_by('-id')
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
        return redirect("signin")


@login_required(login_url='signin')
def sendMail(request):
    obj = EmailAdd.objects.all()
    historys = MessageSendHistory.objects.all().order_by('-id')
    history = MessageSendHistory.objects.all()
    uCategory = dict()
    for unique in obj:
        if unique.category in uCategory:
            uCategory[unique.category] += 1
        else:
            uCategory[unique.category] = 1
    context = {
        'category': uCategory,
        'historys': historys,
        'history': len(history)
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

@login_required(login_url='signin')
def tableview(request):
    obj = EmailAdd.objects.all().order_by('-id')
    historys = MessageSendHistory.objects.all().order_by('-id')
    history = MessageSendHistory.objects.all()
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
        'historys': historys,
        'history': len(history)
    }
    return render(request, 'home/tables.html', context)

@login_required(login_url='signin')
def categoryTable(request, category):
    categoryTable = EmailAdd.objects.filter(category=category)
    historys = MessageSendHistory.objects.all().order_by('-id')
    history = MessageSendHistory.objects.all()
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
        'historys': historys,
        'history': len(history)
    }
    return render(request, 'home/categorytable.html', context)

@login_required(login_url='signin')
def addemail(request):
    historys = MessageSendHistory.objects.all().order_by('-id')
    history = MessageSendHistory.objects.all()
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
        'historys': historys,
        'history': len(history)
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

@login_required(login_url='signin')
def settings(request):
    obj = EmailAdd.objects.all()
    uCategory = dict()
    for unique in obj:
        if unique.category in uCategory:
            uCategory[unique.category] += 1
        else:
            uCategory[unique.category] = 1

    context = {
        'category': uCategory,
    }
    return render(request,"home/settings.html",context)

def update_user(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            user = User.objects.get(username=request.user.username)
            user.first_name = name
            user.email = email
            user.save()
            notification = MessageSendHistory(
                message="User update successfully", category="User Update")
            notification.save()
        return redirect("history")
    else:
        return redirect("signin")


def change_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            password = request.POST.get('password')
            user = User.objects.get(username=request.user.username)
            user.set_password(password)
            user.save()
            notification = MessageSendHistory(
                message="Password change successfully", category="chagne password")
            notification.save()
        return redirect("history")
    else:
        return redirect("signin")


@login_required(login_url='signin')
def updateemail(request, id):
    get_id = EmailAdd.objects.get(id=id)
    form = AddEmailForm(instance=get_id)
    obj = EmailAdd.objects.all()
    historys = MessageSendHistory.objects.all().order_by('-id')
    history = MessageSendHistory.objects.all()
    uCategory = dict()
    for unique in obj:
        if unique.category in uCategory:
            uCategory[unique.category] += 1
        else:
            uCategory[unique.category] = 1
    context = {
        'category': uCategory,
        'form': form,
        'historys': historys,
        'history': len(history)
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

@login_required(login_url='signin')
def delete(request, pk):
    id = pk
    obj = EmailAdd.objects.get(id=id)
    obj.delete()
    return redirect("/tables")

@login_required(login_url='signin')
def history(request):
    historys = MessageSendHistory.objects.order_by('-id')
    length = MessageSendHistory.objects.all()
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
        'length': len(length),
        'category': uCategory,
    }
    return render(request, 'home/history.html', context)

@login_required(login_url='signin')
def historydelete(request, pk):
    id = pk
    obj = MessageSendHistory.objects.get(id=id)
    obj.delete()
    return redirect("/history")


# Error Page Handel
def handle_not_found(request, exception):
    return render(request, 'home/404.html')

    

@login_required(login_url='signin')
# export data to excel
def export_data_to_excel(request):
    try:
        email_data = EmailAdd.objects.all()
        data = []
        
        for i in email_data:
            data.append({
                "email": i.email,
                "category": i.category
            })
        
        df = pd.DataFrame(data)
        filepath = "data.xlsx"  # Modify the file path as per your requirements
        df.to_excel(filepath, index=False)
        file_location = os.path.abspath(filepath)
        return JsonResponse({
            'status': 200,
            'file_path': file_location,
            'data':data
        })
    except Exception as e:
        return JsonResponse({
            'status': 500,
            'message': f'An error occurred: {str(e)}'
        })