from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'modified_date', 'created_date')
    # fields = ('title', 'content', 'modified_date', 'created_date')
    readonly_fields = ('created_date', 'modified_date')
    list_filter = ('created_date', 'modified_date')
    date_hierarchy = 'created_date'
    list_display_links = ('id',)
    # list_editable = ('title', )
    search_fields = ('title',)
    list_per_page = 25
    ordering = ('-id',)
    # save_on_top = True
    # actions_on_bottom = True
    # actions_selection_counter = False
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Article, ArticleAdmin)


