"""thehouseofmouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pages.views import home_view, faqs_view, about_view
from accounts.views import register_view, profile_view
from products.views import results_view, all_products_view, ListingDetailView, famous_category_view, special_category_view, harry_potter_category_view, starwars_category_view, misc_category_view, jobs_category_view, doctor_who_category_view, xmas_category_view, halloween_category_view, categories_view
from cart.views import cart_view, checkout_info_view, checkout_shipping_view, checkout_payment_view, checkout_confirm_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # standard pages
    path('', home_view, name="home"),
    path('faqs/', faqs_view, name="faqs"),
    path('about/', about_view, name="about"),

    # user account pages
    path('register/', register_view, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('profile/', profile_view, name="profile"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name="password_reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm"),

    # listings
    path('listing/<int:pk>/', ListingDetailView.as_view(), name="listing-detail"),
    path('results/', results_view, name="results"),
    path('all-products/', all_products_view, name="all-products"),
    path('categories/', categories_view, name="categories"),
    path('categories/famous', famous_category_view, name="famous"),
    path('categories/special-occasions', special_category_view, name="special-occasions"),
    path('categories/harry-potter', harry_potter_category_view, name="harry-potter"),
    path('categories/star-wars', starwars_category_view, name="star-wars"),
    path('categories/weird-misc', misc_category_view, name="weird-misc"),
    path('categories/jobs-hobbies', jobs_category_view, name="jobs-hobbies"),
    path('categories/doctor-who', doctor_who_category_view, name="doctor-who"),
    path('categories/christmas', xmas_category_view, name="christmas"),
    path('categories/halloween', halloween_category_view, name="halloween"),

    # cart and payment
    path('cart/', cart_view, name="cart"),
    path('checkout/info/', checkout_info_view, name="info"),
    path('checkout/shipping/', checkout_shipping_view, name="shipping"),
    path('checkout/payment/', checkout_payment_view, name="payment"),
    path('checkout/confirm/', checkout_confirm_view, name="confirm"),

]

# only add this in when in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
