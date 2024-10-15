from .models import AdoptBox,StateBox

def get_or_create_box(request):

    user = request.user 
    box_id = request.session.get('box_id')
    #estamos filtrando los carritos con ese id 7y si no existe first nos retorna None
    box  = AdoptBox.objects.filter(box_id = box_id).first()

    #si carrito de compras no existe creame uno
    if box is None:
        box = AdoptBox.objects.create(user=user)
        state_box = StateBox.objects.get(name="En proceso")
        box.StateBox = state_box
        box.save()


    if user and box.user is None:
        box.user = user
        box.save()


    

    request.session['box_id'] = box.box_id

    return box

