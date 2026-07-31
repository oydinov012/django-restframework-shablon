
from django.db import models
from apps.utils.models import BaseModel

class Product(BaseModel):
    product_name = models.CharField(max_length=200)
    product_code = models.IntegerField(default=False)


class Material(BaseModel):
    material_name = models.CharField(max_length=200)


class ProductMaterial(BaseModel):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_id')
    material_id = models.ForeignKey(Material,on_delete=models.CASCADE,related_name='material_id')
    quantity = models.IntegerField()



class Warehouse(BaseModel):
    material_id = models.ForeignKey(Material,on_delete=models.CASCADE,related_name='warehouse_material_id')
    remainder = models.IntegerField()
    price = models.IntegerField()











