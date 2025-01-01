from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)

    
@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('test1', 'test2','test4','test5','test6','test7','test8','test9')
    
    
admin.site.register(Testrelation1)
@admin.register(Testrelation2)
class Testrelation2Admin(admin.ModelAdmin):
    list_display = ('testrelation2','testrelation3')
    
    
admin.site.register(Testrelation3)
@admin.register(Testrelation4)
class Testrelation4Admin(admin.ModelAdmin):
    list_display = ('testrelation5', 'testrelation6')
    
admin.site.register(Testrelation5)
admin.site.register(Testrelation6)
# class Testrelation6Admin(admin.ModelAdmin):
#     list_display = ('testrelation8', 'testrelation9')
admin.site.register(Testmedia)
