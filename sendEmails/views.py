from django.shortcuts import render
from django.core.mail import EmailMessage, send_mail
from GFG import settings
from django.template.loader import render_to_string

# Create your views here.

def home(request):
    return render(request, "sendEmails/index.html")

def staticText(request):
    username = "Anubhav Madhav"
    toEmail1 = "anubhavmadhav20@gmail.com"
    toEmail2 = "201851024@iiitvadodara.ac.in"
    subject = "staticText Email"
    message = "Hello " + username + "!! \n" + "Welcome to GFG!! \nThank you for visiting our website.\n\nThanking You\nAnubhav Madhav"        
    from_email = settings.EMAIL_HOST_USER
    to_list = [toEmail1, toEmail2]
    send_mail(subject, message, from_email, to_list, fail_silently=True)
    
    return render(request, "sendEmails/emailSent.html")

def dynamicTextHTML(request):
    
    first_name = "Digant"
    marks = 335
    college_name = "Oxford University"
    toEmail1 = "anubhavmadhav20@gmail.com"
    toEmail2 = "201851024@iiitvadodara.ac.in"
    
    email_subject = "dynamicTextHTML Email"
    message = render_to_string('sendEmails/dynamic_text.html',{
        
        'name': first_name,
        'marks': marks,
        'university': college_name
    })
    email = EmailMessage(email_subject, message, settings.EMAIL_HOST_USER, [toEmail1, toEmail2])
    email.fail_silently = True
    email.send()
    
    return render(request, "sendEmails/emailSent.html")

def beautifulHTMLEmail(request):
    
    first_name = "Deep"
    marks = 335
    college_name = "Harvard University"
    toEmail1 = "anubhavmadhav20@gmail.com"
    toEmail2 = "201851024@iiitvadodara.ac.in"
    
    email_subject = "beautifulTextHTML Email"
    message = render_to_string('sendEmails/beautiful_text.html',{
        
        'name': first_name,
        'marks': marks,
        'university': college_name
    })
    
    email = EmailMessage(email_subject, message, settings.EMAIL_HOST_USER, [toEmail1, toEmail2])
    email.fail_silently = True
    email.content_subtype = "html"
    email.send()
    return render(request, "sendEmails/emailSent.html")


def attachmentEmail(request):
    
    name = "Anubhav Madhav"
    company_name = "Google"
    role = "Software Engineer"
    toEmail1 = "anubhavmadhav20@gmail.com"
    toEmail2 = "201851024@iiitvadodara.ac.in"
    
    email_subject = "You are placed!"
    message = render_to_string('sendEmails/attachment_email.html',{
        
        'name': name,
        'company_name': company_name,
        'role': role
    })
    
    email = EmailMessage(email_subject, message, settings.EMAIL_HOST_USER, [toEmail1, toEmail2])
    email.attach_file(str(settings.BASE_DIR) + "\\OfferLetter_Google.pdf")
    email.fail_silently = True
    email.content_subtype = "html"
    email.send()
    return render(request, "sendEmails/emailSent.html")