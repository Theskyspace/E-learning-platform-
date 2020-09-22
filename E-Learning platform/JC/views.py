from django.shortcuts import render,redirect,HttpResponse

# used for user authentication
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

#restricting site
from django.contrib.auth.decorators import login_required
from .decorator import allowed_users


from .models import Category,Lecture

# Create your views here.



def home(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request,username=username,password=password)
	
		if user is not None:
			login(request, user)
			return redirect('course')
		else:
			messages.info(request,"Username or Password is incorrect")


	context = {}
	return render(request,'login.html',context)


def logoutUser(request):
	logout(request)
	
	return redirect('home')





@login_required(login_url='home')
#@allowed_users(allowed_roles = ['10std'])
def course(request):
	group = request.user.groups.all()[0].name
	
	if group == '9std':
		course_for_class_9 = Category.objects.filter(standard=9)

		try:
			first = course_for_class_9[0]
			context = {'courses' : course_for_class_9,'first':first}
			return render(request,'courses.html',context)
		except:

			return HttpResponse('no_lectures')



	elif group == '10std':
		course_for_class_10 = Category.objects.filter(standard=10)

		try:
			first = course_for_class_10[0]
			context = {'courses' : course_for_class_10,'first':first}
			return render(request,'courses.html',context)
		except:

			return HttpResponse('no_lectures')
	

	elif group == '11std':
		course_for_class_11 = Category.objects.filter(standard=11)

		try:
			first = course_for_class_11[0]
			context = {'courses' : course_for_class_11,'first':first}
			return render(request,'courses.html',context)
		except:
			return HttpResponse('no_lectures')

	elif group == '12std':
		course_for_class_12 = Category.objects.filter(standard=12)

		try:
			first = course_for_class_12[0]
			context = {'courses' : course_for_class_12,'first':first}
			return render(request,'courses.html',context)
		except:
			return HttpResponse('no_lectures')

	else:
		return HttpResponse('You are not enrolled in any of the classes')










#The chapter videos view

@login_required(login_url='home')
def chapter(request,idofcrs):

	chapter_vids = Lecture.objects.filter(category=idofcrs)
	cata = Category.objects.filter(id=idofcrs)

	context = {'chapter_vids':chapter_vids,'cata':cata}
	
	return render(request,'chapter.html',context)	

