from django.db import models


class Category(models.Model):
	category_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=25)
	last_update = models.DateTimeField()

	class Meta:
		app_label = 'api'
		db_table = "category"
