# from asyncio.windows_events import NULL
from django.shortcuts import render
from . models import *
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse

#index...

def index(request):
    return render(request,'index.html')

def groundfloor(request):
    shops=shopkeeper.objects.filter(floor=0)
    return render(request,'groundfloor.html',{"shops":shops})

def firstfloor(request):
    shops = shopkeeper.objects.filter(floor=1)
    return render(request, 'groundfloor.html', {"shops": shops})
def secondfloor(request):
    shops = shopkeeper.objects.filter(floor=2)
    return render(request, 'groundfloor.html', {"shops": shops})

def shop_list(request):
    shops = shopkeeper.objects.all()
    return render(request, 'shop_list.html', {'shops': shops})

def rate_shop(request, shop_id):
    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        shop = shopkeeper.objects.get(id=shop_id)
        data=Ratings.objects.filter(shopkeepers=shop)
        if data:
            d=data[0]
            old=d.rating
            new=float(rating_value)+old
            new1=new/5
            rating = Ratings(shopkeepers=shop, rating=new1)
        else:
            rating = Ratings(shopkeepers=shop, rating=rating_value)
        rating.save()
        return redirect('shop_detail', shop_id=shop_id)
    return render(request, 'rate_shop.html')

def shop_detail(request, shop_id):
    shop = shopkeeper.objects.get(id=shop_id)
    ratings = Ratings.objects.filter(shopkeepers=shop)
    return render(request, 'shop_detail.html', {'shop': shop, 'ratings': ratings})

def rated_shops(request):
    rated_shops = shopkeeper.objects.filter(ratings__isnull=False).distinct()
    return render(request, 'rated_shops.html', {'rated_shops': rated_shops})

def Rating(request):
    shops = shopkeeper.objects.all()
    return render(request, 'rating.html', {"shops": shops})
#categorylist.............

def Product(request,pk):
    # Retrieve the product using the received pk from the URL
    products = Products.objects.filter(shopkeeper_id=pk)
    # product={*[setattr(prod, 'new_field', 'q') for prod in products]}

    return render(request,'products.html',{"product":products})


def fashion(request):
    product = Products.objects.filter(product_type__name='fashion')
    return render(request, 'fashion.html',{"product":product})

def electronic(request):
    product = Products.objects.filter(product_type__name='electronic')
    return render(request,'electronic.html',{"product":product})

def food(request):
    product = Products.objects.filter(product_type__name='food')
    return render(request,'food.html',{"product":product})

def cosmetics(request):
    product = Products.objects.filter(product_type__name='cosmetics')
    return render(request,'cosmetics.html',{"product":product})

def jewellery(request):
    product = Products.objects.filter(product_type__name='jewellery')
    return render(request,'jewellery.html',{"product":product})

def funtora(request):
    product = Products.objects.filter(product_type__name='funtora')
    return render(request,'funtora.html',{"product":product})

def theater(request):
    product = Products.objects.filter(product_type__name='theater')
    return render(request,'theater.html',{"product":product})




def feedback(request):
    if request.method=="POST":
        message=request.POST.get("Message")
        feed(message=message).save()
    return render(request,'index.html')
    # else:
    #  return render(request,'feedback.html')


#Shopkeeper module start
#............................

#mainpage....


def index1(request):
    return render(request,'index1.html')



def register(request):
    if request.method == 'POST':
        shopowner = request.POST.get("fullName")
        shopname = request.POST.get("username")
        floor = request.POST.get("floorNumber")
        email = request.POST.get("email")
        password = request.POST.get("Password")

        if User.objects.filter(username=shopname).exists():
            message = "Username already exists. Please choose a different username."
            return render(request, 'register.html', {'message': message})

        if int(floor)>2:
            message = "Please enter floor number 0,1 or 2"
            return render(request, 'register.html', {'message': message})

        user = User.objects.create_user(username=shopname, email=email, password=password)
        user.first_name = shopowner
        user.save()
        Shopkeeper=shopkeeper.objects.create(shopowner_name=shopowner,shop_name=shopname,floor=floor)
        Shopkeeper.user=user
        Shopkeeper.save()
        authenticated_user = authenticate(request, username=shopname, password=password)
        if authenticated_user:
            login(request, authenticated_user)
        # Optionally, you might want to log the user in after registration
        # login(request, user)

        # Redirect to a success page or login page
        return redirect('login')
    return render(request,'register.html')




# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']

#         # Create user without any validation checks
#         user = User.objects.create_user(username=username, email=email, password=password)
#         user.save()

#         return redirect('login')  # Redirect to login page after successful registration

#     return render(request, 'register.html')
#loginpage....

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shophome')  # Redirect to your home page
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('/')

def shophome(request):
    products=Products.objects.filter(shopkeeper__user_id=request.user.id)

    return render(request,'shophome.html',{"products":products})
def viewproducts(request):
    return render(request,'viewproducts.html')

#Product detials......

#cloth detials
#.....................

