from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_save



class Category(models.Model):
    name = models.CharField(max_length=200, blank=False, null=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255, blank=False)
    image = models.ManyToManyField('ProductImage', related_name='products')

    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

    country = models.CharField(max_length=100, blank=True, null=True)
    assembly_required = models.BooleanField(default=False) # требуется сборка или нет

    notes = models.TextField(max_length=500, null=True, blank=True)

    depth = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    height = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    weight = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    width = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    package_length = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    package_height = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    package_width = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    
    default_delivery_price = models.DecimalField(max_digits=10, decimal_places=2, default=5.00, blank=True)
    default_delivery_time = models.IntegerField(default=5, blank=True)

    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.image.name


class Application(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# from django.contrib.auth import get_user_model
# User = get_user_model()


# class Cart(models.Model):
#     just_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
#     oredered = models.BooleanField(default=False)
#     total_price = models.FloatField(default=0)

#     def __str__(self):
#         return str(self.just_user.username) + " " + str(self.total_price)
#         # return str(self.just_user)

# class CartItems(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
#     # user = models.ForeignKey(User, on_delete=models].CASCADE, null=True)
#     product = models.ForeignKey('Product',related_name='cartitems')
#     product = models.ManyToManyField(Product, on_delete=models.CASCADE, null=True)
#     price = models.FloatField(default=0)
#     total_items = models.IntegerField(default=0)
#     quantity = models.IntegerField(default=1)

#     def __str__(self):
#         return str(self.product.name)



# # @receiver(pre_save, sender=CartItems)
# # def correct_price(sender, **kwargs):
# #     cart_items = kwargs['instance']
# #     price_of_product = Product.objects.get(id=cart_items.product.id)
# #     cart_items.price = cart_items.quantity * float(price_of_product.price)
# #     total_cart_items = CartItems.objects.filter(user = cart_items.user )
# #     # cart = Cart.objects.get(id = cart_items.cart.id)
# #     # cart.total_price = cart_items.price
# #     # cart.save()
# #     cart_items.total_items = len(total_cart_items)