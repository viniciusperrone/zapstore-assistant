from rest_framework.decorators import action
from django.http import JsonResponse

from products.models import Product
from categories.models import Category
from brands.models import Brand


@action(detail=False, methods=['GET'])
def get_all_data(request):
    products = []
    categories = []
    brands = []

    for product in Product.objects.all():
        product_data = {
            'title': product.title,
            'description': product.description,
            'quantity': product.quantity,
            'selling_price': product.selling_price,
            'serie_number': product.serie_number,
            'brand': product.brand.name,
            'category': product.category.name
        }

        products.append(product_data)

    for category in Category.objects.all():
        category_data = {
            'name': category.name
        }

        categories.append(category_data)

    for brand in Brand.objects.all():
        brand_data = {
            'name': brand.name
        }

        brands.append(brand_data)

    response_data = {
        'products': products,
        'categories': categories,
        'brands': brands
    }

    return JsonResponse(
        data=response_data
    )