def clothesdetails(request):
    type=Type.objects.all()


    if request.method=="POST":
        clothname=request.POST.get("pname")
        brand=request.POST.get("bname")
        countryorigin=request.POST.get("country")
        qualityofcloth=request.POST.get("quality")
        materialofcloth=request.POST.get("material")
        colorofcloth=request.POST.get("color")
        priceofcloth=request.POST.get("price")
        descriptionaboutcloth=request.POST.get("description")
        selected_item_id = request.POST.get('selected_item')
        image_file = request.FILES.get('image')  # Get the uploaded image file
        floor=request.POST.get("floor")
        Shopkeeper=shopkeeper.objects.filter(user=request.user).first()
        Products(shopkeeper_id=Shopkeeper.id,product_type_id=selected_item_id,image=image_file,
                 product_name=clothname,brand_name=brand,country=countryorigin,quality=qualityofcloth,
                 material=materialofcloth,color=colorofcloth,price=priceofcloth,
                 description=descriptionaboutcloth).save()
        return redirect('shophome')
    return render(request,'clothesdetails.html',{"type":type})

def delete_product(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    if request.method == 'POST':
        product.delete()
    return redirect('shophome')
  # Redirect to a view displaying the list of products after deletion

def search_results_category(request,pk=None):
    query = pk
    results = []
    if query:
        filtered_products = Products.objects.filter(product_type__name=query)

        # Get the distinct shopkeepers related to the filtered products
        results = shopkeeper.objects.filter(products__in=filtered_products).distinct()
        for prod in results:
            try:
                rating = Ratings.objects.filter(shopkeepers=prod).first().rating
            except:
                rating = 0
            setattr(prod, 'rating', rating)
    return render(request, 'index.html', {'results': results})

def search_results(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = shopkeeper.objects.filter(shop_name__icontains=query)
        for prod in results:
            try:
                rating = Ratings.objects.filter(shopkeepers=prod).first().rating
            except:
                rating = 0
            setattr(prod, 'rating', rating)
    return render(request, 'index.html', {'results': results})
#food detials
#................
#
# def fooddetails(request):
#     if request.method=='POST':
#
#         foodname=request.POST.get("fname")
#         countryoforigin=request.POST.get("ctry")
#         quantityofcloth=request.POST.get("qty")
#         priceoffood=request.POST.get("price")
#         descriptionaboutfood=request.POST.get("desc")
#         food(food_name=foodname,countryfood=countryoforigin,quantityfood=quantityofcloth,pricefood=priceoffood,descriptionfood=descriptionaboutfood).save()
#
#
#     return render(request,'fooddetails.html')
#
# #electronics detials
# #..................
#
#
# def electronicdetails(request):
#
#     if request.method=="POST":
#         productname=request.POST.get("pname")
#         brand=request.POST.get("name")
#         countryoforigin=request.POST.get("count")
#         qualityofproduct=request.POST.get("quali")
#         colorofproduct=request.POST.get("colour")
#         priceofproduct=request.POST.get("pric")
#         descriptionaboutcloth=request.POST.get("descrip")
#         electronic(product_name=productname,brand_name=brand,country=countryoforigin,quality=qualityofproduct,color=colorofproduct,price=priceofproduct,description=descriptionaboutcloth).save()
#     return render(request,'electronicdetails.html')
#     # else:
#     #     return render(request,'index.html')
#
#
# def parlourdetails(request):
#
#         if request.method=="POST":
#          parlourname=request.POST.get("pname")
#          brand=request.POST.get("bname")
#          countryorigin=request.POST.get("country")
#          qualityofcloth=request.POST.get("quality")
#          materialofcloth=request.POST.get("material")
#          colorofcloth=request.POST.get("color")
#          priceofcloth=request.POST.get("price")
#          descriptionaboutcloth=request.POST.get("description")
#          parlour(product_name=parlourname,brand_name=brand,country=countryorigin,quality=qualityofcloth,material=materialofcloth,color=colorofcloth,price=priceofcloth,description=descriptionaboutcloth).save()
#
#         return render(request,'parlourdetails.html')
#
# #funzone detialsss
#
# def funzonedetails(request):
#         gamename=request.POST.get("gname")
#         duration=request.POST.get("duration")
#         price=request.POST.get("price")
#         description=request.POST.get("description")
#         playzone(gamename=gamename,duration=duration,price=price,description=description).save()
#         return render(request,'funzonedetails.html')
#
# #theater detials....
#
# def theaterdetails(request):
#
#         if request.method=="POST":
#          filmname=request.POST.get("filname")
#          show=request.POST.get("wshow")
#          showandtime=request.POST.get("time")
#          duration=request.POST.get("duration")
#          price=request.POST.get("ticket")
#          review=request.POST.get("review")
#          description=request.POST.get("description")
#          theater(filmname=filmname,show=show,showandendtime=showandtime,duration=duration,price=price,review=review,description=description).save()
#
#         return render(request,'theaterdetails.html')
#
# #product list viewproducts......
#
# #clothlist.......
#
# def clothview(request):
#     view=fashion.objects.all()
#     return render(request,'clothlist.html',{'data':view})
#
# #foodlist......
#
# def foodview(request):
#     view=food.objects.all()
#     return render(request,'foodlist.html',{'data':view})
#
#
# #electroniclist........
#
# def electronicview(request):
#     view=food.objects.all()
#     return render(request,'electroniclist.html',{'data':view})
#
# #parlourlist........
#
# def parlourview(request):
#     view=parlour.objects.all()
#     return render(request,'parlourlist.html',{'data':view})
#
# #funzonelist........
#
# def funzoneview(request):
#     view=playzone.objects.all()
#     return render(request,'funzonelist.html',{'data':view})
#
# #theaterlist........
#
# def theaterview(request):
#     view=theater.objects.all()
#     return render(request,'theaterlist.html',{'data':view})
#
# def addproductslink(request):
#     return render(request,'addproductslink.html')








