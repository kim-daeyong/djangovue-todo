from django.contrib import admin

# Register your models here.
from todo.models import Todo

#등록할때 사용하는 간편한 데코
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):

    #admin 사이트에서 보여줄 컬럼들
    list_display = ('id','name', 'todo')
