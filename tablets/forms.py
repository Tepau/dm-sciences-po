from django import forms
from .models import Tablets, Brand


class DeleteTabletForm(forms.ModelForm):
    class Meta:
        model = Tablets
        fields = ('id',)


class CreateBrandForm(forms.ModelForm):

    def clean_name(self):
        return self.cleaned_data['name'].capitalize()

    def clean_founder(self):
        return self.cleaned_data['name'].title()

    class Meta:
           model = Brand
           fields = '__all__'
