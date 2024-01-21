from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import MemberTable, ContactTable, YogaTable, DiseaseTable
from django.template import loader
from django.contrib import messages
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.conf import settings

# def sendEmail(subject, body):
#     import smtplib
#     import ssl
#     from email.message import EmailMessage
#     sender = ''
#     receiver = ['kirtirajput63969@gmail.com']
#     password = ''

#     obj = EmailMessage()
#     obj['From'] = sender
#     obj['To'] = receiver
#     obj['Subject'] = subject
#     obj.set_content(body)

#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
#         server.login(sender, password)
#         server.sendmail(sender, receiver, obj.as_string())


def checkBMI(request):
    return render(request, 'check-BMI.html', {'title':"Check Your BMI", 'logo':"My Mat Space"})

def resultBMI(request):
    # template = loader.get_template('result-BMI.html')
    if request.method == 'POST':
        name = request.POST['name']
        weight = request.POST['weight']
        height = request.POST['height']

        result = eval(weight)/(eval(height)/100)**2
        string_result = ''
        num_result = 0
        if result < 18.5:
            string_result = 'Underweight'
            num_result = 18.5 - result
        elif result >= 18.5 and result < 25:
            string_result = 'Normal'
        elif result >= 25 and result < 30:
            string_result = 'Overweight'
            num_result = result - 25
        elif result >= 30 and result < 35:
            string_result = 'Obese'
            num_result = result - 25
        elif result >= 35:
            string_result = 'Extremely Obese'
            num_result = result - 25
        num_result = "%0.2f"%(num_result)
        context = {'title':"BMI Result",
                    'logo':"My Mat Space",
                    'result':"%.2f"%(result),
                    'name':name,
                    'string_result':string_result,
                    'correct_weight':num_result,
                    'weight':weight,
                    'height':height
                    }
        # return HttpResponse(template.render(context, request))
        return render(request, 'result-BMI.html', context=context)
    return render(request, 'result-BMI.html')

def yogaPoses(request):
    template = loader.get_template('yoga_poses.html')
    context = {'title':"Different Yoga Poses", 'logo':"My Mat Space"}
    return HttpResponse(template.render(context, request))

def yogaForWomen(request):
    template = loader.get_template('yoga-for-women.html')
    context = {'title':"Yoga for Women", 'logo':"My Mat Space"}
    return HttpResponse(template.render(context, request))

def yogaForMen(request):
    template = loader.get_template('yoga-for-men.html')
    context = {'title':"Yoga for Men", 'logo':"My Mat Space"}
    return HttpResponse(template.render(context, request))

def yogaForDisease(request, bimari):
    bimari_code = bimari[:5]
    yogas = YogaTable.objects.filter(disease_code=bimari_code).values()

    for yoga in yogas:
        yoga['how_to_do'] = list(map(str.strip, yoga['how_to_do'].split('.')))
        yoga['benefits'] = list(map(str.strip, yoga['benefits'].split('.')))
        yoga['contraindications'] = list(map(str.strip, yoga['contraindications'].split('.')))

    context = {'title':"Recommended Yogas", 'logo':"My Mat Space", 'yogass':yogas, 'bimari':bimari}
    return render(request, 'yoga-for-disease.html', context=context)

def profile(request):
    if request.session.get('email'):
        user = MemberTable.objects.get(email=request.session.get('email'))
        print(user.disease)
        if user.disease is not None:
            disease = DiseaseTable.objects.filter(d_code=user.disease[:5]).values()
        else:
            disease = None
        print(disease)
        my_query = ContactTable.objects.filter(email=user.email).values()
        context = {'title':"My Profile", 'logo':"My Mat Space", 'user':user, 'my_query':my_query, 'disease':disease}
        return render(request, 'profile.html', context=context)
    else:
        messages.info(request, "Please Sign-In First!")
        return redirect('/login')

def search(request):
    query = request.GET['search']
    if query == '':
        return render(request, 'search.html', {'query':query, 'title':'Search Results', 'logo':'My Mat Space'})
    d = DiseaseTable.objects.filter(d_name__icontains=query)
    yogas = YogaTable.objects.filter(name__icontains=query).values()
    for yoga in yogas:
        yoga['how_to_do'] = list(map(str.strip, yoga['how_to_do'].split('.')))
        yoga['benefits'] = list(map(str.strip, yoga['benefits'].split('.')))
        yoga['contraindications'] = list(map(str.strip, yoga['contraindications'].split('.')))
    return render(request, 'search.html', {'diseases':d, 'yogas':yogas, 'query':query, 'title':'Search Results', 'logo':'My-Mat-Space'})

