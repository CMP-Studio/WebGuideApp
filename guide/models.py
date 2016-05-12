from __future__ import unicode_literals

from django.utils.text import slugify
from django.db import models

#Hours table
class Hour(models.Model):
    dow_i           = models.IntegerField(null=True, blank=True)
    dow             = models.CharField(max_length=30, null=True, blank=True)
    day_open        = models.TimeField(null=True, blank=True)
    day_close       = models.TimeField(null=True, blank=True)

# Sync tables.
class Location(models.Model):
    uuid            = models.UUIDField(primary_key=True)
    created_at      = models.DateTimeField(null=True, blank=True)
    updated_at      = models.DateTimeField(null=True, blank=True)
    deleted_at      = models.DateTimeField(null=True, blank=True)
    name            = models.CharField(max_length=255, null=True, blank=True)

class Category(models.Model):
    uuid            = models.UUIDField(primary_key=True)
    created_at      = models.DateTimeField(null=True, blank=True)
    updated_at      = models.DateTimeField(null=True, blank=True)
    deleted_at      = models.DateTimeField(null=True, blank=True)
    title           = models.CharField(max_length=255)

    slug            =models.SlugField(max_length=255, null=True, blank=True)

class Exhibition(models.Model):
    uuid                    = models.UUIDField(primary_key=True)
    created_at              = models.DateTimeField(null=True, blank=True)
    updated_at              = models.DateTimeField(null=True, blank=True)
    deleted_at              = models.DateTimeField(null=True, blank=True)
    title                   = models.CharField(max_length=255, null=True, blank=True)
    subtitle                = models.CharField(max_length=255, null=True, blank=True)
    is_live                 = models.BooleanField(default=False)
    position                = models.IntegerField(null=True, blank=True)
    sponsor                 = models.CharField(max_length=255, null=True, blank=True)
    bg_iphone_updated_at    = models.DateTimeField(null=True, blank=True)
    bg_ipad_updated_at      = models.DateTimeField(null=True, blank=True)
    bg_iphone_file_size     = models.IntegerField(null=True, blank=True)
    bg_ipad_file_size       = models.IntegerField(null=True, blank=True)
    bg_iphone_normal        = models.URLField(null=True, blank=True)
    bg_iphone_retina        = models.URLField(null=True, blank=True)
    bg_ipad_normal          = models.URLField(null=True, blank=True)
    bg_ipad_retina          = models.URLField(null=True, blank=True)

    slug                    =models.SlugField(max_length=255, null=True, blank=True)

class Tour(models.Model):
    uuid            = models.UUIDField(primary_key=True)
    created_at      = models.DateTimeField(null=True, blank=True)
    updated_at      = models.DateTimeField(null=True, blank=True)
    deleted_at      = models.DateTimeField(null=True, blank=True)
    title           = models.CharField(max_length=255)
    subtitle        = models.CharField(max_length=255)
    body            = models.TextField(null=True, blank=True)
    exhibition      = models.ForeignKey('Exhibition', on_delete=models.CASCADE, db_column='exhibition_uuid')
    artwork         = models.ManyToManyField('Artwork', through='tourArtwork')

    slug            =models.SlugField(max_length=255, null=True, blank=True)

class Artist(models.Model):
    uuid            = models.UUIDField(primary_key=True)
    created_at      = models.DateTimeField(null=True, blank=True)
    updated_at      = models.DateTimeField(null=True, blank=True)
    deleted_at      = models.DateTimeField(null=True, blank=True)
    first_name      = models.CharField(max_length=255)
    last_name       = models.CharField(max_length=255)
    country         = models.CharField(max_length=20)
    bio             = models.TextField(null=True, blank=True)
    code            = models.CharField(max_length=40)
    exhibition      = models.ForeignKey('Exhibition', on_delete=models.CASCADE, db_column='exhibition_uuid')
    artwork         = models.ManyToManyField('Artwork', through='artistArtwork')

    slug            =models.SlugField(max_length=255, null=True, blank=True)

