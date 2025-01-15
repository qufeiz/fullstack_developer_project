# from django.contrib import admin
# from .models import related models
from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.

# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel  # Specify the model to inline
    extra = 1  # Number of extra blank rows for adding new CarModels

# CarModelAdmin class
@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'year', 'car_make')  # Fields displayed in the CarModel list view
    list_filter = ('type', 'year', 'car_make')  # Add filters for type, year, and car make


# CarMakeAdmin class with CarModelInline
@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]  # Add CarModelInline to CarMake admin
    list_display = ('name', 'description')  # Fields displayed in the CarMake list view


# Register models here
