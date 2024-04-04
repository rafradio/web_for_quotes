from django.db import models

class TestQuotas(models.Model):
    link = models.PositiveIntegerField()
    title = models.CharField(max_length=250, db_collation='utf8_unicode_ci', blank=True, null=True)
    prj_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'test_quotas'