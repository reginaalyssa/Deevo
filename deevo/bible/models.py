# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class BibleVersionKey(models.Model):
    table = models.TextField()
    abbreviation = models.TextField()
    language = models.TextField()
    version = models.TextField()
    info_text = models.TextField()
    info_url = models.TextField()
    publisher = models.TextField()
    copyright = models.TextField()
    copyright_info = models.TextField()

    def __str__(self):
        return self.version + ' (' + self.abbreviation + ')'

    class Meta:
        managed = False
        db_table = 'bible_version_key'

class KeyEnglish(models.Model):
    n = models.TextField()

    def __str__(self):
        return self.n

    class Meta:
        managed = False
        db_table = 'key_english'


class TAsv(models.Model):
    b = models.IntegerField()
    c = models.IntegerField()
    v = models.IntegerField()
    t = models.TextField()

    def __str__(self):
        return str(self.v)

    class Meta:
        managed = False
        db_table = 't_asv'


class TBbe(models.Model):
    b = models.IntegerField()
    c = models.IntegerField()
    v = models.IntegerField()
    t = models.TextField()

    def __str__(self):
        return str(self.v)

    class Meta:
        managed = False
        db_table = 't_bbe'


class TDby(models.Model):
    b = models.IntegerField()
    c = models.IntegerField()
    v = models.IntegerField()
    t = models.TextField()

    def __str__(self):
        return str(self.v)

    class Meta:
        managed = False
        db_table = 't_dby'


class TKjv(models.Model):
    b = models.IntegerField()
    c = models.IntegerField()
    v = models.IntegerField()
    t = models.TextField()

    def __str__(self):
        return str(self.v)

    class Meta:
        managed = False
        db_table = 't_kjv'


class TWbt(models.Model):
    b = models.IntegerField()
    c = models.IntegerField()
    v = models.IntegerField()
    t = models.TextField()

    def __str__(self):
        return str(self.v)

    class Meta:
        managed = False
        db_table = 't_wbt'


class TWeb(models.Model):
    b = models.IntegerField()
    c = models.IntegerField()
    v = models.IntegerField()
    t = models.TextField()

    def __str__(self):
        return str(self.v)

    class Meta:
        managed = False
        db_table = 't_web'


class TYlt(models.Model):
    b = models.IntegerField()
    c = models.IntegerField()
    v = models.IntegerField()
    t = models.TextField()

    def __str__(self):
        return str(self.v)

    class Meta:
        managed = False
        db_table = 't_ylt'