
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Company
from .forms import CompanyForm

def company_list(request):
    # Check if the request is a GET request
    if request.method == 'GET':
        # Get the search query from the request's GET parameters
        search_query = request.GET.get('q', '')

        # Filter companies based on the search query using Q objects
        companies = Company.objects.filter(
            Q(company__username__icontains=search_query) |  # Search by company username
            Q(email_id__icontains=search_query) |          # Search by email_id
            Q(phone_no__icontains=search_query) |         # Search by phone_no
            Q(address__icontains=search_query) |          # Search by address
            Q(nationality__icontains=search_query) |      # Search by nationality
            Q(state__icontains=search_query) |            # Search by state
            Q(city__icontains=search_query) |             # Search by city
            Q(zipcode__icontains=search_query)            # Search by zipcode
        )

        return render(request, 'company_list.html', {'companies': companies, 'search_query': search_query})

    return render(request, 'company_list.html')



def company_detail(request, pk):
    # Retrieve a specific Company object using the primary key (pk)
    company = get_object_or_404(Company, pk=pk)

    return render(request, 'company_detail.html', {'company': company})

def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()

    return render(request, 'company_form.html', {'form': form})

def company_update(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm(instance=company)

    return render(request, 'company_form.html', {'form': form})

def company_delete(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        company.delete()
        return redirect('company_list')

    return render(request, 'company_confirm_delete.html', {'company': company})








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
