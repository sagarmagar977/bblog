from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget

#https://www.tiny.cloud/docs/quick-start/


class catagoryAdmin(admin.ModelAdmin):
    list_display=('img_tag','title','description','url')
    search_fields=('title',)
    list_per_page=10


class postAdmin(admin.ModelAdmin):
    list_display=('img_tag','title','url')
    search_fields=('title',)
    list_filter=('cat',)
    list_per_page=10

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }



   
    # class Media:
    #     js=('https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js','js/script.js')



admin.site.register(catagory,catagoryAdmin)
admin.site.register(post,postAdmin)
# Register your models here.
