from django.shortcuts import render,  redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import *
from Webcashier.models import *
from .forms import *
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
import joblib
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from Webcashier.backEnd import FaceRecognition
from django.contrib import messages

facerecognition = FaceRecognition()


# Create your views here.

def Homepage(request):
    return render(request,'Webcashier/Home.html')

def logout(req):
    authlogout(req)
    return redirect('/')

@csrf_exempt
def loginpage(request):
    print(request)
    if request.method == 'POST':
        print("request.POST")
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        print('USER =',user)
        if user is not None:
            print(user)
            authlogin(request, user)
            return redirect('/Home/')
    else :
        print('เขายังไม่ได้กรอก login/password (ครั้งแรกที่เข้าหน้านี้)')
    return render(request, 'Webcashier/login.html')

def Incustumerpage(request,face_id = 0 ):
    print(face_id)
    data = {
        'user': Incustumer.objects.get(pk= face_id)
    }

    return render(request,'Webcashier/Incustumer.html',data)    

def Editcustumerpage(request):
    return render(request,'Webcashier/Editcustumer.html',)      

def Orderhotpage(request):
    order = Product.objects.all()
    context = {'order': order}
    
    return render(request,'Webcashier/Orderhot.html',context) 

def Orderblendedpage(request):
    order = Product.objects.all()
    context = {'order': order}
    return render(request,'Webcashier/Orderblended.html',context)  

def Ordercoldpage(request):
   order = Product.objects.all()
   context = {'order': order}
   return render(request,'Webcashier/Ordercold.html',context)        

def recommendpage(request):
    return render(request,'Webcashier/recommend.html',)            

def Basepage(request):
    return render(request, 'Webcashier/base.html',)

def registercus(request):
    if request.POST:
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Successfully Registerd!')
            addFace(request.POST['face_id'])
            return redirect('/Home/')
        else:
            messages.error(request, "Account Register Failed!")

    form = RegisterForm()
   
    context = {
        'title' : 'Register Form',
        'form' : form,
    }

    return render(request, 'Webcashier/register.html', context  )
    
def customers(request):
    return render(request, 'Webcashier/customers.html', { 'customers': Customer.objects.all() })

def customer_register(request):
    '''ลงทะเบียนลูกค้า'''
    if request.method == "POST":
        form = CustomerForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'ลงทะเบียนสำเร็จ')
            #return redirect('/customer_register/')
        else:
            messages.error(request, 'มีข้อผิดพลาดในการลงทะเบียน')

    else:
        form = CustomerForm()
   
    context = {
        'title' : 'Customer Form',
        'form' : form,
        'customers' : Customer.objects.all(),
    }

    return render(request, 'Webcashier/customer_register.html', context  )

# def recommend(req):
#     if req.user.is_anonymous:
#         return redirect('/register')
#     else:
#         Incustumer = Incustumer.objects.get(username=req.user.username)
#         random_For = joblib.load('static/model/')
#     favc = None
#     try:
#         favc = FavoriteCloth.objects.filter(member=member).first()
#     except: pass
#     if favc:
#         user_cloth = knn.get_neighbors(favc.cloth.cid-1, 9)
#         recommend_items = []
#         for u in user_cloth: 
#             item = Cloth.objects.get(pk=u+1)
#             print(item)
#             recommend_items.append( item )
#     else:
#         from django.db.models import Sum
#         fc = FavoriteCloth.objects.values('cloth').annotate(star=Sum('star')).order_by('-star')
#         recommend_items = []
#         for u in fc[:9]: 
#             item = Cloth.objects.get(pk=u['cloth'])
#             print(item)
#             recommend_items.append( item )
#     return render(req, 'lookinggreat/recommend.html',{
#     'member': member,
#     'has_store': has_store(req),
#     'recommends': recommend_items
# })

def addFace(face_id):
    face_id = face_id
    facerecognition.faceDetect(face_id)
    facerecognition.trainFace()
    return redirect('/Home/')

def loginIncus(request):
    face_id = facerecognition.recognizeFace()
    print(face_id)
    return redirect('/Webcashier/Incustumer/'+ str(face_id))

