from django.shortcuts import render,redirect,get_object_or_404
from .forms import AboutForm
from .models import About
import os
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# @csrf_exempt
def create(request):
  if request.method == 'POST':
    form = AboutForm(request.POST,request.FILES)
    if form.is_valid():
      form.save()
      return redirect("retrive")
  else:
    form = AboutForm()
  return render(request,'create.html',{'form':form})

# @csrf_protect
def retrive(request):
  if request.method == 'GET':
    data = About.objects.all()
  return render(request,'retrive.html',{'data':data})
 

# def view_details(request,selected_id):
  # if request.method == 'GET':
  #   data = About.objects.get()
  # return render(request,'view_personal_detail.html',{'data':data})
  # selected_data = About.objects.filter(ids=selected_id).first()
  # return render(request,'view_personal_detail.html',{'data':selected_data})

def view_details(request,selected_id):
  # if request.method == 'GET':
  #   data = About.objects.get()
  # return render(request,'view_personal_detail.html',{'data':data})
  selected_data = About.objects.get(ids = selected_id)
  return render(request,'view_personal_detail.html',{'data':selected_data})



# def update(request,selected_id):
#   update = request.POST.get(selected_id = selected_id)
#   form = AboutForm()
#   if form.is_valid():
#     form.save()
#     return HttpResponse("hhhhh")
#   return render(request,'update.html',{'form':update})

def update(request, id):
    identity = About.objects.get(ids=id)
    if request.method == 'POST':
        form = AboutForm(request.POST,request.FILES, instance=identity)
        if form.is_valid():
            if identity.image:
              image_path = identity.image.path
              if os.path.exists(image_path):
                os.remove(image_path)
            form.save()
            return redirect("retrive")
    else:
        form = AboutForm(instance=identity)
    return render(request, 'update.html', {'identity': identity, 'form': form})

def sure_delete(request,id):
  instance = About.objects.get(ids = id)
  return render(request, 'sure_delete.html',{'instance':instance})


def delete(request,id ):
  instance = About.objects.get(ids = id)
  instance.delete()
  return redirect("retrive")












########################################################################################



# def update(request, id):  
#     employee = About.objects.get(ids=id)  
#     form = AboutForm(request.POST, instance = employee)  
#     if form.is_valid():  
#         form.save()  
#         return redirect("view_details")  
#     else:
#       form = AboutForm()

#     return render(request, 'update.html', {'employee': employee, 'form':form}) 



