from django import forms

class ContactoForm(forms.Form):
    
    TIPO_CONSULTA=(
        ('', '-Seleccione-'),
        (1,'Oferta del día'),
        (2,'Comprar en cantidad'),
        (3,'Oferta para compartir'),
    )
    nombre = forms.CharField(label='Nombre', max_length=50)
    email = forms.EmailField(label='Email', max_length=50)
    asunto = forms.CharField(label='Asunto', max_length=50)
    mensaje= forms.CharField(label='Mensaje', max_length=100,widget=forms.Textarea(attrs={'rows':5,'class':'form-control'}))
    tipo_consulta = forms.ChoiceField(
        label='Tipo_consulta',
        choices= TIPO_CONSULTA,
        initial=1
    )
    suscripcion= forms.BooleanField(
        label='Suscripcion',
        required=False
    )