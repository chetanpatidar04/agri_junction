from django.urls import path
from .views.signup import Signup
from .views.login import Login,logout
from .views.cart import Cart
from .views.checkout import Checkout
from .views.view_orders import View_order
from .views.home import Index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',Index.as_view(), name="homepage"),
    path('signup',Signup.as_view() ,name="signup"),
    path('login',Login.as_view() ,name="login"),
    path('logout',logout, name="logout"),
    path('cart',Cart.as_view(), name="cart"),
    path('checkout',Checkout.as_view(), name="checkout"),
    path('view_order',View_order.as_view(), name="view_order")    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)