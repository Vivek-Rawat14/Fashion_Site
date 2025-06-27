from django.shortcuts import redirect, get_object_or_404
from django.urls import path
from django.shortcuts import render,redirect
from . import models
import json
import itertools
from .models import clothes,users

def homepage(req):
    if 'user' not in req.session:
        return redirect('/login') 
    cd = list(clothes.objects.filter(clothescat='shirtm').values())
    cc = list(clothes.objects.filter(clothescat='printtshirtw').values())
    vd = list(clothes.objects.filter(clothescat='rings').values())
    d = list(clothes.objects.filter(clothescat='bags').values())

    return render(req, 'index.html', context={
        'data': cd,
        'wtsh': cc,
        'watch': vd,
        'bags': d
    })
def mencollection(req):
    return render(req, 'mencollection.html')


def womencollection(req):
    return render(req, 'womencollection.html')


def accessories(req):
    return render(req, 'accessoires.html')

def tshirt(req):
    db = clothes.objects.filter(clothescat='printtshirtm').values()
    cd = list(db)
    return render(req, 'tshirt.html',context={'data':cd})

def shirtm(req):
    db = clothes.objects.filter(clothescat='shirtm').values()
    cd = list(db)
    return render(req, 'shirtm.html',context={'data':cd})


def full(req):
    db = clothes.objects.filter(clothescat='fullm').values()
    cd = list(db)
    return render(req, 'full.html',context={'data':cd})

def jeansm(req):
    db = clothes.objects.filter(clothescat='jeansm').values()
    cd = list(db)
    return render(req, 'jeansm.html',context={'data':cd})

def cargom(req):
    db = clothes.objects.filter(clothescat='cargom').values()
    cd = list(db)
    return render(req, 'cargom.html',context={'data':cd})

def baggym(req):
    db = clothes.objects.filter(clothescat='baggym').values()
    cd = list(db)
    return render(req, 'baggym.html',context={'data':cd})

def printtshirtw(req):
    db = clothes.objects.filter(clothescat='printtshirtw').values()
    cd = list(db)
    return render(req, 'printtshirtw.html',context={'data':cd})

def hoodies(req):
    db = clothes.objects.filter(clothescat='hoodies').values()
    cd = list(db)
    return render(req, 'hoodies.html',context={'data':cd})

def shirtw(req):
    db = clothes.objects.filter(clothescat='shirtw').values()
    cd = list(db)
    return render(req, 'shirtw.html',context={'data':cd})

def kurta(req):
    db = clothes.objects.filter(clothescat='kurta').values()
    cd = list(db)
    return render(req, 'kurta.html',context={'data':cd})

def cargow(req):
    db = clothes.objects.filter(clothescat='cargow').values()
    cd = list(db)
    return render(req, 'cargow.html',context={'data':cd})

def sareew(req):
    db = clothes.objects.filter(clothescat='sareesw').values()
    cd = list(db)
    return render(req, 'sareew.html', context={'data': cd})

def braclets(req):
    db = clothes.objects.filter(clothescat='braclets').values()
    cd = list(db)
    return render(req, 'braclets.html',context={'data':cd})

def necklace(req):
    db = clothes.objects.filter(clothescat='necklace').values()
    cd = list(db)
    return render(req, 'necklace.html', context={'data': cd})

def caps(req):
    db = clothes.objects.filter(clothescat='caps').values()
    cd = list(db)
    return render(req, 'caps.html', context={'data': cd})

def rings(req):
    db = clothes.objects.filter(clothescat='rings').values()
    cd = list(db)
    return render(req, 'rings.html', context={'data': cd})

def sunglasses(req):
    db = clothes.objects.filter(clothescat='sunglasses').values()
    cd = list(db)
    return render(req, 'sunglasses.html', context={'data': cd})

def bags(req):
    db = clothes.objects.filter(clothescat='bags').values()
    cd = list(db)
    return render(req, 'bags.html', context={'data': cd})

def watchm(req):
    db = clothes.objects.filter(clothescat='watchm').values()
    cd = list(db)
    return render(req, 'watchm.html', context={'data': cd})

def watchw(req):
    db = clothes.objects.filter(clothescat='watchw').values()
    cd = list(db)
    return render(req, 'watchw.html', context={'data': cd})

def shoes(req):
    db = clothes.objects.filter(clothescat='shoes').values()
    cd = list(db)
    return render(req, 'shoes.html', context={'data': cd})

def shoesw(req):
    db = clothes.objects.filter(clothescat='shoesw').values()
    cd = list(db)
    return render(req, 'shoesw.html', context={'data': cd})

def shoescoll(req):
    return render(req,'shoescoll.html')

def watchcoll(req):
    return render(req,'watchcoll.html')

def productshow(req,Id):
    db = clothes.objects.get(id=Id)
    sizes = db.clothsize.strip("[]").split(",")
    print(type(sizes),sizes)
    return render(req,'productshow.html',context={'data':db,'sizes':sizes})

