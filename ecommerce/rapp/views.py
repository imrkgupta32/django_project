# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from .models import  Retailer

# # Create your views here.
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


from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def view_loyalty_points(request):
    retailer = request.user.retailer_profile.first()
    loyalty_points = retailer.loyalty_points if retailer else 0
    return render(request, 'loyalty_points.html', {'loyalty_points': loyalty_points})
