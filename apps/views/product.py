from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from apps.models import Category, Product


class HomeListView(ListView):
    queryset = Category.objects.all()
    template_name = 'apps/home.html'
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['products'] = Product.objects.all()
        return data

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'apps/product-list.html'
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        slug = self.request.GET.get("category")
        data['slug'] = slug
        if not slug == "all":
            data['products'] = data.get('products').filter(category__slug=slug)
        data['categories'] = Category.objects.all()
        return data


class SearchListView(View):
    def post(self, request):
        search = request.POST.get("search")
        products = Product.objects.filter(Q(name__icontains=search) | Q(description__icontains=search))
        context = {"products": products}
        return render(request, 'apps/search.html', context)
