# # from django.shortcuts import render

# # # Create your views here.

# from django.shortcuts import render, redirect
# from .models import CustomUser


# def user_list(request):
#     users = CustomUser.objects.all()
#     return render(request, 'user_list.html', {'users': users})


# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, logout

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('account:login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'account/register.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('account:profile')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'account/login.html', {'form': form})

# def logout_view(request):
#     logout(request)
#     return redirect('account:login')

# def profile(request):
#     return render(request, 'account/profile.html')
