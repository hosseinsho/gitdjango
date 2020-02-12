from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
class person:
    def __init__(self,firstname,lastname,gmailname,password,repassword):
        self.firstname=firstname
        self.lastname=lastname
        self.gmailname=gmailname
        self.password=password
        self.repassword=repassword

    def get_name(self):
        return "%s %s %s" %(self.firstname, self.lastname,self.gmailname)
    def __str__(self):
        return "%s %s" %(self.firstname, self.lastname)

ali=person("ali","molavi","asali@gmail.com","123456","123456")
reza=person("reza","khaled","rezi@gmail.com","0025","0025")

users = [ali,reza]


'''baraye check kardn dorosti ba try ham mishod used in signup first if'''
def check_value(data):
    if len(data['first']) < 3:
        eroreshow="your first name is less than 3 character"
        return False
    if(data['psw']!=data['psw-repeat']):
        eroreshow="YOUR PASSWORD NOT SAME"
        return False    
    return True


def signup(request):
    if 'first' in request.GET:
        if check_value(request.GET) == True:
            p = person(request.GET['first'],request.GET['last']
            ,request.GET['email'],request.GET['psw'],request.GET['psw-repeat']
            )
            users.append(p)

            #User.objects.create(username=(request.GET['first'])

        else:
            #modelle eroreshow mishe ba rendder o if zad neshon dad to html ha
            return HttpResponse("""
            <html><head>
            <title>FAILED</title></head>
            <a href='http://127.0.0.1:8000/users/signup'>erore</a></html>"""
            )

    return render(request,'signup.html',
    {
    'users':users
    }
    )


def adduser(request):
    if(request.GET['psw']==request.GET['psw-repeat']):
            p = person(request.GET['first'],request.GET['last']
            ,request.GET['email'],request.GET['psw'],request.GET['psw-repeat']
            )
            users.append(p)
            return HttpResponse("this is Ok")
    else:
        return HttpResponse("""
        <html><head>
        <title>FAILED</title></head>
        <body>
        <a href='http://127.0.0.1:8000/users/signup'>try again</a></html>"""
        )

def login(request):
    return render(request,'login.html')
    
def homepage(request):
    return render(request,'index2.html')
