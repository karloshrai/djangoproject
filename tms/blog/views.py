from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from blog.forms import ContactFrom
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from django.contrib.auth.models import User
from django.utils import timezone
from django.views import View
from django.views.generic.base import TemplateView

import stripe

stripe.api_key = 'sk_test_51IqDAhArl4iPt62ehV74vR7q9gDsqnp13UNjL8ufjRMuDQy3kVToCFkQQlHCJHfmNNVn55u8k9VGAxY2EWeiUzrx00XuRo8g38'


# Create your views here.

def index(request):
    data = {
        'sliderData': Slider.objects.all(),
        'packageData': Package.objects.all()
    }
    return render(request, 'pages/index/index.html', data)


def about(request):
    data = {
        'aboutData': About.objects.first()
    }
    return render(request, 'pages/about/about.html', data)


def term(request):
    data = {
        'termData': Terms.objects.first()
    }
    return render(request, 'pages/terms/termsofservices.html', data)


def policy(request):
    data = {
        'policyData': Policy.objects.first()
    }
    return render(request, 'pages/terms/policy.html', data)


@login_required(login_url='login')
@csrf_exempt
def contact(request):
    if request.method == "POST":
        fm = ContactFrom(request.POST)
        if fm.is_valid():
            fm.save()
            name = request.POST.get('full_name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            send_mail(subject, message, email, ['karloshrai270@gmail.com'])
            data = {
                'success': "Contact was successfully send",
                'status': 200
            }
            return JsonResponse(data)

    else:
        data = {
            'contactForm': ContactFrom()
        }
        return render(request, 'pages/contact/contact.html', data)


def slider_details(request, slug):
    data = {
        'sliderData': Slider.objects.get(slug=slug)
    }
    return render(request, 'pages/slider/slider-details.html', data)


def category_data(request, cat_slug):
    catData = BlogCategory.objects.get(slug=cat_slug)
    data = {
        'categoryData': catData,
        'blogData': BlogNews.objects.filter(cat_id=catData.id)
    }
    return render(request, 'pages/blog/blog-category.html', data)


def blog_details(request, slug):
    obj = BlogNews.objects.get(slug=slug)
    cat_name = obj.cat_id

    data = {
        'suggestNews': BlogNews.objects.filter(cat_id=cat_name),
        'blogDetails': BlogNews.objects.get(slug=slug)
    }
    return render(request, 'pages/blog/blog-details.html', data)


def user_register(request):
    if request.method == 'POST':
        user_obj = UserCreationForm(request.POST)
        if user_obj.is_valid():
            user_obj.save()
            messages.success(request, 'User was successfully created')
            return redirect('register')

        else:
            return redirect('register')
    else:
        data = {
            'userRegisterForm': UserCreationForm
        }
        return render(request, 'users/register.html', data)


def user_login(request):
    if request.method == "POST":
        user_request = AuthenticationForm(data=request.POST)
        if user_request.is_valid():
            user = user_request.get_user()
            login(request, user)
            return redirect('users')
        else:
            messages.error(request, 'Invalid Access')
            return redirect('login')

    else:
        data = {
            'loginForm': AuthenticationForm
        }
        return render(request, 'users/login.html', data)


@login_required(login_url='login')
def users(request):
    user_id = request.user.id
    data = {
        'bookingData': Booking.objects.filter(user_id=user_id).select_related('package_id')

    }
    return render(request, 'users/users.html', data)


def users_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')


def get_package(request):
    data = {
        'packageData': Package.objects.all()
    }
    return render(request, 'pages/package/package.html', data)


def package_details(request, id):
    data = {
        'packageDetails': Package.objects.filter(id=id)
    }
    return render(request, 'pages/package/package-details.html', data)


def get_hotel(request):
    data = {
        'hotelData': Hotel.objects.all()
    }
    return render(request, 'pages/hotel/hotel.html', data)


def h_details(request, id):
    data = {
        'hotelDetails': Hotel.objects.filter(id=id)
    }
    return render(request, 'pages/hotel/hotel-details.html', data)


def book(request, package_id):
    if request.user.is_authenticated:
        uId = request.user.id
        user = User.objects.get(id=uId)
        package = Package.objects.get(id=package_id)
        obj = Booking.objects.create(
            booking_date=timezone.now(),
            package_id=package,
            user_id=user
        )
        obj.save()

        messages.success(request, 'Booking successfully created')
        return redirect('users')

    else:
        return redirect('login')


def get_booking_details(request, id):
    data = {
        'packageData': Package.objects.get(id=id)
    }
    return render(request, 'users/booking-details.html', data)


def delete_booking_details(request, id):
    Booking.objects.filter(package_id=id).delete()
    user_id = request.user.id
    data = {
        'bookingData': Booking.objects.filter(user_id=user_id).select_related('package_id')

    }
    return render(request, 'users/users.html', data)


def hotelbook(request, hotel_id):
    if request.user.is_authenticated:
        uId = request.user.id
        user = User.objects.get(id=uId)
        hotel = Hotel.objects.get(id=hotel_id)
        obj = HotelBooking.objects.create(
            booking_date=timezone.now(),
            hotel_id=hotel,
            user_id=user
        )
        obj.save()

        messages.success(request, 'Booking successfully created')
        return redirect('hotel_details')

    else:
        return redirect('login')


@login_required(login_url='login')
def hotel_details(request):
    user_id = request.user.id
    data = {
        'bookingData': HotelBooking.objects.filter(user_id=user_id).select_related('hotel_id')

    }
    return render(request, 'users/hotel-booking.html', data)


def get_hotelbooking_details(request, id):
    data = {
        'hotelData': Hotel.objects.get(id=id)
    }
    return render(request, 'users/hotelbooking-details.html', data)


def delete_hotelbooking_details(request, id):
    HotelBooking.objects.filter(hotel_id=id).delete()
    user_id = request.user.id
    data = {
        'bookingData': HotelBooking.objects.filter(user_id=user_id).select_related('hotel_id')

    }
    return render(request, 'users/hotel-booking.html', data)


class CreateCheckoutSession(View):
    def post(self, request, *args, **kwargs):
        get_id = self.kwargs.get('id')
        obj = Package.objects.get(id=get_id)
        YOUR_DOMAIN = 'http://127.0.0.1:8000/'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': obj.price,
                        'product_data': {
                            'name': obj.title,

                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + 'success',
            cancel_url=YOUR_DOMAIN + 'cancel',
        )
        return JsonResponse({'id': checkout_session.id})


class SuccessPayment(TemplateView):
    template_name = 'users/success.html'


class CancelPayment(TemplateView):
    template_name = 'users/cancel.html'


def enquiry(request):
    return render(request, 'pages/enquiry/enquiry.html')


def enquiry_get(request):
    obj = list(Enquiry.objects.all().values())
    data = dict()
    data['enquiryData'] = obj
    return JsonResponse(data)


def enquiry_insert(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        details = request.POST.get('details')
        obj = Enquiry.objects.create(
            full_name=full_name, email=email, subject=subject, details=details)
        obj.save()
        data = {
            'success': 'Enquiry was successfully made'
        }
        return JsonResponse(data)
    else:
        return redirect('enquiry')


def enquiry_delete(request, id):
    obj = Enquiry.objects.get(id=id)
    obj.delete()
    data = {
        'success': 'Enquiry was successfully deleted'
    }
    return JsonResponse(data)


def enquiry_edit(request, id):
    obj = Enquiry.objects.get(id=id)
    data = {
        "id": obj.id,
        "full_name": obj.full_name,
        "email": obj.email,
        "subject": obj.subject,
        "details": obj.details,
    }
    return JsonResponse(data)


def enquiry_update(request, id):
    obj = Enquiry.objects.get(id=id)
    obj.full_name = request.POST.get('full_name')
    obj.email = request.POST.get('email')
    obj.subject = request.POST.get('subject')
    obj.details = request.POST.get('details')
    obj.save()
    data = {
        'success': 'Enquiry was successfully updated'
    }
    return JsonResponse(data)