class Link(models.Model):
    uuid                = models.UUIDField(primary_key=True)
    created_at          = models.DateTimeField(null=True, blank=True)
    updated_at          = models.DateTimeField(null=True, blank=True)
    deleted_at          = models.DateTimeField(null=True, blank=True)
    title               = models.CharField(max_length=255)
    url                 = models.URLField(null=True, blank=True)
    exhibition          = models.ForeignKey('Exhibition', on_delete=models.CASCADE, db_column='exhibition_uuid')
    artist              = models.ForeignKey('Artist', on_delete=models.CASCADE, db_column='artist_uuid')

class Artwork(models.Model):
    uuid                = models.UUIDField(primary_key=True)
    created_at          = models.DateTimeField(null=True, blank=True)
    updated_at          = models.DateTimeField(null=True, blank=True)
    deleted_at          = models.DateTimeField(null=True, blank=True)
    title               = models.CharField(max_length=255)
    code                = models.CharField(max_length=40)
    body                = models.TextField(null=True, blank=True)
    share_url           = models.URLField(null=True, blank=True)
    exhibition          = models.ForeignKey('Exhibition', on_delete=models.CASCADE, db_column='exhibition_uuid')
    location            = models.ForeignKey('Location', on_delete=models.CASCADE, db_column='location_uuid')
    category            = models.ForeignKey('Category', on_delete=models.CASCADE, db_column='category_uuid')

    body_html           = models.TextField(null=True, blank=True)
    slug                =models.SlugField(max_length=255, null=True, blank=True)

class Media(models.Model):
    uuid            = models.UUIDField(primary_key=True)
    created_at      = models.DateTimeField(null=True, blank=True)
    updated_at      = models.DateTimeField(null=True, blank=True)
    deleted_at      = models.DateTimeField(null=True, blank=True)
    title           = models.CharField(max_length=255)
    kind            = models.CharField(max_length=255)
    width           = models.IntegerField(null=True, blank=True)
    height          = models.IntegerField(null=True, blank=True)
    position        = models.IntegerField(null=True, blank=True)
    alt             = models.CharField(max_length=255, null=True, blank=True)
    exhibition      = models.ForeignKey('Exhibition', on_delete=models.CASCADE, db_column='exhibition_uuid')
    artwork         = models.ForeignKey('Artwork', on_delete=models.CASCADE, db_column='artwork_uuid')
    urlThumb        = models.URLField(null=True, blank=True)
    urlSmall        = models.URLField(null=True, blank=True)
    urlMedium       = models.URLField(null=True, blank=True)
    urlLarge        = models.URLField(null=True, blank=True)
    urlFull         = models.URLField(null=True, blank=True)

class artistArtwork(models.Model):
    uuid            = models.UUIDField(primary_key=True)
    created_at      = models.DateTimeField(null=True, blank=True)
    updated_at      = models.DateTimeField(null=True, blank=True)
    deleted_at      = models.DateTimeField(null=True, blank=True)
    exhibition      = models.ForeignKey('Exhibition', on_delete=models.CASCADE, db_column='exhibition_uuid')
    artist          = models.ForeignKey('Artist', on_delete=models.CASCADE, db_column='artist_uuid')
    artwork         = models.ForeignKey('Artwork', on_delete=models.CASCADE, db_column='artwork_uuid')

class tourArtwork(models.Model):
    uuid            = models.UUIDField(primary_key=True)
    created_at      = models.DateTimeField(null=True, blank=True)
    updated_at      = models.DateTimeField(null=True, blank=True)
    deleted_at      = models.DateTimeField(null=True, blank=True)
    position        = models.IntegerField(null=True, blank=True)
    exhibition      = models.ForeignKey('Exhibition', on_delete=models.CASCADE, db_column='exhibition_uuid')
    tour            = models.ForeignKey('Tour', on_delete=models.CASCADE, db_column='tour_uuid')
    artwork         = models.ForeignKey('Artwork', on_delete=models.CASCADE, db_column='artwork_uuid')

#Updates - only used for debugging updates

class Update(models.Model):
    updated_at     = models.DateTimeField(auto_now_add=True)
    descrip        = models.CharField(max_length=255, null=True, blank=True)
    success        = models.BooleanField(default=False)
