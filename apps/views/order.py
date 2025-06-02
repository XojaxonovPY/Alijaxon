
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from apps.forms import OrderModelForm
from apps.models import Product, Order, AdminSetting


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "apps/product-detail.html"
    context_object_name = 'product'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['discount_price'] = data.get('product').discount_price
        return data


class OrderCreateView(CreateView):
    queryset = Order.objects.all()
    template_name = 'apps/product-detail.html'
    success_url = reverse_lazy('home')
    form_class = OrderModelForm

    def form_valid(self, form):
        super().form_valid(form)
        admin_setting = AdminSetting.objects.first()

        context = {
            "order": self.object,
            "deliver_price": admin_setting.deliver_price,
        }
        return render(self.request, 'apps/order/order-success.html', context)


class OrderListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("auth")
    queryset = Order.objects.all()
    template_name = "apps/order/order-list.html"
    context_object_name = "orders"

    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(owner=self.request.user)


class RequestTemplateView(ListView):
    queryset = Order.objects.all()
    template_name = 'apps/order/requests.html'
    context_object_name = 'requests'

    def get_queryset(self):
        query=super().get_queryset()
        query=query.filter(owner=self.request.user).select_related('product').select_related('thread')
        return query