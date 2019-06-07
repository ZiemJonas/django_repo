from django.shortcuts import render
from django.http import HttpResponse
from app.models import AccessRecord, Topic, Webpage
from . import forms

# Create your views here.


def index(request):
    '''
        This is the view for the index page
    '''

    web_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': web_list}
    return render(request, 'index.html', context=date_dict)


def form_name_view(request):
    '''
        This view handles form request.
    '''
    form = forms.FormName()

    # Test for method attribute if POST, GET OR HTTP
    if request.method == 'POST':
        # passing request method to form
        form = forms.FormName(request.POST)

        # check if form is valid
        if form.is_valid():
            print('validation success!!!')

            # Process form data (print form data to console)
            print('Name: {}'.format(str(form.cleaned_data['name'])))
            print('Email: {}'.format(form.cleaned_data['email']))
            print('Text: {}'.format(form.cleaned_data['text']))

    return render(request, 'index.html', {'form': form})
