from django.shortcuts import render
from .forms import ProductForm
from .models import Product
from django.shortcuts import get_object_or_404
from django.http import Http404


# Create your views here.

def render_initial_data(request):
    initial_data = {
        'title': "My this is awesome title!"
    }
    obj = Product.objects.get(id = 1)
    form = ProductForm(request.POST or None, initial = initial_data, instance = obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             #now data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#                 'form' : my_form
#
#             }
#     return render(request, "products/product_create.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    context = {
    'object': obj
    }
    return render(request, "products/product_detail.html", context)


def dynamic_lookup_view(request, my_id):
    # obj = Product.objects.get(id=my_id)
    try:
        obj = Product.objects.get(id = my_id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object" : obj
    }
    return render(request, "products/product_detail.html", context)

def product_delete_view(request, my_id):
    obj = Product.objects.get(id = my_id)
    if request.method == 'POST':
        obj.delete()
    context = {
    }
    return render(request, "products/product_delete.html", context)
