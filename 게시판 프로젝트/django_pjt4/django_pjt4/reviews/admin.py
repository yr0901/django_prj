from django.contrib import admin
from .models import Review, Movie, Comment
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'content']

admin.site.register(Review, ReviewAdmin)

class MoviewAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'director']
admin.site.register(Movie, MoviewAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=['id', 'content']
admin.site.register(Comment, CommentAdmin)