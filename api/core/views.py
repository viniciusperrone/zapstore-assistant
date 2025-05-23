from rest_framework.decorators import action
from django.http import JsonResponse

from products.models import Product


@action(detail=False, methods=['GET'])
def get_all_data(request):
    response_data = {
        'products': [],
        'categories': [],
        'brands': []
    }


    return JsonResponse(
        data=response_data
    )
