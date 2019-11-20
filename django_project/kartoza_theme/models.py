from django.db import models
from django.db.models import CharField, TextField, FileField


class ProductViewData(models.Model):
    category_summary = CharField("Category Page Summary", max_length=255)
    category_html = TextField("Category Page HTML")

