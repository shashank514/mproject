from django.contrib import admin
from .models import Items,Order,OrderItem,TotalOrder,Category,UserOtp,BillingAddress,ProductImage

# Register your models here.

admin.site.register(Items)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(TotalOrder)
admin.site.register(Category)
admin.site.register(UserOtp)
admin.site.register(BillingAddress)
admin.site.register(ProductImage)
