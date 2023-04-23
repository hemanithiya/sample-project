from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Topic,WebPage,Users
from first_app.forms import NewUser
# Create your views here.
def index(hello):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record':webpage_list}
    my_dict = {'insert_me':'this is from views.py','hello':' welcome '}
    return render(hello,'index.html',context=date_dict)

def index2(hello):
    return HttpResponse('this is the second page')

def formpage(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)

    return render(request,'formpage.html',{'form':form})
