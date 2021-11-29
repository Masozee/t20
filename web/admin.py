from django.contrib import admin
from .models import *

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('judul', 'mulai', 'selesai', 'publish')
    search_fields = ['judul']
admin.site.register(event, EventAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('nama', 'jabatan', 'organisasi', )
    search_fields = ['nama', 'organisasi', 'jabatan']
admin.site.register(author, AuthorAdmin)

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('judul', 'kategori', 'publish' )
    search_fields = ['judul', 'author', 'kategori']
admin.site.register(publications, PublicationAdmin)

class BeritaAdmin(admin.ModelAdmin):
    list_display = ('judul', 'created_at', 'updated_at', 'publish'  )
    search_fields = ['judul']
admin.site.register(berita, BeritaAdmin)