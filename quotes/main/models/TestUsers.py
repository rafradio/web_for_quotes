from django.db import models


class TestUsers(models.Model):
    name = models.CharField(max_length=250, db_collation='utf8_unicode_ci', blank=True, null=True)
    email = models.CharField(max_length=250, db_collation='utf8_unicode_ci', blank=True, null=True)
    password = models.CharField(max_length=50, db_collation='utf8_unicode_ci', blank=True, null=True)
    role = models.PositiveIntegerField(blank=True, null=True)
    ban = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'test_users'
