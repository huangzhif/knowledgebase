from django.contrib import admin
from .models import knowledges


# Register your models here.
class knowledgeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')
    list_filter = ('created_date', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',) #设置添加文本时，author是下拉框还是弹出框选择,弹出框显示外键的详细信息
    date_hierarchy = 'created_date'
    ordering = ['-created_date', 'author']


admin.site.register(knowledges,knowledgeAdmin)