def login(req):
    req.session.set_test_cookie()

    if req.method == 'POST':
        phonenumber = req.POST.get('phone')
        passwordl = req.POST.get('password')
        try:
            s = users.objects.get(phone=phonenumber)
            if s.password == passwordl:
                req.session['user'] = s.username  # Store username in session
                return redirect('/')
            else:
                return render(req, 'login.html', context={"error": "Invalid password"})
        except users.DoesNotExist:
            return render(req, 'login.html', context={"error": "User not found"})
        except Exception:
            return render(req, 'login.html', context={"error": "Something went wrong, try again"})

    return render(req, 'login.html')

def signup(req):
    if req.method=='POST':
        name = req.POST['name']
        email = req.POST['email']
        password = req.POST['password']
        repassword = req.POST['re_password']
        state = req.POST['state']
        city = req.POST['city']
        pincode = req.POST['pincode']
        address = req.POST['address']
        phone  = req.POST['phone']

        users.objects.create(username = name,password=password,email=email,phone =phone,address= address,city=city,pincode=pincode,state=state,repassword=repassword  )
        return redirect('/login')
    
    return render(req,'signup.html')

def userst(req):
    if 'user' not in req.session:
        return redirect('/login')

    username = req.session['user']
    try:
        user_data = users.objects.filter(username=username).values()
        return render(req, 'users.html', context={"userde": user_data})
    except users.DoesNotExist:
        return render(req, 'users.html', context={"error": "User not found"})

def logout(req):
    return redirect('/login')

def carts(req):
    return render(req,'carts.html')


def search(req, item):
    db = clothes.objects.all().values()
    filterdb = []
    for i in db:
        if i['clothname'].lower().find(item) != -1:
            filterdb.append(i)
    return render(req, 'search.html', context={"data": filterdb})


    
def addlikeitem(req,Id):
    username = req.session['user']
    users = models.users.objects.get(username=username)
    likeitems = json.loads(users.likes)
    likeitems.append(Id)
    users.likes=likeitems
    users.save()
    return redirect('/like') 


def addremoveitem(request, Id):
    if request.method == 'POST':
        username = request.session.get('user')
        if not username:
            return redirect('/login')

        user = models.users.objects.get(username=username)

        likeitems = json.loads(user.likes) if user.likes else []

        try:
            likeitems.remove(Id)
        except ValueError:
            pass  

        user.likes = json.dumps(likeitems)
        user.save()

    return redirect('/like')


def like(req):
    if 'user' not in req.session:
        return redirect('/homepage')
    
    username = req.session['user']
    try:
        user = users.objects.get(username=username)

        try:
            liked_ids = json.loads(user.likes)  # convert string to list
        except json.JSONDecodeError:
            liked_ids = []

        liked_items = clothes.objects.filter(id__in=liked_ids)
        return render(req, 'like.html', context={'data': liked_items})
    except users.DoesNotExist:
        return redirect('/login')
    




def addbuyitem(req, Id):
    if 'user' not in req.session:
        return redirect('/login')

    size = req.POST.get('size') 
    qty = req.POST.get('productqty') 
    print("get",size,qty)

    username = req.session['user']
    user = models.users.objects.get(username=username)

    try:
        cartitems = json.loads(user.cart)
    except (TypeError, json.JSONDecodeError):
        cartitems = []

    new_cart = []
    for item in cartitems:
        if isinstance(item, int):
           
            new_cart.append({"id": item, "size": "Default", "qty": 1})
        else:
            new_cart.append(item)

    
    found = False
    for item in new_cart:
        if item["id"] == Id and item["size"] == size:
            item["qty"] = str(int(item["qty"]) + int(qty))
            found = True
            break

    if not found:
        new_cart.append({
            "id": Id,
            "size": size,
            "qty": qty
        })

    user.cart = json.dumps(new_cart)
    user.save()
    return redirect('/carts')


def carts(req):


    if 'user' not in req.session:
        return redirect('/homepage')

    username = req.session['user']
    try:
        user = models.users.objects.get(username=username)
        try:
            cart_data = json.loads(user.cart)
        except json.JSONDecodeError:
            cart_data = []

        cart_items = []
        for item in cart_data:
            try:
                product = models.clothes.objects.get(id=item["id"])
                cart_items.append({
                    "product": product,
                    "size": item.get("size", ""),
                    "qty": item.get("qty", 1)
                })
            except models.clothes.DoesNotExist:
                continue

        return render(req, 'carts.html', context={'data': cart_items})
    except models.users.DoesNotExist:
        return redirect('/login')
    


def about(req):
    return render(req,'about.html')

def privacy(req):
    return render(req,'privacy.html')

def help(req):
    return render(req,'help.html')

def terms(req):
    return render(req,'term.html')



def clearcart(request):
    username = request.session.get('user')
    if not username:
        return redirect('/login')

    user = models.users.objects.get(username=username)
    user.cart = json.dumps([])  # empty list
    user.save()
    return redirect('/carts')