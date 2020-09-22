from django.http import HttpResponse
from django.shortcuts import redirect


#backtracking avoid



#Checking which class the user is?



def allowed_users(allowed_roles = []):
	def decorator(view_func):
		def wrapper_func(request,*args,**kwargs):
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name
			if group in allowed_roles:
				return view_func(request,*args,**kwargs) 
			else:
				return HttpResponse("User is not authorised")
		return wrapper_func
	return decorator




"""

def standard_users(view_func):
	def wrapper_function(request,*args,**kwargs):
		group = None
		if request.user.groups.exists():
				group = request.user.groups.all()[0].name
		
		if group == '10th':
			return redirect('course-10')
		if group == '11th':
			return redirect('course-11')
		if group == '12th':
			return redirect('course-12')
	return wrapper_function
"""