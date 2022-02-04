from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from . import models, forms


class ProductListView(ListView):
    queryset = models.ProductCL.objects.filter().order_by("-id")
    template_name = "clothes_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter().order_by("-id")


class ProductCLListView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name="LuxClothes").order_by("-id")
    template_name = "lux_clothes_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name="LuxClothes").order_by("-id")


class ProductSportListView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name="Sport clothes").order_by("-id")
    template_name = "sport_clothes_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name="Sport clothes").order_by("-id")



class ProductDetailViewCl(DetailView):
    template_name = "clothes_detail.html"

    def get_object(self, **kwargs):
        clothes_id = self.kwargs.get("id")
        return get_object_or_404(models.ProductCL, id=clothes_id)


class OrderCreateViewCl(CreateView):
    template_name = "add_order_cl.html"
    form_class = forms.OrderForm
    success_url = "/clothes/"
    queryset = models.OrderCL.objects.all()

    def form_valid(self, form):
        return super(OrderCreateViewCl, self).form_valid(form=form)
