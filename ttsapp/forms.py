from django import forms

LANG_CHOICES = [
    ('pt', 'Português (pt-BR)'),
    ('en', 'English (en-US)'),
    ('es', 'Español (es-ES)'),
]

class TTSForm(forms.Form):
    text = forms.CharField(
        label='Texto',
        widget=forms.Textarea(attrs={
            'rows': 6,
            'placeholder': 'Digite o texto que deseja converter em áudio...'
        })
    )
    lang = forms.ChoiceField(label='Idioma', choices=LANG_CHOICES, initial='pt')
    slow = forms.BooleanField(label='Velocidade lenta', required=False)
    filename = forms.CharField(
        label='Nome do arquivo (opcional, sem extensão)',
        required=False
    )
