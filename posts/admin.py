from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Post, Topic
class ListAdminMixin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

class PostCreateForm(SummernoteModelAdmin, ListAdminMixin):
    pass
admin.site.register(Topic)
admin.site.register(Post, PostCreateForm)

