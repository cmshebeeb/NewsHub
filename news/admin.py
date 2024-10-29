from django.contrib import admin
from .models import Article, UserPreferences, Query
from django.utils.html import format_html
from django.urls import reverse


class QueryInline(admin.TabularInline):
    model = Query
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'show_queries_button')

    def show_queries_button(self, obj):
        return format_html(
            '<a class="button" href="{}">Queries</a>',
            reverse('admin_show_queries', args=[obj.pk])
        )
    show_queries_button.short_description = 'Queries'
    show_queries_button.allow_tags = True
    inlines = [QueryInline]

admin.site.register(Article, ArticleAdmin)
admin.site.register(UserPreferences)
admin.site.register(Query)
