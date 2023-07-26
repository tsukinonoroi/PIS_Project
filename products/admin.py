from django.contrib import admin
from .models import ApartCategory, TypeOfApart, Mebel, Vidovaya, LcdOrSingle, ApartPlan, Apart, ApartmentImage
from django.contrib.auth.models import Group, User

admin.site.site_header = 'Nolabel'
admin.site.site_title = 'Админ панель'
admin.site.index_title = 'Главная'

Group._meta.verbose_name_plural = 'Группы'
User._meta.verbose_name_plural = 'Пользователи'

class ApartmentImageInline(admin.TabularInline):
    model = ApartmentImage
    extra = 1

@admin.register(ApartCategory)
class ApartCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Apart)
class ApartAdmin(admin.ModelAdmin):
    inlines = [ApartmentImageInline]

@admin.register(TypeOfApart)
class TypeOfApartAdmin(admin.ModelAdmin):
    pass

@admin.register(Mebel)
class MebelAdmin(admin.ModelAdmin):
    pass

@admin.register(Vidovaya)
class VidovayaAdmin(admin.ModelAdmin):
    pass

@admin.register(LcdOrSingle)
class LcdOrSingleAdmin(admin.ModelAdmin):
    pass

@admin.register(ApartPlan)
class ApartPlanAdmin(admin.ModelAdmin):
    pass

@admin.register(ApartmentImage)
class ApartmentImageAdmin(admin.ModelAdmin):
    pass
