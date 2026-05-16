from django.contrib import admin
from .models import Category, MenuItem, TableBooking, SliderImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available')
    list_filter = ('category', 'is_available')

@admin.register(TableBooking)
class TableBookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'booking_date', 'status')
    list_editable = ('status',)

@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')