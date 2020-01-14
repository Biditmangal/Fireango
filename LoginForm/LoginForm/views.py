from django.shortcuts import render
from firebase import firebase
from django.contrib import auth
from django.urls import reverse

Config = {
    'apiKey': "AIzaSyCwt1tJItYRoKDo5omL6dVNF0gqEWhncPU",
    'authDomain': "loginformdjango.firebaseapp.com",
    'databaseURL': "https://loginformdjango.firebaseio.com",
    'projectId': "loginformdjango",
    'storageBucket': "loginformdjango.appspot.com",
    'messagingSenderId': "798266349598",
    'appId': "1:798266349598:web:c4eed81998add0f9b8b60f",
    'measurementId': "G-7218SJKRHX"
}

firebase = Firebase(Config)
auth = firebase.auth()
databse = firebase.database()


def login(request):
    return render(request, template_name="login.html")


def postlogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user = auth.sign_in_with_username_and_password(username, password)
    except:
        message = "Oops! Wrong Credentials. Try Again!"
        return render(request, "login.html", {'message': message})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    try:
        idtoken = request.session['uid']
        a = authi.get_account_info(idtoken)
        a = a['users']
        a= a[0]
        a = a['localId']
        print("info"+a)
        name = databse.child('users').child(a).child('details').child('name').get().val()
        return render(request, "homepage.html", {'name': name})
    except KeyError:
        message = "Please Comeback by loging again!"
        return render(request, "homepage.html", {'message': message})

def logoutfunc(request):
    auth.logout(request)
    return render(request,'login.html')


def register(request):
    registered=False
    if (request.method == 'POST'):
        if user_form.
    return render(request, 'register.html')


def postsignup(request):
    name = request.POST.get('name')
    password = request.POST.get('password')
    try:
        user = authi.create_user_with_name_and_password(name, password)
    except:
        message = "Wasn't able to Register you. Please Try again!"
        return render(request, 'register.html', {"message": message})
    uid = user['localId']
    data = {"name": name, "status": "1"}
    databse.child("users").child(uid).child("details").set(data)
    
    return render(request, "login.html")