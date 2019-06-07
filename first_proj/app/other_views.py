from django.shortcuts import render
from django.http import HttpResponse
from app.models import AccessRecord, Topic, Webpage

# Create your views here.


def index(request):
    '''
        This is the view for the index page
    '''
    web_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': web_list}
    return render(request, 'home.html', context=date_dict)
