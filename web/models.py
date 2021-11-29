from django.db import models
from django.db.models.base import Model
from django.utils.text import slugify
from tinymce.models import HTMLField
from easy_thumbnails.fields import ThumbnailerImageField

TF1 = '0'
TF2 = '1'
TF3 = '2'
TF4 = '3'
TF5 = '4'
TF6 = '5'
TF7 = '6'
TF8 = '7'
TF9 = '8'

KATEGORI_CHOICES = (
        (TF1,'TF1 - Open Trade and Sustainable Investment'),
        (TF2,'TF2 - Meaningful Digital Connectivity, Cyber Security, Empowerment'),
        (TF3,'TF3 - Governing Climate Target, Energy Transition and Environmental Protection'),
        (TF4,'TF4 - Food Security and Sustainable Agriculture'),
        (TF5,'TF5 - Inequality, Human Capital, and Well-being'),
        (TF6,'TF6 - Global Health Security and COVID-19'),
        (TF7,'TF7 - International Finance and Economic Recovery'),
        (TF8,'TF8 - Resilient Infrastructure and Financing'),
        (TF9,'TF9 - Global Cooperation for SDGs Financing'),
    )

class author(models.Model):
    nama = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=50, blank=True, null=True)
    organisasi = models.CharField(max_length=50, blank=True, null=True)
    foto = models.ImageField(upload_to = 'author/', blank=True, null=True)
    biodata = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = ("Author")
        verbose_name_plural = ("Authors")

class event(models.Model):
    judul = models.CharField(max_length=50)
    slug = models.SlugField(default='', editable=False, max_length=140)
    mulai = models.DateTimeField()
    selesai = models.DateTimeField(blank=True)
    description = HTMLField()
    gambar = ThumbnailerImageField(upload_to='photos', blank=True)
    link_video = models.URLField(blank=True)
    link_pendaftaran = models.URLField(blank=True)
    keterangan = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.judul
    
    def save(self, *args, **kwargs):
        value = self.judul
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = ("Event")
        verbose_name_plural = ("Events")
        
    @property
    def mli(self):
        return self.mulai.strftime('%d %B %Y')

class publications (models.Model):
    judul = models.CharField(max_length=50)
    slug = models.SlugField(default='', editable=False, max_length=140)
    author = models.ManyToManyField(author)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    kategori = models.CharField(max_length=2, choices=KATEGORI_CHOICES)
    description = HTMLField()
    image = models.ImageField(upload_to='event/', blank=True)
    dokumen = models.FileField(upload_to='publications', blank=True)
    keterangan = models.TextField(blank=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.judul
    
    def save(self, *args, **kwargs):
        value = self.judul
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = ("Publication")
        verbose_name_plural = ("Publications")
        
class berita(models.Model):
    judul = models.CharField(max_length=50)
    slug = models.SlugField(default='', editable=False, max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = HTMLField()
    image = ThumbnailerImageField(upload_to='berita', blank=True)
    link_video = models.URLField(blank=True)
    dokumen = models.FileField(upload_to = 'berita/', blank=True)
    keterangan = models.TextField(blank=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.judul
    
    def save(self, *args, **kwargs):
        value = self.judul
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = ("News")
        verbose_name_plural = ("News")
        
    @property
    def mli(self):
        return self.created_at.strftime('%d %B %Y')

class FAQ(models.Model):
    judul = models.CharField(max_length=150)
    isi = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.judul

class TaskForces(models.Model):
    TF = models.CharField(max_length=2, choices=KATEGORI_CHOICES)
    lead = models.OneToOneField(author, related_name='+', on_delete=models.CASCADE)
    cochairs = models.ManyToManyField(author)
    coordinator = models.OneToOneField(author, related_name='+', on_delete=models.CASCADE)
    policyarea = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.TF)