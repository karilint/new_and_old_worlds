from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('acknowledgements/', views.acknowledgements, name='acknowledgements'),
    path('board/', views.board, name='board'),
    path('contact/', views.contact, name='contact'),
    path('wiki/', views.wiki, name='wiki'),
    path('database/', views.database, name='database'),
    path('ecometrics/', views.ecometrics, name='ecometrics'),
    path('faq/', views.faq, name='faq'),
    path('field_archive/', views.field_archive, name='field_archive'),
    path('links/', views.links, name='links'),
    path('news/', views.news, name='news'),
    path('note/', views.note, name='note'),
    path('publications/', views.publications, name='publications'),
]
