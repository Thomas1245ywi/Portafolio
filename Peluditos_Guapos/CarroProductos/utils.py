from .models import ProductBox

def get_or_create_product_box(request):
    user = request.user
    box_id = request.session.get('product_box_id')
    box = ProductBox.objects.filter(box_id=box_id).first()

    if box is None:
        box = ProductBox.objects.create(user=user)

    if user and box.user is None:
        box.user = user
        box.save()

    box.total = sum(product.price for product in box.products.all())
    box.save()

    request.session['product_box_id'] = box.box_id

    return box