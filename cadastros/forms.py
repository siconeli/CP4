from typing import Any
from django import forms
from django.forms.fields import Field
from .models import Andamento

# Funções para preencher o campo processo automaticamente no cadastro de andamento, de acordo com o ID do processo passada pela URL
class AndamentoForm(forms.ModelForm):
    class Meta:
        model = Andamento
        fields = ['processo', 'datandamento', 'andamento', 'dataprazo', 'locprocesso', 'Funcionario', 'datrecebimento', 'complemento', 'arq1', 'arq2', 'arq3', 'arq4', 'arq5', 'arq6' ]

    # Recupera a pk(primary key) do kwargs e define como atributo do formulário
    def __init__(self, *args, **kwargs):
        self.processo_pk = kwargs.pop('processo_pk', None) # 'processo_pk' é configurado na url de cadastro de andamento, para obter o pk do processo
        super().__init__(*args, **kwargs)

    def get_initial_for_field(self, field, field_name):
        # Preenche automaticamente o campo ForeignKey com nome processo
        if field_name == 'processo':
            return self.processo_pk
        
        return super().get_initial_for_field(field, field_name)
 