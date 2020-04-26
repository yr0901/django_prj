from django.contrib import admin
from .models import Review
# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display=('title','movie_title','rank','content')

admin.site.register(Review, ReviewAdmin)