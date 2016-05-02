from django.contrib import admin
from .models import Location, Category, Exhibition, Tour, Artist, Link, Artwork, Media, artistArtwork, tourArtwork

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Exhibition)
admin.site.register(Tour)
admin.site.register(Artist)
admin.site.register(Link)
admin.site.register(Artwork)
admin.site.register(Media)
admin.site.register(artistArtwork)
admin.site.register(tourArtwork)
