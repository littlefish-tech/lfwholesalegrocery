from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        product = request.POST['product']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        salesmanager_email = request.POST['salesmanager_email']

        #  Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                product_id=product_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You have already made an inquiry for this product')
                return redirect('/products/'+product_id)

        contact = Contact(product=product, product_id=product_id, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)

        contact.save()
        send_mail(
            'Product Inquiry'
            'There has been an inquiry for ' + product +
            '. Sign into the admin panel for more info',
            'yimeng.yu@gmail.com',
            [salesmanager_email, 'yvonne.shop123@gmail.com'],
            fail_silently=False
        )

        messages.success(
            request, 'Your request has been submitted, the Sales Manager will get back to you soon')
        return redirect('/products/'+product_id)
