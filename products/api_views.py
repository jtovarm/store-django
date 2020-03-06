import json
from datetime import datetime
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from products.models import Products, DataTable

@csrf_exempt
def get_products_dt(request):

    columns = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'price': 'price',
        'date_up': 'date_up'
    }

    data_table = DataTable(request.POST, columns)

    base_query = Products.objects.all()

    count_query_set = base_query

    query_set = base_query.filter(
        Q(name__icontains=data_table.search_value) |
        Q(description__icontains=data_table.search_value) |
        Q(price__icontains=data_table.search_value)
    )

    total = count_query_set.count()

    records_filtered = query_set.count()

    query_set = query_set.order_by(*data_table.get_orderings())

    products = query_set[data_table.start:data_table.limit]

    results = []
    for product in products:
        reg_dict = {
            'id': product.pk,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'date_up': product.date_up
        }

        results.append(reg_dict)

    response = {
        'draw': data_table.draw,
        'recordsTotal': total,
        'recordsFiltered': records_filtered,
        'data': results
    }

    return JsonResponse(response, status=200)


def get_products(request):
    products = Products.objects.all()

    results = []
    for product in products:
        reg_dict = {
            'id': product.pk,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'date_up': product.date_up,
            'image': product.image.url if product.image else ''
        }

        results.append(reg_dict)

    response = {
        'products_list': results
    }

    return JsonResponse(response, status=200)


def get_product(request, uuid):
    id_product = uuid

    product = Products.objects.filter(pk=id_product).get()

    if not product:
        return JsonResponse({}, status=400)

    response = {
        'name': product.name,
        'description': product.description,
        'precio': product.price,
        'date_up': product.date_up,
        'image': product.image.url if product.image else ''
    }

    return JsonResponse(response, status=200)


@csrf_exempt
def add_product(request):
    params = json.loads(request.POST['json'])

    name = params['name']
    price = params['precio']
    description = params['description']
    date_up = datetime.now()

    if not name:
        return JsonResponse({}, status=400)

    product = Products()
    product.name = name
    product.description = description
    product.price = price
    product.date_up = date_up
    product.save()

    response = {
        'created': True
    }
    return JsonResponse(response, status=200)


@csrf_exempt
def update_product(request, uuid):
    id_product = uuid
    params = json.loads(request.POST['json'])

    name = params['name']
    price = params['precio']
    description = params['description']

    if not id_product:
        return JsonResponse({}, status=400)

    product = Products.objects.filter(pk=id_product).update(name=name, description=description, price=price)

    response = {
        'created': True
    }
    return JsonResponse(response, status=200)


def delete_product(request, uuid):
    id_product = uuid

    Products.objects.filter(pk=id_product).delete()

    response = {
        'product_deleted': True
    }

    return JsonResponse(response, status=200)


@csrf_exempt
def upload_file(request):
    file_obj = request.FILES['file']

    product = Products.objects.last()
    product.image = file_obj
    product.save()
    
    return HttpResponse({})

@csrf_exempt
def update_file(request, uuid):
    id_product = uuid
    file_obj = request.FILES['file']

    product = Products.objects.get(id=id_product)
    product.image = file_obj
    product.save()
    
    return HttpResponse({})


@csrf_exempt
def search_product(request):
    terms = json.loads(request.POST['json'])

    if not terms:
        return JsonResponse({}, status=400)

    base_query = Products.objects.all()
    
    query_set = base_query.filter(
        Q(name__icontains=terms) |
        Q(description__icontains=terms) |
        Q(price__icontains=terms)
    )

    results = []
    for product in query_set:
        reg_dict = {
            'id': product.pk,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'date_up': product.date_up,
            'image': product.image.url if product.image else ''
        }

        results.append(reg_dict)

    response = {
        'products_list': results
    }
    return JsonResponse(response, status=200)