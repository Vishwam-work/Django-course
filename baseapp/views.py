from multiprocessing import context
from pydoc_data.topics import topics
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room,Topic
from .forms import RoomForm
from django.db.models import Q
# Create your views here.
# room_li=[
#         {'id':1,'name':'Vishwam'},
#         {'id':2,'name':'Vishant'}
#     ]

def home(request):
    q=request.GET.get('q') if request.GET.get('q')!= None else ''
    

    
#    Whitout sing templates
    # return HttpResponse("Home page")
#     Using tempaltes
   
    room_li=Room.objects.filter(
        Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(disp__icontains=q) )

    topics=Topic.objects.all()

    room_count=room_li.count()

    context={'rooms':room_li,
                'topics':topics,
                'room_count':room_count}
    return render(request,'baseapp/home.html',context)

def rooms(request,pk):
#    Whitout sing templates
    # return HttpResponse("Room")
#   with the use of templates
    # ro=None
    # for i in room_li:
    #     if i['id']==(dy):
    #         ro=i

    # using models
    ro=Room.objects.all()
    context={'room':ro}
    return render(request,'baseapp/room.html',context)

def show(request):
    form=RoomForm()
    if request.method =='POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request ,'baseapp/show.html',context)

def updateroom(request,pk):
    room = Room.objects.get(id=pk)
    form=RoomForm(instance=room)
    if request.method=="POST":
        form=RoomForm(request.POST,instance=room)
        if form.is_valid:
            try:
                form.save()
                return redirect('home')
            except:
                pass

    context={'form':form}
    return render(request,'baseapp/show.html',context)
    
def deleteroom(request,pk):
    room=Room.objects.get(id=pk)
    if(request.method=="POST"):
        room.delete()
        return redirect('home')
    return render(request,'baseapp/delete.html',{'obj':room})