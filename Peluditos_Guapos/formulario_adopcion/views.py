from django.shortcuts import render
from .forms import FormAdoptionForm 
from .models import form_adoption as model_form
from CajaMascotas.models import StateBox
from AdopcionMascotas.models import StatePet

from CajaMascotas.utils import get_or_create_box

from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.




def form_adoption(request):

    if request.method == 'POST':
        form = FormAdoptionForm(request.POST, request.FILES)

        if form.is_valid():

        
            model_form = form.save(commit=False)
            model_form.user = request.user
            model_form.save()

            request.session['adoption_id'] = model_form.id
            box = get_or_create_box(request)



            box.StateBox =  StateBox.objects.get(name="Terminado")

            box.save()


            messages.success(request,'Solcitud Enviada exitosamente, Nuestros ascesores revisaran su solicitud en los proximos 5 dias habiles')
            return redirect('index_real')

    else:
        form = FormAdoptionForm()

    return render(request,'form_adoption.html',{
        'form': form
    })


def details_adoption(request):
    adoption_id = request.session.get('adoption_id')
    box = get_or_create_box(request)



    # Utiliza el modelo 'form_adoption' para hacer la consulta, no el formulario 'form_adoption'
    adoption = model_form.objects.filter(id=adoption_id).first()


    return render(request, 'details_adoptions.html', {
        'adoption': adoption,
        'box':box
    })