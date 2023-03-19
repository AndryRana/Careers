from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from .models import Registered_email, Support, Message, Notepad, Openings, Countdown, WaitingList, Vacancies
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control #delete the session after logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
import re

# ==============================Frontend==========================================
# Function to render homepage
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    return render(request, "home.html")


# Function to render opportunities page
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def opportunities(request):
    jobOpenings = Openings.objects.all()
    show_countdowns = Countdown.objects.all()
    vacancies = Vacancies.objects.all()
    
    p = Paginator(vacancies, 5)
    page_number = request.GET.get('page')
    page_vacancies = p.get_page(page_number)
     
    return render(request, "opportunities.html", {
        'jobOpenings': jobOpenings, 
        'show_countdowns': show_countdowns, 
        'vacancies': vacancies, 
        'page_vacancies': page_vacancies, 
    })

# Show vacancies description
def description(request, vacancy_id):
    vacancy = Vacancies.objects.get(id=vacancy_id) 
    jobOpenings = Openings.objects.all()
    show_countdowns = Countdown.objects.all()
    if vacancy != None:
        target = vacancy.dataTarget
        ty = re.findall('[a-zA-Z][^A-Z]*', target)
        data = ty[0]
        dataTarget = data.capitalize()
        return render(request, "description.html", {
            "vacancy": vacancy,
            "dataTarget": dataTarget,
            "jobOpenings": jobOpenings,
            "show_countdowns": show_countdowns,
        })

#Function for Support
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def support(request):
    if request.method == "POST":
        # Check if email already exists
        email = request.POST["email"]
        # Candidate or User must exists to contact the support
        if not Registered_email.objects.filter(email=email).exists() and not User.objects.filter(email=email).exists():
            messages.warning(request, 'Your e-mail is not registered yet !')
            return HttpResponseRedirect('/support')
        
        if Support.objects.filter(email=email, situation = 'Pending').exists():
            messages.info(request, ",")
            return HttpResponseRedirect('/support')
        else:
            support = Support()
            
            terms = request.POST.get('terms')
            message = request.POST.get('message')
            person = request.POST.get('person')
            option = request.POST.get('option')
            email = request.POST.get('email')
            
            support.terms = terms
            support.message = message
            support.person = person
            support.option = option
            support.email = email

            support.save()
            messages.success(request, 'Your request will be processed quickly by our teams !')
            if not request.user.is_authenticated:
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('backend')
    else:
            jobOpenings = Openings.objects.all()
            show_countdowns = Countdown.objects.all()
            return render(request, "support.html", {
                'show_countdowns' : show_countdowns,
                'jobOpenings' : jobOpenings,
            })   

# function to send frontend email
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def frontend_email(request):
    if request.method == "POST":
        
         # Check if email already exists
        email = request.POST["email"]
        if Registered_email.objects.filter(email=email).exists():
            messages.error(request, "We already have your resume")
            return HttpResponseRedirect('/opportunities')
        
        else:
            name = request.POST.get("name")
            age = request.POST.get("age")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            address = request.POST.get("address")
            experience = request.POST.get("experience")
            skills = request.POST.get("skills")
            if request.POST.get("vacancy_title") != None:
                vacancy_title = request.POST.get("vacancy_title")

            # save the email in database
            contact = Registered_email()
            contact.email = email
            contact.save()

            template = loader.get_template("resume_form.txt")
            context = {
                "name": name,
                "age": age,
                "email": email,
                "phone": phone,
                "address": address,
                "experience": experience,
                "skills": skills,
                "vacancy_title": vacancy_title,
            }
            message = template.render(context)
            email = EmailMultiAlternatives(
                "Frontend - Candidate",
                message,
                "Frontend Opportunity",
                ["ranamiran75@gmail.com"],
            )
            email.content_subtype = "html"
            file = request.FILES["file"]
            email.attach(file.name, file.read(), file.content_type)
            email.send()
            messages.success(request, "Frontend resume sent successfully !")
            return HttpResponseRedirect("/")
    


# function to send backend email
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def backend_email(request):
    if request.method == "POST":
        
        email = request.POST["email"]
        if Registered_email.objects.filter(email=email).exists():
            messages.error(request, "We already have your resume")
            return HttpResponseRedirect('/opportunities')
        
        else:
            name = request.POST.get("name")
            age = request.POST.get("age")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            address = request.POST.get("address")
            experience = request.POST.get("experience")
            skills = request.POST.get("skills")
            if request.POST.get("vacancy_title") != None:
                vacancy_title = request.POST.get("vacancy_title")

            # save the email in database
            contact = Registered_email()
            contact.email = email
            contact.save()

            template = loader.get_template("resume_form.txt")
            context = {
                "name": name,
                "age": age,
                "email": email,
                "phone": phone,
                "address": address,
                "experience": experience,
                "skills": skills,
                "vacancy_title": vacancy_title,
            }
            message = template.render(context)
            email = EmailMultiAlternatives(
                "Backend - Candidate",
                message,
                "Backend Opportunity",
                ["ranamiran75@gmail.com"],
            )
            email.content_subtype = "html"
            file = request.FILES["file"]
            email.attach(file.name, file.read(), file.content_type)
            email.send()
            messages.success(request, "Backend resume sent successfully !")
            return HttpResponseRedirect("/")


