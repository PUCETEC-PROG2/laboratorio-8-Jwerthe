from django import forms 
from .models import Pokemon, Trainer

class PokemonForm(forms.ModelForm):
    class Meta: 
        model = Pokemon
        #fields = ['name', 'type', 'weight', 'heigth', 'trainer', 'picture']
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'type':forms.Select(attrs={'class': 'form-control'}),
            'weight':forms.NumberInput(attrs={'class': 'form-control'}),
            'height':forms.NumberInput(attrs={'class': 'form-control'}),
            'trainer':forms.Select(attrs={'class': 'form-control-file'}),
            'picture':forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'
        widgets = {
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date':forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'level':forms.NumberInput(attrs={'class': 'form-control'}),
            'region':forms.Select(attrs={'class': 'form-control-file'}),
            'picture':forms.ClearableFileInput(attrs={'class': 'form-control-file'}),            
        }