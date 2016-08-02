# -*- coding: utf-8 -*-
__author__ = 'macpro'

from django.forms import ModelForm
from models import Comments

class CommentForm(ModelForm):
		class Meta:
			model = Comments
			fields = ['comments_pasport_number', 'comments_takedate', 'comments_other', 'comments_article']