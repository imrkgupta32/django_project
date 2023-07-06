from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import  Dealer
# # Create your views here.
# def dealer_detail(request, dealer_id):
#     try:
#         dealer = Dealer.objects.get(id=dealer_id)
#         response_data = {
#             'name': dealer.dealer,
#             'email_id': dealer.email_id,
#             'ph_no': dealer.ph_no,
#             'state': dealer.state,
#             'city': dealer.city,
#             'zipcode': dealer.zipcode,
#             'experience_years' : dealer.experience_years,
#             'company': dealer.company,
#         }
#         return HttpResponse(response_data, content_type='application/json')
#     except Dealer.DoesNotExist:
#         return HttpResponse('Dealer not found.', status=404)




from capp.models import Company
from django.shortcuts import get_object_or_404

def dealer_detail(request, dealer_id):
    company = request.user.company

    dealer = get_object_or_404(Dealer, id=dealer_id, company=company)

    response_data = {
        'dealer': dealer.dealer,
        'email_id': dealer.email_id,
        'ph_no': dealer.ph_no,
        'state': dealer.state,
        'city': dealer.city,
        'zipcode': dealer.zipcode,
        'experience_years': dealer.experience_years,
        'company': dealer.company,
    }

    return HttpResponse(response_data, content_type='application/json')

