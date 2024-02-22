from django.shortcuts import render
import os.path, time
from new_and_old_worlds.settings import BASE_DIR

from django.conf import settings
from django.urls import resolve
import os, time
from django.template.response import TemplateResponse

# add_mod_date:
# Use a decorator for displaying the last modification date of the template file (html)
# https://community.simpleisbetterthancomplex.com/t/displaying-the-last-modification-date-of-the-template-file/952/4

def add_mod_date(template):
    def outer_wrapper(func):
        def wrapper(request, *args, **kwargs):
           template_path = os.path.join(settings.BASE_DIR, resolve(request.path).app_name, settings.TEMPLATE_URL, template)
           r = func(request, *args, **kwargs)
           r.context_data = {"last_modified": time.ctime(os.path.getmtime(template_path))}
           return r.render()
        return wrapper
    return outer_wrapper

#def acknowledgements(request):
#    """
#    View function for acknowledgements page of site.
#    """
#    return render(
#        request,
#        'acknowledgements.html',
#    )

@add_mod_date("acknowledgements.html")
def acknowledgements(request):
    return TemplateResponse(request, "acknowledgements.html")

@add_mod_date("browsing_details.html")
def browsing_details(request):
    return TemplateResponse(request, "browsing_details.html")

@add_mod_date("browsing_lists.html")
def browsing_lists(request):
    return TemplateResponse(request, "browsing_lists.html")

@add_mod_date("board.html")
def board(request):
    return TemplateResponse(request, "board.html")

@add_mod_date("contact.html")
def contact(request):
    return TemplateResponse(request, "contact.html")

@add_mod_date("conventions.html")
def conventions(request):
    return TemplateResponse(request, "conventions.html")

@add_mod_date("database.html")
def database(request):
    return TemplateResponse(request, "database.html")

@add_mod_date("data_entry_practices.html")
def data_entry_practices(request):
    return TemplateResponse(request, "data_entry_practices.html")

@add_mod_date("ecometrics.html")
def ecometrics(request):
    return TemplateResponse(request, "ecometrics.html")

@add_mod_date("export_maps.html")
def export_maps(request):
    return TemplateResponse(request, "export_maps.html")

@add_mod_date("faq.html")
def faq(request):
    return TemplateResponse(request, "faq.html")

@add_mod_date("field_archive.html")
def field_archive(request):
    return TemplateResponse(request, "field_archive.html")

@add_mod_date("index.html")
def index(request):
    return TemplateResponse(request, "index.html")

@add_mod_date("index.html")
def database(request):
    return TemplateResponse(request, "index.html")

@add_mod_date("links.html")
def links(request):
    return TemplateResponse(request, "links.html")

@add_mod_date("locality_notes.html")
def locality_notes(request):
    return TemplateResponse(request, "locality_notes.html")

@add_mod_date("news.html")
def news(request):
    return TemplateResponse(request, "news.html")

@add_mod_date("note.html")
def note(request):
    return TemplateResponse(request, "note.html")

@add_mod_date("publications.html")
def publications(request):
    return TemplateResponse(request, "publications.html")

@add_mod_date("species_at_localities.html")
def species_at_localities(request):
    return TemplateResponse(request, "species_at_localities.html")

@add_mod_date("species_notes.html")
def species_notes(request):
    return TemplateResponse(request, "species_notes.html")

@add_mod_date("taxonomy.html")
def taxonomy(request):
    return TemplateResponse(request, "taxonomy.html")

@add_mod_date("wiki.html")
def wiki(request):
    return TemplateResponse(request, "wiki.html")
