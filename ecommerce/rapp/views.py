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
from django.shortcuts import render, redirect
from .models import Retailer

def retailer_detail(request, retailer_id):
    retailers = Retailer.objects.filter(id=retailer_id)
    
    if retailers.exists():
        retailer = retailers.first()
        response_data = {
            'name': retailer.name,
            'email_id': retailer.email_id,
            'ph_no': retailer.ph_no,
            'state': retailer.state,
            'city': retailer.city,
            'zipcode': retailer.zipcode,
            'fieldstaff': retailer.fieldstaff.name,
            'dealer': retailer.dealer.name,
            'company': retailer.company.name,
        }
        return HttpResponse(response_data, content_type='application/json')
    else:
        return HttpResponse('Retailer not found.', status=404)
