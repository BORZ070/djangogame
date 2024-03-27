from django.contrib import admin

from order.models import OrderNumber, OrderItem


class ItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(OrderItem)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'user', 'game']


@admin.register(OrderNumber)
class ModelNameAdmin(admin.ModelAdmin):
     list_display = ['id', 'user']
     inlines = [ItemInline]