def register(request):
    if request.method=='POST':
        fullname = request.POST['fullname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        email = request.POST['email']
        mobile = request.POST['mobile']
        age = request.POST['age']
        gender = request.POST['gender']
        disease = request.POST['disease']

        if pass1 != pass2:
            messages.info(request, "Password is not Matching")
            return redirect('/register')
        if len(mobile) != 10:
            messages.info(request, "Mobile Number must be 10 digits")
            return redirect('/register')
        try:
            data = MemberTable.objects.filter(email=email).values()
            if data:
                messages.warning(request, "Email ID Already Exists")
                return redirect('/register')
        except Exception as identifier:
            pass
        try:
            data = MemberTable.objects.filter(mobile=mobile).values()
            if data:
                messages.warning(request, "Mobile Number Already Exists")
                return redirect('/register')
        except Exception as identifier:
            pass

        member = MemberTable(fullname=fullname, pass1=pass1, pass2=pass2, email=email, mobile=mobile, age=age, gender=gender, disease=disease)
        member.save()




        # Send Email to Admins
        subject = 'New Account is Created | My Mat Space'
        email_message = f"{fullname} has been created his/her account at My Mat Space. Here are some information about the user.\n\nName : {fullname}\nEmail ID : {email}\nMobile : {mobile}\nAge : {age}\nGender : {gender}\nDisease : {disease}"
        # recipient_list = ["saraju.work@gmail.com", "kirtirajput63969@gmail.com", 'jayadmalik525@gmail.com', 'vanshikavce19@gmail.com']
        recipient_list =[]
        email_from = settings.EMAIL_HOST_USER
        send_mail( subject, email_message, email_from, recipient_list )

        # Send email to User
        subject = 'Thank You! Your Account has been Created | My Mat Space'
        email_message = f"Dear {fullname}!\n\nThank you for connecting with us. You can do yoga according to your disease/problems."
        recipient_list = [email]
        send_mail( subject, email_message, email_from, recipient_list)

        request.session['fullname'] = fullname
        request.session['email'] = email
        messages.success(request, "User is Created. Please Login")

        return redirect('/login')
    diseases = DiseaseTable.objects.all().values()
    return render(request, 'yoga-register.html', {'diseases':diseases})

def handleLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = MemberTable.objects.filter(email=email, pass1=password).values()
        try:
            if not user:
                messages.error(request, "User Doesn't Exists. Please Create your account")
                return redirect('/login')
        except Exception as identifier:
            pass
        try:
            if user:
                request.session['email'] = email
                return redirect('/')
        except Exception as identifier:
            pass
        # context = {'title':'Home Page', 'logo':'My Mat Space' }
        # template = loader.get_template('dashboard.html')
        # return HttpResponse(template.render(context, request))
    return render(request, 'yoga-signin.html')

def handleLogout(request):
    logout(request)
    messages.success(request, 'Logout Success')
    return redirect('/login')

def help(request):
    context = {'title':"Help Desk", 'logo':"My Mat Space"}
    return render(request, 'help.html', context=context) 

def contact(request):
    try:
        user = None
        if request.session.get('email'):
            user = MemberTable.objects.get(email=request.session.get('email'))
            if request.method=='POST':
                sub =  request.POST.get('subject')
                message = request.POST.get('message')
                contact = ContactTable(name=user.fullname, email=user.email, subject=sub, message=message)
                contact.save()

                # Send email to Admins
                subject = 'Attention Please! Query is Sent at <My-Mat-Space>'
                email_message = f"{user[0]['fullname']} has a query regarding \"{sub}\". Please check your admin panel, if needed, and provide the solution to the user.\nHave a good day! 😊😍"
                recipient_list = ["kirtirajput63969@gmail.com"']
                email_from = settings.EMAIL_HOST_USER
                send_mail( subject, email_message, email_from, recipient_list )

                messages.warning(request, "Thank You! Your responce has been submitted")
                return redirect('/home/contact')
        else:
            messages.error(request, "Please Login First!")
            return redirect("/login")
        context = {'title':"Contact Us", 'logo':"My Mat Space"}
        return render(request, 'contact.html', context=context)
    except:
        messages.info(request, "Please Sign-In First!")
        return redirect('/login')

def about(request):
    context = {'title':"About Us", 'logo':"My Mat Space"}
    return render(request, 'about.html', context=context)

def home(request):
    problems = DiseaseTable.objects.all().values()
    context = {'title':"Home", 'logo':"My Mat Space", 'problems':problems}
    return render(request, 'dashboard.html', context=context)


def updateRecord(request, num):
    data = MemberTable.objects.get(id=num)
    if data:
        if request.method=='POST':
            fullname = request.POST['fullname']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            # email = request.POST['email']
            mobile = request.POST['mobile']
            age = request.POST['age']
            gender = request.POST['gender']
            disease = request.POST['disease']
            if disease == 'None':
                disease = None
            if pass1 != pass2:
                messages.info(request, "Password is not Matching")
                return redirect(f'/update/{data.id}')
            if len(mobile) != 10:
                messages.info(request, "Mobile Number must be 10 digits")
                return redirect(f'/update/{data.id}')
            
            data.fullname = fullname
            data.pass1 = pass1
            data.pass2 = pass2
            # data.email = email
            data.mobile = mobile
            data.age = age
            data.gender = gender
            data.disease = disease
            data.save()
            return HttpResponseRedirect('/home/profile')
        diseases = DiseaseTable.objects.all().values()
        return render(request, 'update.html',{'data':data, 'title':'Update Record', 'logo':'My-Mat-Space', 'diseases':diseases})
    return render(request, 'update.html')
