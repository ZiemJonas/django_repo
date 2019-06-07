from django import forms
from django.core import validators

'''
    Basic django forms
'''


# def check_for_z(value):
#     '''
#         custom func to check for z at the beginning of name input

#         every validator function must hav the keyword 'value' as its parameter for django to recognize it as a validator.
# voal!!! u can now pass 'check_for_z' as a validator
#     '''

#     if value[0].lower() != 'z':
#         raise forms.ValidationError('Begin name with z')


class FormName(forms.Form):
    '''
        Working with basic forms
    '''
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='enter email again')
    text = forms.CharField(widget=forms.Textarea)

    # # VALIDATION WITH DJANGO's INBUILT VALIDATORS
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[
    #                              validators.MaxLengthValidator(0)])

    def clean(self):
        '''
            clean input fields in form
        '''
        clean_all_data = super().clean()

        email = clean_all_data['email']
        vmail = clean_all_data['verify_email']

        if email != vmail:
            raise.forms.ValidationError('Email mismatch')
