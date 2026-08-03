
from django.db import models
from django.db.models import ForeignKey
from apps.utils.models import BaseModel

class Product(BaseModel):
    product_name = models.CharField(max_length=200)
    product_code = models.IntegerField(default=False)

    def __str__(self):
        return self.product_name


class Material(BaseModel):
    material_name = models.CharField(max_length=200)

    def __str__(self):
        return self.material_name

class ProductMaterial(BaseModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='products')
    material = models.ForeignKey(Material,on_delete=models.CASCADE,related_name='materials')
    quantity = models.FloatField()

    def __str__(self):
        return f" {self.product.product_name }ga ketadigan {self.material.material_name} soni {self.quantity}"


class Warehouse(BaseModel):
    material = models.ForeignKey(Material,on_delete=models.CASCADE,related_name='warehouse_material')
    remainder = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return f"Warehouse raqami-{self.pk}   ||    mahsulot nomi-{self.material.material_name}  ||   soni-{self.remainder}   ||   narxi-{self.price}"









