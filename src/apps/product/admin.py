from django.contrib import admin
from apps.product.models import ProductMaterial, Product, Material, Warehouse

admin.site.register(Product)
admin.site.register(ProductMaterial)
admin.site.register(Warehouse)
admin.site.register(Material)