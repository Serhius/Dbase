# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Article(models.Model):
	class Meta():
		db_table = "article"
	article_first_name = models.CharField(max_length = 20)
	article_second_name = models.CharField(max_length = 20)
	article_third_name = models.CharField(max_length = 20)
	article_pasport_number = models.CharField(max_length = 20)
	article_birthdate = models.DateField()
	article_sex = models.CharField(max_length = 2)
	article_other = models.TextField()

class Comments(models.Model):
	class Meta():
		db_table = "comments"
	comments_pasport_number = models.CharField(max_length = 20)
	comments_takedate = models.DateField()
	comments_other = models.TextField()
	comments_article = models.ForeignKey(Article)
