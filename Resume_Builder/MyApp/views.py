from io import SEEK_CUR
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Resume

# Create your views here.
from django.contrib import messages
from django.http import HttpResponseNotFound

from django.contrib.auth.models import User, auth
from django.http import HttpResponse
# from django.core.urlresolvers import resolve

from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,"index.html")
def login(request):
    if request.method == "POST":
        username = request.POST.get("username").strip().lower()
        password = request.POST.get("password")
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('MyApp:index')
        else:
            messages.info(request,'invalid credientials')
            return redirect('/login/')
    else:
        return render(request,"login.html")

def register(request):
    
    if request.method == 'POST': 
        if request.POST['username'] and request.POST['first_name'] and request.POST['email'] and request.POST['pass1'] and request.POST['pass2'] :
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2'] 
            if pass1 == pass2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'User already exists with that username.')
                    return redirect('MyApp:register')
                
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Email already registered')
                    return redirect('MyApp:register')


                else:
                    user = User.objects.create_user(username=username, password=pass1,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    print('user created')
                    return redirect('MyApp:login')

            else:
                messages.info(request,'Password does not match')
                return redirect('MyApp:register')

        else:
            messages.info(request,"Invalid crediantials")
            return redirect('MyApp:register')
            
    else:
        return render(request,"register.html") 

def logout(request):
    auth.logout(request)
    return redirect("/")
def dash(request):
    return render(request,"dash.html")
@login_required(login_url="/login/")
def create_resume(request):
    current_url = request.resolver_match.url_name
    current_url+=".html"
    print(current_url)
    if request.method=="POST":
        username=request.user.username 
        if request.POST.get("fname",""):

            obj,Resume_info = Resume.objects.get_or_create(username=username)
            obj.name =request.POST.get("fname","")+" " +request.POST.get("lname","")
            obj.cv_img=request.POST.get("myFile")
            obj.email=request.POST.get("email")
            obj.phone=request.POST.get("phone")
            address=request.POST.get("address")+" " +request.POST.get("address2")
            if request.POST["city"] or request.POST["state"]:
                address+=", " +request.POST.get("city")+" " +request.POST.get("state","")
            obj.address=address    
            obj.degree=request.POST.get("degree","")
            obj.intermediate=request.POST.get("inter","")
            obj.highSchool=request.POST.get("highschool","")
            obj.about_you=request.POST.get("about_you","")
            obj.experience=request.POST.get("experience","")
            obj.skills=request.POST.get("skills","")
            # name=full_name,phone=phone,email=email,address=address,degree=degree,inter=intermediate,highschool=highSchool,about_you=about_you,skills=skills,experience=experience,cv_img=cv_img)
            
            obj.save()
            # generate resume
            try:
                resume_info = Resume.objects.all()
                for resume_info in resume_info:
                    context={"resume_info":resume_info}
                return render(request,current_url,context)
            except:
                return render(request,current_url)
            # return redirect("MyApp:template")
            # messages.info(request, 'Resume Info Added Successfully. Download Resume Now')
        else:
            messages.info(request,"Invalid Details")
            return redirect("MyApp:create_resume")

    else:
        return render(request,"create_resume.html")

    #     try:
    #         resume = client.query(q.get(q.match(q.index("resume_index"), username)))

    #         quiz = client.query(q.update(q.ref(q.collection("Resume_Info"),resume["ref"].id()), {
    #             "data": {
    #                 "user":username,
    #                 "full_name": full_name,
    #                 "address": address,
    #                 "phone": phone,
    #                 "email":email,
    #                 "about_you":about_you,
    #                 "Graduation": Degree,
    #                 "Intermediate": Intermediate,
    #                 "HighSchool": HighSchool,
    #                 "skills":skills,
    #                 "Experience":Experience,
    #             }
    #         }))
    #         messages.add_message(request, messages.INFO, 'Resume Info Edited Successfully. Download Resume Now')
    #         return redirect("MyApp:resume")
    #     except:
    #         quiz = client.query(q.create(q.collection("Resume_Info"), {
    #             "data": {
    #                 "user":username,
    #                 "full_name": full_name,
    #                 "address": address,
    #                 "phone": phone,
    #                 "email":email,
    #                 "about_you":about_you,
    #                 "Graduation": Degree,
    #                 "Intermediate": Intermediate,
    #                 "HighSchool": HighSchool,
    #                 "career":career,
    #                 "Experience":Experience,
    #                 "job_1__start":job_1__start,
    #                 "job_1__end":job_1__end,
    #                 "job_1__details":job_1__details,
    #                 "job_2__start":job_2__start,
    #                 "job_2__end":job_2__end,
    #                 "job_2__details":job_2__details,
    #             }
    #         }))
    #         messages.add_message(request, messages.INFO, 'Resume Info Saved Successfully. Download Resume Now')
    #         return redirect("MyApp:resume")
    # else:
    #     try:
    #         resume_info = client.query(q.get(q.match(q.index("resume_index"), request.session["user"]["username"])))["data"]
    #         context={"resume_info":resume_info}
    #         return render(request,"create-resume.html",context)
    #     except:
    #         return render(request,"create-resume.html")


# def template(request):

#     return render(request,"template.html")
    

# def resume(request):
#     current_url = request.resolver_match.url_name
#     current_url+=".html"
#     # print(current_url)
#     # username=request.user.username

#     try:
#         resume_info = Resume.objects.all()
#         for resume_info in resume_info:
#             context={"resume_info":resume_info}
#         print(context)
        
#         return render(request,current_url,context)
#     except:
#         return render(request,current_url)

