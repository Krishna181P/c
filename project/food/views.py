from django.shortcuts import render,redirect
from django.views import View
from food.models import Category,FoodMenu,Cart,Order,WishlistModel
from food.models import User
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.core.mail import send_mail,settings
import random


# Create your views here.
class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"register.html")
    def post(self,request,*args,**kwargs):
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        address=request.POST["address"]
        email=request.POST["email"]
        mobile=request.POST["mobile"]
        user_name=request.POST["user_name"]
        password=request.POST["password"]
        confirm_password=request.POST["confirm_password"]
        profile=request.FILES["profile"]

        # User already exist or not

        user=User.objects.filter(username=user_name)
        if user:
            message="User Already Exist"
            return render(request,"register.html",{'userexist':message})
        else:
            if password == confirm_password:
                newuser = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,mobile=mobile,address=address,username=user_name,confirm_password=confirm_password,profile=profile,password=password)
                message = "User Registration Successfully"
                return render(request,"index.html",{'newuser':message})
            else:
                message = "Password and Confirm Password are not matched..."
                return render(request,"register.html",{'passerror':message})

        
class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")
    def post(self,request,*args,**kwargs):
        username=request.POST.get("user")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("home_view")
        else:
            return redirect('login_view')
        
class UserLogout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('login_view')
    
class HomeView(View):
    def get(self,request,*args,**kwargs):
        menu=FoodMenu.objects.all()
        menus=list(FoodMenu.objects.all())
        recommend=random.sample(menus,4)
        data=request.user
        return render(request,'homeview.html',{'foodmenu':menu,'recommend':recommend,'user':data})
    

class FoodDetailView(View):
    def get(self,request,*args,**kwargs):
        fid=kwargs.get('id')
        food=FoodMenu.objects.get(id=fid)
        menus=list(FoodMenu.objects.all())
        recommend=random.sample(menus,4)
        return render(request,'fooddetails.html',{'food':food,'recommend':recommend})
    def post(self,request,*args,**kwargs):
        fid=kwargs.get('id')
        u=request.user
        f=FoodMenu.objects.get(id=fid)
        cart=Cart.objects.filter(user=u,food=f)
        print(cart)
        if cart:
            obj=Cart.objects.get(user=u,food=f)
            obj.quantity+=1
            obj.save()
            return redirect('food_cart')
        else:
            Cart.objects.create(user=request.user,food=f,quantity=1)
            return redirect('food_cart')
        
        

