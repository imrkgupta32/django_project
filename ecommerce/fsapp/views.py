
# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from .models import  FieldStaff

# # Create your views here.
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

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import FieldStaff

def fieldstaff_detail(request, fieldstaff_id):
    fieldstaffs = FieldStaff.objects.filter(id=fieldstaff_id)
    
    if fieldstaffs.exists():
        fieldstaff = fieldstaffs.first()
        response_data = {
            'name': fieldstaff.name,
            'ph_no': fieldstaff.ph_no,
            'email_id': fieldstaff.email_id,
            'state': fieldstaff.state,
            'city': fieldstaff.city,
            'zipcode': fieldstaff.zipcode,
            'experience_years': fieldstaff.experience_years,
            'dealer': fieldstaff.dealer.name,
            'company': fieldstaff.company.name,
        }
        return HttpResponse(response_data, content_type='application/json')
    else:
        return HttpResponse('Field Staff not found.', status=404)
