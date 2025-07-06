from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.html import format_html
from .models import *

admin.site.unregister(Group)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['phone_number', 'first_name', 'last_name', 'role', 'district', 'balance', 'is_active',
                    'date_joined']
    list_filter = ['role', 'is_active', 'is_staff', 'district__region', 'district']
    search_fields = ['phone_number', 'first_name', 'last_name']
    ordering = ['-date_joined']
    readonly_fields = ['date_joined', 'last_login']

    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'district', 'address', 'telegram_id', 'about')}),
        ('Financial', {'fields': ('balance',)}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2', 'role'),
        }),
    )


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'order_count']
    search_fields = ['name']
    list_editable = ['order_count']
    ordering = ['name']


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'region']
    list_filter = ['region']
    search_fields = ['name', 'region__name']
    ordering = ['region__name', 'name']




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']
    readonly_fields = ['slug']




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'discount', 'seller_price', 'quantity']
    list_filter = ['category', 'discount']
    search_fields = ['name', 'description']
    readonly_fields = ['slug']
    list_editable = ['price', 'discount', 'quantity']


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'created_at']
    list_filter = ['created_at', 'product__category']
    search_fields = ['user__phone_number', 'user__first_name', 'product__name']
    ordering = ['-created_at']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'phone_number', 'product', 'status', 'quantity', 'total', 'district',
                    'created_at']
    list_filter = ['status', 'district__region', 'district', 'created_at', 'deliver_time']
    search_fields = ['first_name', 'phone_number', 'product__name']
    list_editable = ['status']
    ordering = ['-created_at']
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Customer Info', {
            'fields': ('first_name', 'phone_number', 'district')
        }),
        ('Order Details', {
            'fields': ('product', 'quantity', 'total', 'comment')
        }),
        ('Management', {
            'fields': ('owner', 'operator', 'thread', 'status', 'deliver_time')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ['created_at', 'updated_at']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('product', 'district', 'owner', 'operator')


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'product', 'discount_price', 'visit_count', 'created_at']
    list_filter = ['created_at', 'product__category']
    search_fields = ['name', 'owner__phone_number', 'product__name']
    ordering = ['-created_at']
    readonly_fields = ['visit_count']


@admin.register(AdminSetting)
class AdminSettingAdmin(admin.ModelAdmin):
    list_display = ['deliver_price', 'start_competition', 'end_competition']

    fieldsets = (
        ('Delivery Settings', {
            'fields': ('deliver_price',)
        }),
        ('Competition Settings', {
            'fields': ('competition_thumbnail_img', 'competition_description', 'start_competition', 'end_competition')
        }),
    )



@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['card_number', 'owner', 'pay_amount', 'pay_status', 'created_at']
    list_filter = ['pay_status', 'created_at']
    search_fields = ['card_number', 'owner__phone_number', 'owner__first_name']
    list_editable = ['pay_status']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'update_at']



# Admin site customization
admin.site.site_header = "Admin Panel"
admin.site.site_title = "Admin"
admin.site.index_title = "Boshqaruv Paneli"