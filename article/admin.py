from django.contrib import admin
from article.models import Article, Comments
from DBase.models import DBase

# Register your models here.
class ArticleInline(admin.StackedInline):
	model = Comments
	extra = 2

class ArticleAdmin(admin.ModelAdmin):
	fields = ['article_first_name', 'article_second_name', 'article_third_name', 'article_pasport_number', 'article_birthdate', 'article_sex', 'article_other']
	inlines = [ArticleInline]
	list_filter = ['article_birthdate','article_first_name', 'article_second_name']
	list_display = ['article_first_name', 'article_second_name', 'article_third_name', 'article_pasport_number', 'article_birthdate', 'article_sex', 'article_other']

admin.site.register(Article, ArticleAdmin)
admin.site.register(DBase)