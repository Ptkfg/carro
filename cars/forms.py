from typing import Any
from django import forms
from cars.models import car


class CarModelForm(forms.ModelForm):
    class Meta():
        model = car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 15000:
            self.add_error('value', 'Valor minimo do carro deve ser de R$15.000')
        else:
            return value
        
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Não são permitidos os cadastros de carros com o ano abaixo de 1975')
        else:
            return factory_year


