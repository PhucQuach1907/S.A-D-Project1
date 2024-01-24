# from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.contrib import messages
# from .forms import ProductAddToCartForm
# from .models import CartItem
# from product.models import Product

# def add_to_cart(request, product_slug):
#     product = Product.objects.get(slug=product_slug)

#     if request.method == 'POST':
#         form = ProductAddToCartForm(request.POST, request=request)
#         if form.is_valid():
#             quantity = form.cleaned_data['quantity']

#             cart_item, created = CartItem.objects.get_or_create(
#                 cart_id=request.session.session_key,
#                 product=product
#             )

#             if not created:
#                 cart_item.quantity += quantity
#             else:
#                 cart_item.quantity = quantity

#             cart_item.save()

#             messages.success(request, f'{product.name} has been added to your cart.')
#     else:
#         form = ProductAddToCartForm(request=request)

#     context = {'form': form, 'product': product}
#     return render(request, 'cart.html', context)