# function to send fullstack email
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def fullstack_email(request):
    if request.method == "POST":
        
        # Check if email already exists
        email = request.POST["email"]
        if Registered_email.objects.filter(email=email).exists():
            messages.error(request, "We already have your resume")
            return HttpResponseRedirect('/opportunities')
        
        else:
            name = request.POST.get("name")
            age = request.POST.get("age")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            address = request.POST.get("address")
            experience = request.POST.get("experience")
            skills = request.POST.get("skills")
            if request.POST.get("vacancy_title") != None:
                vacancy_title = request.POST.get("vacancy_title")
            
            # save the email in database
            contact = Registered_email()
            contact.email = email
            contact.save()
            
            template = loader.get_template("resume_form.txt")
            context = {
                "name": name,
                "age": age,
                "email": email,
                "phone": phone,
                "address": address,
                "experience": experience,
                "skills": skills,
                "vacancy_title": vacancy_title,
            }
            message = template.render(context)
            email = EmailMultiAlternatives(
                "Fullstack - Candidate",
                message,
                "Fullstack Opportunity",
                ["ranamiran75@gmail.com"],
            )
            email.content_subtype = "html"
            file = request.FILES["file"]
            email.attach(file.name, file.read(), file.content_type)
            email.send()
            messages.success(request, "Fullstack resume sent successfully !")
            return HttpResponseRedirect("/")
        
# function to send intern email
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def intern_email(request):
    if request.method == "POST":
        
        # Check if email already exists
        email = request.POST["email"]
        if Registered_email.objects.filter(email=email).exists():
            messages.error(request, "We already have your resume")
            return HttpResponseRedirect('/opportunities')
        
        else:
            name = request.POST.get("name")
            age = request.POST.get("age")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            address = request.POST.get("address")
            experience = request.POST.get("experience")
            skills = request.POST.get("skills")
            if request.POST.get("vacancy_title") != None:
                vacancy_title = request.POST.get("vacancy_title")
            
            # save the email in database
            contact = Registered_email()
            contact.email = email
            contact.save()
            
            template = loader.get_template("resume_form.txt")
            context = {
                "name": name,
                "age": age,
                "email": email,
                "phone": phone,
                "address": address,
                "experience": experience,
                "skills": skills,
                "vacancy_title": vacancy_title,
            }
            message = template.render(context)
            email = EmailMultiAlternatives(
                "Intern - Candidate",
                message,
                "Intern Opportunity",
                ["ranamiran75@gmail.com"],
            )
            email.content_subtype = "html"
            file = request.FILES["file"]
            email.attach(file.name, file.read(), file.content_type)
            email.send()
            messages.success(request, "Intern resume sent successfully !")
            return HttpResponseRedirect("/")


#Send message
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def send_message(request):
    if request.method == "POST":
        if request.POST["message"]:
            send_message = request.POST["message"]
            message = Message.objects.get_or_create(message=send_message)
            messages.success(request, "Message sent successfully!")
            return HttpResponseRedirect("/")
    else:
        return render(request, "home.html")
        

# Waiting list
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def waiting_list(request):
    if request.method == "POST":
    
        # Check if email exist in DB
        email = request.POST['email']
        if WaitingList.objects.filter(email = email).exists():
            messages.warning(request, ",") 
            return HttpResponseRedirect('/waiting_list')
        else:
            
            file = request.FILES['document']
            store_file = FileSystemStorage()
            document = store_file.save(file.name, file)

            waiting = WaitingList(
            post = request.POST.get('post'),
            email = request.POST.get('email'),
            document = document,
            message = request.POST.get('message'))

            waiting.save()
            messages.success(request, 'Your message was successfully registered !')
            return HttpResponseRedirect('/')
    else:
            show_countdowns = Countdown.objects.all()
            return render(request, 'waiting_list.html', {
                'show_countdowns' : show_countdowns
            })
            
        
# ==============================Backend==========================================

@login_required(login_url = "login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def backend (request):
    number = Registered_email.objects.all().count()
    allNotes = Notepad.objects.all()
    jobOpenings = Openings.objects.all()
    show_countdowns = Countdown.objects.all()
    return render(request, "backend.html", {
        'total_number': number, 
        'allNotes': allNotes,
        'jobOpenings': jobOpenings,
        'show_countdowns': show_countdowns,
        })

@login_required(login_url = "login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def notepad(request):
    if request.method == 'POST':
        edit_notepad = Notepad.objects.get(id=request.POST.get('id'))
        if edit_notepad != None:
            edit_notepad.title = request.POST.get('title')
            edit_notepad.text = request.POST.get('text')
            edit_notepad.save()
            messages.success(request, 'The Notepad was successfully updated!')
            return HttpResponseRedirect('/backend')

#Job Openings
@login_required(login_url = "login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def openings(request):
    if request.method == 'POST':
        opening = Openings.objects.get(id=request.POST.get('id'))
        if opening != None:
            opening.backend = request.POST.get('backend')
            opening.frontend = request.POST.get('frontend')
            opening.fullstack = request.POST.get('fullstack')
            opening.intern = request.POST.get('intern')
            opening.save()
            messages.success(request, 'Job openings was successfully updated!')
            return HttpResponseRedirect('/backend')

#Vacancies
@login_required(login_url = "login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def vacancies(request):
    if request.method == 'POST':
        dataTarget = request.POST['target']
        title = request.POST['title']
        description = request.POST['description']
        vacancy = Vacancies(
            dataTarget=dataTarget, 
            title=title, 
            description=description
        )
        vacancy.save()
        messages.success(request, 'Vacancy was created successfully !')
        return HttpResponseRedirect('/backend')
    

#Countdown
@login_required(login_url = "login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def countdown(request):
    if request.method == 'POST':
        show_countdown = Countdown.objects.get(id=request.POST.get('id'))
        if show_countdown != None:
            show_countdown.timer = request.POST.get('timer')
            show_countdown.save()
            messages.success(request, "Countdown was successfully updated")
            return HttpResponseRedirect('/backend')