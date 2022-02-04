from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("products/", views.ProductListView.as_view(), name="product_list"),
    path("add-order/", views.OrderCreateView.as_view(), name="order_create"),
    path(
        "products/<int:id>/", views.ProductDetailView.as_view(),
        name="product_detail"
    ),
]


