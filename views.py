from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST) # gets the POST request data and creates usercreation form with it
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request, f'your account {username}, has been created successfully!')
			return redirect('login')
	else:
		form = UserRegistrationForm() # so, if request method is not POST method then we get a blank form 
	return render(request, 'Users/register.html', {'form':form})

#def Logout_view(request):
	# logs out the user and redirects to home page
#	if request.method == 'GET':
#		logout(request)
#		return render(request, 'Users/logout.html')
#	else:
#		return redirect('Home-Page') # to redirect to home page of app after log out

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		if u_form.is_valid():
			u_form.save()
			messages.success(request, f'your account has been updated successfully!')
			return redirect('profile-page')
	else:
		u_form = UserUpdateForm(instance=request.user)
	context = {'u_form':u_form}

	return render(request, "Users/profile.html", context)