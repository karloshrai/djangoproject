from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('term', views.term, name='term'),
    path('policy', views.policy, name='policy'),
    path('contact', views.contact, name='contact'),
    path('slider-details/<slug>', views.slider_details, name='slider-details'),
    path('blog/<cat_slug>', views.category_data, name='category_blog'),
    path('blog/blog_details/<slug>', views.blog_details, name='blog_details'),
    path('register', views.user_register, name='register'),
    path('login', views.user_login, name='login'),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
         name="password_reset_complete"),

    path('users', views.users, name='users'),
    path('user_logout', views.users_logout, name='user_logout'),
    path('package', views.get_package, name='package'),
    path('package/package-details/<id>', views.package_details, name='package-details'),
    path('booking/<package_id>', views.book, name='booking'),
    path('get_booking_details/<id>', views.get_booking_details, name='get_booking_details'),
    path('delete_booking_details/<id>', views.delete_booking_details, name='delete_booking_details'),
    path('hotel', views.get_hotel, name='hotel'),
    path('hotel/hotel-details/<id>', views.h_details, name='h-details'),
    path('hotelbooking/<hotel_id>', views.hotelbook, name='hotelbooking'),
    path('hotel_details', views.hotel_details, name='hotel_details'),
    path('get_hotelbooking_details/<id>', views.get_hotelbooking_details, name='get_hotelbooking_details'),
    path('delete_hotelbooking_details/<id>', views.delete_hotelbooking_details, name='delete_hotelbooking_details'),
    path('create-checkout-session/<id>', views.CreateCheckoutSession.as_view(), name='create-checkout-session'),
    path('success', views.SuccessPayment.as_view(), name='success'),
    path('cancel', views.CancelPayment.as_view(), name='cancel'),
    path('enquiry', views.enquiry, name='enquiry'),
    path('enquiry-get', views.enquiry_get, name='enquiry-get'),
    path('enquiry-insert', views.enquiry_insert, name='enquiry-insert'),
    path('enquiry-delete/<id>', views.enquiry_delete, name='enquiry-delete'),
    path('enquiry-edit/<id>', views.enquiry_edit, name='enquiry-edit'),
    path('enquiry-update/<id>', views.enquiry_update, name='enquiry-update'),
]