class FoodCart(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            food=FoodMenu.objects.all()
            data=Cart.objects.filter(user_id=request.user)
            count=Cart.objects.filter(user_id=request.user).count()
            print(count)
            return render(request,'addtoCart.html',{'cart':data,'food':food,'count':count})
        else:
            return redirect('food_detail')
        

class SearchView(View):
    def get(self,request,*args,**kwargs):
        search=request.GET.get('search')
        result=FoodMenu.objects.filter(Q(food_name__icontains=search)|Q(category__category_name__icontains=search))
        print(result)
        menus=list(FoodMenu.objects.all())
        recommend=random.sample(menus,4)
        return render(request,'searchresult.html',{'foodmenu':result,'recommend':recommend})
class Burger(View):
    def get(self,request,*args,**kwargs):
        result=FoodMenu.objects.filter(Q(category__category_name__icontains='Burger'))
        menus=list(FoodMenu.objects.all())
        recommend=random.sample(menus,4)
        return render(request,'searchresult.html',{'foodmenu':result,'recommend':recommend})
class Pizza(View):
    def get(self,request,*args,**kwargs):
        result=FoodMenu.objects.filter(Q(category__category_name__icontains='Pizza'))
        menus=list(FoodMenu.objects.all())
        recommend=random.sample(menus,4)
        return render(request,'searchresult.html',{'foodmenu':result,'recommend':recommend})
class Wine(View):
    def get(self,request,*args,**kwargs):
        result=FoodMenu.objects.filter(Q(category__category_name__icontains='Wine'))
        menus=list(FoodMenu.objects.all())
        recommend=random.sample(menus,4)
        return render(request,'searchresult.html',{'foodmenu':result,'recommend':recommend})
class IceCream(View):
    def get(self,request,*args,**kwargs):
        result=FoodMenu.objects.filter(Q(category__category_name__icontains='Ice cream'))
        menus=list(FoodMenu.objects.all())
        recommend=random.sample(menus,4)
        return render(request,'searchresult.html',{'foodmenu':result,'recommend':recommend})
class Coffee(View):
    def get(self,request,*args,**kwargs):
        result=FoodMenu.objects.filter(Q(category__category_name__icontains='Coffee'))
        menus=list(FoodMenu.objects.all())
        recommend=random.sample(menus,4)
        return render(request,'searchresult.html',{'foodmenu':result,'recommend':recommend})
class Seafood(View):
    def get(self,request,*args,**kwargs):
        result=FoodMenu.objects.filter(Q(category__category_name__icontains='Seafood'))
        menus=list(FoodMenu.objects.all())
        recommend=random.sample(menus,4)
        return render(request,'searchresult.html',{'foodmenu':result,'recommend':recommend})
class Healthy(View):
    def get(self,request,*args,**kwargs):
        result=FoodMenu.objects.filter(Q(category__category_name__icontains='Meals&Breakfast'))
        menus=list(FoodMenu.objects.all())
        recommend=random.sample(menus,4)
        return render(request,'searchresult.html',{'foodmenu':result,'recommend':recommend})
class CartDelete(View):
    def get(self,request,*args,**kwargs):
        cart_id=kwargs.get('id')
        data=Cart.objects.get(id=cart_id)
        data.delete()
        return redirect('food_cart')
class UserProfile(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        data=User.objects.get(id=id)
        return render(request,'userprofile.html',{'user':data})

class EditProfile(View):
    def get(self,request,*args,**kwargs):
        uid=kwargs.get('id')
        data=User.objects.get(id=uid)
        return render(request,"editprofile.html",{'user':data})
    def post(self,request,*args,**kwargs):
        uid=kwargs.get('id')
        data=User.objects.get(id=uid)
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        address=request.POST["address"]
        email=request.POST["email"]
        mobile=request.POST["mobile"]
        profile=request.FILES["profile"]
        data.first_name=first_name
        data.last_name=last_name
        data.address=address
        data.email=email
        data.mobile=mobile
        data.profile=profile
        data.save()
        return redirect('user_profile',id=uid)
    
class BuyNow(HomeView):
    def get(self,request,*args,**kwargs):
        return render(request,"buynow.html",{'user':request.user})
    def post(self,request,*args,**kwargs):
        uid=kwargs.get('id')
        cart=Cart.objects.get(id=uid)
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        address=request.POST["address"]
        email=request.POST["email"]
        mobile=request.POST["mobile"]
        food=cart.food
        quantity=cart.quantity
        data = Order.objects.create(cart=uid,user=request.user,food=food,quantity=quantity,first_name=first_name,last_name=last_name,email=email,mobile=mobile,address=address)

        # email generation
        if data:
            cart_id=kwargs.get('id')
            data=Cart.objects.get(id=cart_id)
            data.delete()
            user=Order.objects.get(cart=cart_id)
            sub="Thank You for Choosing Us ......."
            msg="Hey " +user.first_name+  " ,you are successfully ordered.We just wanted to take a moment to thank you for choosing us for your food delivery needs.We hope that you enjoyed the food and the services ,and that we met your expectations."
            rec=user.email
            send_mail(sub,msg,settings.EMAIL_HOST_USER,[rec])
            success='Order Successfully'
            return render(request,'success.html',{'success':success})
        else:
            error="Order Failed"
            return render(request,'success.html',{'success':success})

class AddWishlist(View):
    def get(self,request,*args,**kwargs):
        menu=FoodMenu.objects.all()
        menus=list(FoodMenu.objects.all())
        recommend=random.sample(menus,4)
        data=request.user
        return render(request,'homeview.html',{'foodmenu':menu,'recommend':recommend,'user':data})
    
    def post(self,request,*args,**kwargs):
        if 'wishlistbtn' in request.POST:
            uid=kwargs.get('id')
            user=request.user
            data=FoodMenu.objects.get(id=uid)
            wishlist=WishlistModel.objects.filter(user=user,food=data)
            if wishlist:
                return redirect('home_view')
            else:
                WishlistModel.objects.create(user=request.user,food=data)
                return redirect('home_view')

class WishlistView(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            food=FoodMenu.objects.all()
            data=WishlistModel.objects.filter(user_id=request.user)
            count=data.count()
            print(count)
            return render(request,'wishlist.html',{'wishlist':data,'food':food,'count':count})
        else:
            return redirect('home_view')
    def post(self,request,*args,**kwargs):
        fid=kwargs.get('id')
        u=request.user
        f=FoodMenu.objects.get(id=fid)
        cart=Cart.objects.filter(user=u,food=f)
        print(cart)
        if cart:
            obj=Cart.objects.get(user=u,food=f)
            obj.quantity+=1
            obj.save()
            return redirect('food_cart')
        else:
            Cart.objects.create(user=request.user,food=f,quantity=1)
            return redirect('food_cart')
 
class WishlistDelete(View):
    def get(self,request,*args,**kwargs):
        cart_id=kwargs.get('id')
        data=WishlistModel.objects.get(id=cart_id)
        data.delete()
        return redirect('wishlist_view')
class ContactUs(View):
    def get(self,request,*args,**kwargs):
        return render(request,'contactus.html')

class OrderView(View):    
    def get(self,request,*args,**kwargs):
            if request.user.is_authenticated:
                food=FoodMenu.objects.all()
                data=Order.objects.filter(user_id=request.user)
                count=Order.objects.filter(user_id=request.user).count()
                print(count)
                return render(request,'orders.html',{'cart':data,'food':food,'count':count})
            else:
                return redirect('home_view')