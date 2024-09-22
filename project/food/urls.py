from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from food import views

urlpatterns = [
    path("reg/view",views.RegistrationView.as_view(),name="registration_view"),
    path("",views.LoginView.as_view(),name="login_view"),
    path("logout/",views.UserLogout.as_view(),name="logout_view"),
    path("home/view",views.HomeView.as_view(),name="home_view"),
    path('fooddetail/<int:id>',views.FoodDetailView.as_view(),name='food_detail'),
    path('foodcart/',views.FoodCart.as_view(),name='food_cart'),
    path('search/',views.SearchView.as_view(),name='search_result'),
    path('search/burger',views.Burger.as_view(),name='search_burger'),
    path('search/pizza',views.Pizza.as_view(),name='search_pizza'),
    path('search/wine',views.Wine.as_view(),name='search_wine'),
    path('search/icecream',views.IceCream.as_view(),name='search_icecream'),
    path('search/coffee',views.Coffee.as_view(),name='search_coffee'),
    path('search/seafood',views.Seafood.as_view(),name='search_seafood'),
    path('search/healthy',views.Healthy.as_view(),name='search_healthy'),
    path('cart/delete/<int:id>',views.CartDelete.as_view(),name='cart_delete'),
    path('user/profile/<int:id>',views.UserProfile.as_view(),name='user_profile'),
    path('edit/profile/<int:id>',views.EditProfile.as_view(),name='edit_profile'),
    path('cart/buynow/<int:id>',views.BuyNow.as_view(),name='buy_now'),
    path('wish/<int:id>',views.AddWishlist.as_view(),name='wish_list'),
    path('wish/list/',views.WishlistView.as_view(),name='wishlist_view'),
    path('contactus/',views.ContactUs.as_view(),name='contact_us'),
    path('order/view',views.OrderView.as_view(),name='order_view'),
    path('wishlist/delete/<int:id>',views.WishlistDelete.as_view(),name='wishlist_delete'),























]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)