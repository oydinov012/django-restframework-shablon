# views.py

from collections import defaultdict

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.product.models import Product, ProductMaterial, Warehouse
from api.serializer.product_serializer import ProductRequestSerializer


class CalculateAPIView(APIView):

    def post(self, request):
        serializer = ProductRequestSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        products = serializer.validated_data  # bu — list of dict

        warehouses = Warehouse.objects.select_related("material").order_by("id")

        stock = defaultdict(list)

        for warehouse in warehouses:
            stock[warehouse.material.material_name].append({
                "warehouse_id": warehouse.pk,
                "remainder": warehouse.remainder,
                "price": warehouse.price
            })

        result = []

        for item in products: # type: ignore
            product = Product.objects.get(product_code=item["product_code"])

            recipes = ProductMaterial.objects.filter(
                product=product
            ).select_related("material")

            product_result = {
                "product_code": product.product_code,
                "product_name": product.product_name,
                "quantity": item["quantity"],
                "product_materials": []
            }

            for recipe in recipes:
                need = recipe.quantity * item["quantity"]
                lots = stock[recipe.material.material_name]

                for lot in lots:
                    if need == 0:
                        break
                    if lot["remainder"] == 0:
                        continue

                    take = min(need, lot["remainder"])

                    product_result["product_materials"].append({
                        "warehouse_id": lot["warehouse_id"],
                        "material_name": recipe.material.material_name,
                        "qty": take,
                        "price": lot["price"]
                    })

                    lot["remainder"] -= take
                    need -= take

                if need > 0:
                    product_result["product_materials"].append({
                        "warehouse_id": None,
                        "material_name": recipe.material.material_name,
                        "qty": need,
                        "price": None
                    })

            result.append(product_result)

        return Response({"result": result})