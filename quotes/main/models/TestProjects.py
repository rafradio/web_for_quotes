from django.db import models

class TestProjects(models.Model):
    link = models.CharField(max_length=250, db_collation='utf8_unicode_ci', blank=True, null=True)
    title = models.CharField(max_length=250, db_collation='utf8_unicode_ci', blank=True, null=True)
    ac_gizmo = models.CharField(max_length=12, db_collation='utf8_unicode_ci', blank=True, null=True)
    ban = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'test_projects'
