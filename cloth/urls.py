from django.urls import path
from . import views

app_name = "clothes"
urlpatterns = [
    path("clothes/", views.ProductListView.as_view(), name="clothes_list"),
    path("lux_clothes/", views.ProductListView.as_view(), name="lux_clothes_list"),
    path("sport_clothes/", views.ProductSportListView.as_view(), name='sport_clothes'),
    path("add-order_cl/", views.OrderCreateViewCl.as_view(), name="order_cl_creat"),
    path(
        "clothes/<int:id>/", views.ProductDetailViewCl.as_view(), name="clothes_detail"
    ),
]
