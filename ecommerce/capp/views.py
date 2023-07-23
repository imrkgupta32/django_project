
# # Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Company
# from django.contrib.auth.models import User
# # def aboutUs(request):
# #     return HttpResponse("Welcome to the Order Management System")


def company_detail(request, company_id):
    try:
        company = Company.objects.get(Company, id=company_id)
        # company = Company.objects.get(Company_id=48)
        response_data = {
            'company': company.company,
            'email_id': company.email_id,
            'ph_no': company.ph_no,
            'state': company.state,
            'city': company.city,
            'zipcode:':company.zipcode,
            
        }
        return HttpResponse(response_data, content_type='application/json')
    except Company.DoesNotExist:
        return HttpResponse('Company not found.', status=404)




def search_feature(request):
    # Check if the request is a post request.
    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search_query = request.POST['search_query']
        # Filter your model by the search query
        companies = Company.objects.filter(company__contains=search_query)
        return render(request, 'capp/index.html', {'query': search_query, 'companies': companies})
    else:
        return render(request, 'capp/index.html', {})



# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User, Group, Permission

# def company_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)

#         if user is not None and user.groups.filter(name='Company').exists():
#             login(request, user)
#             # Redirect to the company's dashboard or desired page
#             return redirect('company_dashboard')
#         else:
#             # Invalid credentials or user is not in the 'Company' group
#             error_message = "Invalid login credentials"
#             return render(request, 'login.html', {'error_message': error_message})

#     return render(request, 'login.html')

# @login_required
# def company_dashboard(request):
#     # Retrieve the logged-in user's details and perform necessary operations
#     logged_in_user = request.user
#     # Your logic for the company dashboard

#     return render(request, 'company_dashboard.html', {'user': logged_in_user})
