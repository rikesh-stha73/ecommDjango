from django.contrib import admin
from core.models import Product, Category, Vendor, CartOrder, Wishlist, CartOrderItems, ProductImages, ProductReview, Address


class ProductsImagesAdmin(admin.TabularInline):
    model = ProductImages  # Add the model attribute here

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductsImagesAdmin]
    list_display = ['user', 'title', 'product_image', 'price', 'featured', 'product_status']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']

class VendoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'vendor_image']

class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'paid_status', 'order_date', 'product_status']

class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'invoice_no', 'item', 'image', 'qty', 'price', 'total']

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating']

class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date']

class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'mobile', 'status']  # Update 'address' to 'mobile' or any other valid attribute or method on the Address model


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendoryAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Address, AddressAdmin)
