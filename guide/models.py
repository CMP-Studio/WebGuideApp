from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Exhibition(models.Model):
    uuid                    = models.UUIDField(primary_key=True)
    created_at              = models.DateTimeField()
    updated_at              = models.DateTimeField()
    deleted_at              = models.DateTimeField()
    title                   = models.CharField(max_length=255)
    subtitle                = models.CharField(max_length=255)
    is_live                 = models.BooleanField()
    position                = models.IntegerField()
    sponsor                 = models.CharField(max_length=255)
    bg_iphone_updated_at    = models.DateTimeField()
    bg_ipad_updated_at      = models.DateTimeField()
    bg_iphone_file_size     = models.IntegerField()
    bg_ipad_file_size       = models.IntegerField()
    bg_iphone_normal        = models.URLField()
    bg_iphone_retina        = models.URLField()
    bg_ipad_normal          = models.URLField()
    bg_ipad_retina          = models.URLField()


class Artist(models.Model):
    uuid            = models.UUIDField(primary_key=True)
    created_at      = models.DateTimeField()
    updated_at      = models.DateTimeField()
    deleted_at      = models.DateTimeField()
    first_name      = models.CharField(max_length=255)
    last_name       = models.CharField(max_length=255)
    country         = models.CharField(max_length=20)
    bio             = models.TextField()
    code            = models.CharField(max_length=40)
    exhibition_uuid = models.ForeignKey('Exhibition', on_delete=models.CASCADE)

class Location(models.Model):
    uuid            = models.UUIDField(primary_key=True)
    created_at      = models.DateTimeField()
    updated_at      = models.DateTimeField()
    deleted_at      = models.DateTimeField()
    name            = models.CharField(max_length=255)

class Category(models.Model):
    uuid            = models.UUIDField(primary_key=True)
    created_at      = models.DateTimeField()
    updated_at      = models.DateTimeField()
    deleted_at      = models.DateTimeField()
    title           = models.CharField(max_length=255)

class Artwork(models.Model):
    uuid            = models.UUIDField(primary_key=True)
    created_at      = models.DateTimeField()
    updated_at      = models.DateTimeField()
    deleted_at      = models.DateTimeField()
    title           = models.CharField(max_length=255)
    code            = models.CharField(max_length=40)
    body            = models.TextField()
    share_url       = models.URLField()
    exhibition_uuid = models.ForeignKey('Exhibition', on_delete=models.CASCADE)
    location_uuid   = models.ForeignKey('Location', on_delete=models.CASCADE)
    category_uuid   = models.ForeignKey('Category', on_delete=models.CASCADE)
