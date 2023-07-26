from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import   Product,  Orders, OrderItem

# def aboutUs(request):
#     return HttpResponse("Welcome to the Order Management System")


# def company_detail(request, company_id):
#     try:
#         company = Company.objects.get(id=company_id)
#         response_data = {
#             'name': company.name,
#             'email_id': company.email_id,
#             'ph_no': company.ph_no,
#             'state': company.state,
#             'city': company.city,
#             'zipcode:':company.zipcode,
            
#         }
#         return HttpResponse(response_data, content_type='application/json')
#     except Company.DoesNotExist:
#         return HttpResponse('Company not found.', status=404)



# def dealer_detail(request, dealer_id):
#     try:
#         dealer = Dealer.objects.get(id=dealer_id)
#         response_data = {
#             'name': dealer.name,
#             'email_id': dealer.email_id,
#             'ph_no': dealer.ph_no,
#             'state': dealer.state,
#             'city': dealer.city,
#             'zipcode': dealer.zipcode,
#             'experience_years' : dealer.experience_years,
#             'company': dealer.company.name,
#         }
#         return HttpResponse(response_data, content_type='application/json')
#     except Dealer.DoesNotExist:
#         return HttpResponse('Dealer not found.', status=404)

# def fieldstaff_detail(request, fieldstaff_id):
#     try:
#         fieldstaff = FieldStaff.objects.get(id=fieldstaff_id)
#         response_data = {
#             'name': fieldstaff.name,
#             'ph_no': fieldstaff.ph_no,
#             'email_id': fieldstaff.email_id,
#             'state': fieldstaff.state,
#             'city': fieldstaff.city,
#             'zipcode': fieldstaff.zipcode,
#             'experience_years': fieldstaff.experience_years,
#             'dealer': fieldstaff.dealer.name,
#             'company' : fieldstaff.company.name,
#         }
#         return HttpResponse(response_data, content_type='application/json')
#     except FieldStaff.DoesNotExist:
#         return HttpResponse('Field Staff not found.', status=404)


# def retailer_detail(request, retailer_id):
#     try:
#         retailer = Retailer.objects.get(id=retailer_id)
#         response_data = {
#             'name': retailer.name,
#             'email_id': retailer.email_id,
#             'ph_no': retailer.ph_no,
#             'state': retailer.state,
#             'city': retailer.city,
#             'zipcode': retailer.zipcode,
#             'fieldstaff': retailer.fieldstaff.name,
#             'dealer': retailer.dealer.name,  
#             'company': retailer.company.name,  
            
#         }
#         return HttpResponse(response_data, content_type='application/json')
#     except Retailer.DoesNotExist:
#         return HttpResponse('Retailer not found.', status=404)

# def product_detail(request, product_id):
#     try:
#         product = Product.objects.get(id=product_id)
#         response_data = {
#             'name': product.name,
#             'description': product.description,
#             'price': product.price,
            
#         }
#         return HttpResponse(response_data, content_type='application/json')
#     except Product.DoesNotExist:
#         return HttpResponse('Product not found.', status=404)



# def order_detail(request, order_id):
#     try:
#         order = Orders.objects.get(id=order_id)
#         response_data = {
#             'retailer': order.retailer.name,
#             'fieldstaff': order.fieldstaff.name,
#             'dealer': order.dealer.name,
#             'order_date': order.order_date,
#             'total_amount': order.total_amount,
            
#         }
#         return HttpResponse(response_data, content_type='application/json')
#     except Orders.DoesNotExist:
#         return HttpResponse('Order not found.', status=404)

# def order_item_detail(request, order_item_id):
#     try:
#         order_item = OrderItem.objects.get(id=order_item_id)
#         response_data = {
#             'order': order_item.order,
#             'product': order_item.product.name,
#             'quantity': order_item.quantity,
#             'price': order_item.price,
#         }
#         return HttpResponse(response_data, content_type='application/json')
#     except OrderItem.DoesNotExist:
#         return HttpResponse('Order Item not found.', status=404)

from math import ceil




# from django.shortcuts import render
# from .models import Product

# def search_products(request):
#     if request.method == 'POST':
#         search_query = request.POST.get('search_query')
#         products = Product.objects.filter(name__icontains=search_query)

#         context = {
#             'products': products,
#             'search_query': search_query,
#         }

