from .models import OrderModel, OrderStatusModel, ProductModel, GaleryModel
from rest_framework import serializers


class GalerySerializers(serializers.ModelSerializer):
    class Meta:
        model = GaleryModel
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    images = GalerySerializers(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = ProductModel
        fields = ('id', 'product_name', 'description', 'added_at', 'images', 'uploaded_images')

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        product_id = ProductModel.objects.create(**validated_data)

        for image in uploaded_images:
            GaleryModel.objects.create(product_id=product_id, image=image)

        return product_id


class ProductSerializers2(serializers.ModelSerializer):
    p = GalerySerializers(read_only=True, many=True)

    class Meta:
        model = ProductModel
        fields = '__all__'
