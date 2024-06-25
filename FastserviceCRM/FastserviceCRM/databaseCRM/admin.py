from django.contrib import admin
from django.utils.safestring import mark_safe


from .models import Company, Workshop, Order, CustomerOrder, devices, StatusOrder, TypeOrder, Employees, Positions, Brand


@admin.register(Company)
class Company(admin.ModelAdmin):
    list_display = ('companyName', 'image2', 'phone', 'address', 'email', 'site')
    # list_filter = ('id', 'companyName', 'phone', 'address', 'email', 'site')
    # search_fields = ('id', 'companyName', 'phone', 'address', 'email', 'site')

    readonly_fields = ["image", "image2"]


    def image(self, obj):
        return mark_safe(f'<img width="200px" src="{obj.logo.url}">')

    def image2(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.logo.url}">')



@admin.register(StatusOrder)
class StatusOrder(admin.ModelAdmin):
    list_display = ('id', 'nameStatus', 'status', 'descriptionStatus')
    # list_filter = ('id', 'companyName', 'phone', 'address', 'email', 'site')
    # search_fields = ('id', 'companyName', 'phone', 'address', 'email', 'site')
    list_display_links = ('id', 'nameStatus')

    readonly_fields = ["status"]


    def status(self, obj):
        return mark_safe(f'<div style="padding: 10px; color: white; display: inline-block; background-color: {obj.colorStatus}; border-radius: 5px;">{obj.nameStatus}<div>')



@admin.register(Workshop)
class Workshop(admin.ModelAdmin):
    list_display = ('company', 'workshopName', 'Color', 'address', 'phone', 'email')
    # list_filter = ('id', 'address', 'phone', 'email')
    # search_fields = ('id', 'address', 'phone', 'email')
    readonly_fields = ["Color"]

    def Color(self, obj):
        return mark_safe(f'<div style="height: 20px; width: 20px; background-color: {obj.WorkShopColor}; border-radius: 50%;"><div>')

    Color.short_description = "Цвет мастерской"




@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ('id', 'dateCreate', 'workShop', 'brand', 'modelDevice', 'malfunction', 'manager', 'master', 'estimatedСost')
    # list_filter = ('id', 'address', 'phone', 'email')
    # search_fields = ('id', 'address', 'phone', 'email')


@admin.register(CustomerOrder)
class CustomerOrder(admin.ModelAdmin):
    list_display = ('id', 'fio', 'phone', 'address')
    # list_filter = ('id', 'address', 'phone', 'email')
    # search_fields = ('id', 'address', 'phone', 'email')




@admin.register(devices)
class devices(admin.ModelAdmin):
    list_display = ('id', 'device')
    # list_filter = ('id', 'address', 'phone', 'email')
    # search_fields = ('id', 'address', 'phone', 'email')
# Register your models here.


@admin.register(TypeOrder)
class TypeOrder(admin.ModelAdmin):
    list_display = ('id', 'typeOrder', 'descriptionTypeOrder')
    # list_filter = ('id', 'address', 'phone', 'email')
    # search_fields = ('id', 'address', 'phone', 'email')
# Register your models here.


@admin.register(Employees)
class Employees(admin.ModelAdmin):
    list_display = ('nameEmployees', 'phone', 'email', 'address', 'positions', 'fotoTable')
    # list_filter = ('id', 'address', 'phone', 'email')
    # search_fields = ('id', 'address', 'phone', 'email')



    readonly_fields = ["foto", "fotoTable"]
    def foto(self, obj):
        return mark_safe(f'<img width="200px" src="{obj.photo.url}">')

    def fotoTable(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.photo.url}">')

    foto.short_description = "Фотография"


@admin.register(Positions)
class Positions(admin.ModelAdmin):
    list_display = ('id', 'namePosition')
    # list_filter = ('id', 'address', 'phone', 'email')
    # search_fields = ('id', 'address', 'phone', 'email')


@admin.register(Brand)
class Brand(admin.ModelAdmin):
    list_display = ('id', 'nameBrand')
    # list_filter = ('id', 'address', 'phone', 'email')
    # search_fields = ('id', 'address', 'phone', 'email')