from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('acknowledgements/', views.acknowledgements, name='acknowledgements'),
    path('browsing_lists/', views.browsing_lists, name='browsing_lists'),
    path('board/', views.board, name='board'),
    path('contact/', views.contact, name='contact'),
    path('conventions/', views.conventions, name='conventions'),
    path('database/', views.database, name='database'),
    path('ecometrics/', views.ecometrics, name='ecometrics'),
    path('export_maps/', views.export_maps, name='export_maps'),
    path('faq/', views.faq, name='faq'),
    path('field_archive/', views.field_archive, name='field_archive'),
    path('links/', views.links, name='links'),
    path('news/', views.news, name='news'),
    path('note/', views.note, name='note'),
    path('publications/', views.publications, name='publications'),
]