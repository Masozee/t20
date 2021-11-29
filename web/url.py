from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.urls import include

from web import views as webviews

urlpatterns = [
    path('', webviews.home, name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('task-forces/', TemplateView.as_view(template_name='index.html'), name='task-forces'),
    path('task-forces/TF-1', TemplateView.as_view(template_name='index.html'), name='tf-1'),
    path('task-forces/TF-2', TemplateView.as_view(template_name='index.html'), name='tf-2'),
    path('task-forces/TF-3', TemplateView.as_view(template_name='index.html'), name='tf-3'),
    path('task-forces/TF-4', TemplateView.as_view(template_name='index.html'), name='tf-4'),
    path('task-forces/TF-5', TemplateView.as_view(template_name='index.html'), name='tf-5'),
    path('task-forces/TF-6', TemplateView.as_view(template_name='index.html'), name='tf-6'),
    path('task-forces/TF-7', TemplateView.as_view(template_name='index.html'), name='tf-7'),
    path('task-forces/TF-8', TemplateView.as_view(template_name='index.html'), name='tf-8'),
    path('task-forces/TF-9', TemplateView.as_view(template_name='index.html'), name='tf-9'),
    path('events/', webviews.Acara, name='events'),
    path('events/details/', TemplateView.as_view(template_name='eventdetail.html'), name='events-details'),
    path('publications/', TemplateView.as_view(template_name='publicationlist.html'), name='publications'),
    path('publications/detail/', TemplateView.as_view(template_name='publicationdetail.html'), name='publication-detail'),
    path('media/', TemplateView.as_view(template_name='index.html'), name='media'),
    path('media/detail', TemplateView.as_view(template_name='index.html'), name='media-detail'),
    path('news/', TemplateView.as_view(template_name='news.html'), name='news'),
    path('news/detail/', TemplateView.as_view(template_name='publicationdetail.html'), name='news-detail'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('faq/', TemplateView.as_view(template_name='index.html'), name='faq'),
    path('privacy-policy/', TemplateView.as_view(template_name='index.html'), name='privacy-policy'),
    
]