#         return render(request, 'search_results.html', context)

#     # Handle other cases, such as rendering the search form initially
#     return render(request, 'index.html')




def product_detail(request, product_id):
    products = Product.objects.filter(Product, id=product_id)
    # print(products)
    # n= len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # params = { 'no_of_slides':nSlides , 'range': range(nSlides), 'product': products}



    if products.exists():
        product = products.first()
        response_data = {
            
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'imgae': product.image,
            'category': product.category,
            'sub_category': product.sub_category,
            'company':product.company,
        }
        return HttpResponse(response_data, content_type='application/json')
    else:
        return HttpResponse('Product not found.', status=404)


# from capp.models import Company
# from django.db.models import Q

# def product_detail(request, product_id):
#     # Check if a search query is provided in the request
#     search_query = request.POST.get('search_query')
#     if search_query:
#         # Perform a search query using case-insensitive matching on the product name and category
#         products = Product.objects.filter(Q(name__icontains=search_query) | Q(category__icontains=search_query))
#     else:
#         # Retrieve the product by ID if no search query is provided
#         products = Product.objects.filter(id=product_id)

#     if products.exists():
#         product = products.first()
#         response_data = {
#             'name': product.name,
#             'description': product.description,
#             'price': product.price,
#             'image': product.image.url,
#             'category': product.category,
#             'sub_category': product.sub_category,
#             'company': product.company.company.username,
#         }
#         return HttpResponse(response_data, content_type='application/json')
#     else:
#         return HttpResponse('Product not found.', status=404)





def order_detail(request, order_id):
    orders = Orders.objects.filter(id=order_id)
    
    if orders.exists():
        order = orders.first()
        response_data = {
            # 'retailer': order.retailer.name,
            'fieldstaff': order.fieldstaff.name,
            'dealer': order.dealer.name,
            'order_date': order.order_date,
            'total_amount': order.total_amount,
        }
        return HttpResponse(response_data, content_type='application/json')
    else:
        return HttpResponse('Order not found.', status=404)


def order_item_detail(request, order_item_id):
    order_items = OrderItem.objects.filter(id=order_item_id)
    
    if order_items.exists():
        order_item = order_items.first()
        response_data = {
            'order': order_item.order,
            'product': order_item.product.name,
            'quantity': order_item.quantity,
            'price': order_item.price,
        }
        return HttpResponse(response_data, content_type='application/json')
    else:
        return HttpResponse('Order Item not found.', status=404)
    
def Index(request):
    return render(request, ' index.html')

def OrderManagementSystem(request):
    data={
        'title':'OrderManagementSystem'
    }
    return render(request, 'index.html', data)


    # return render (request, 'index.html', params)





from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Orders, OrderItem

def place_order(request):
    if request.method == 'POST':
        # Get user from the request (assuming user is authenticated)
        user = request.user

        # Get products from the user's cart (you need to implement cart functionality)
        # For simplicity, we'll assume cart_items is a list of dictionaries containing product_id and quantity.
        cart_items = request.session.get('cart_items', [])

        # Create a new order for the user
        order = Orders.objects.create(user=user)

        # Calculate the total price of the order and add order items
        total_price = 0
        for item in cart_items:
            product = Product.objects.get(pk=item['product_id'])
            quantity = item['quantity']
            item_total = product.price * quantity
            total_price += item_total
            OrderItem.objects.create(order=order, product=product, quantity=quantity, item_total=item_total)

        order.total_price = total_price
        order.save()

        # Clear the user's cart after the order is placed
        request.session['cart_items'] = []

        # Trigger a notification for the user (you can implement notification logic)
        messages.success(request, 'Your order has been placed successfully!')

        return redirect('order_confirmation')  # Redirect to the order confirmation page

    # Render the order placement page
    products = Product.objects.all()
    return render(request, 'place_order.html', {'products': products})

def order_confirmation(request):
    # Fetch the last order placed by the user
    user = request.user
    order = Orders.objects.filter(user=user).order_by('-order_date').first()

    # Display the order confirmation page with order details
    return render(request, 'order_confirmation.html', {'order': order})




# views.py
from django.shortcuts import render
from myapp.signals import order_placed

def place_order(request):
    # Your order placement logic here...

    # Emit the order_placed signal when an order is placed
    order_placed.send(sender=None, order=Orders, user=request.user)

    # Return response to the user
