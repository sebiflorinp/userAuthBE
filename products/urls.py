from django.urls import path
from .views import CreateProduct, ListProductsById

urlpatterns = [
    path('products', CreateProduct.as_view()),
    path('products/<int:id>', ListProductsById.as_view())
]