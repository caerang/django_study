from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    # 명시된 속성에 포스트 항목 리스트 페이지에 표시
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    # 사이드바에 필터로 표시됨
    list_filter = ('status', 'created', 'publish', 'author')
    # 상단에 검색 항목 표시됨
    search_fields = ('title', 'body')

    prepopulated_fields = {'slug': ('title',)}

    raw_id_fields = ('author',)
    # 날짜별 검색이 가능한 필드 추가 됨
    date_hierarchy = 'publish'
    
    ordering = ['status', 'publish']

admin.site.register(Post, PostAdmin)
