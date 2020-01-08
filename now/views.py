from django.shortcuts import render

def acknowledgements(request):
    """
    View function for acknowledgements page of site.
    """
    return render(
        request,
        'acknowledgements.html',
    )

def browsing_lists(request):
    """
    View function for Browsing - Lists page of site.
    """
    return render(
        request,
        'browsing_lists.html',
    )

def board(request):
    """
    View function for board page of site.
    """
    return render(
        request,
        'board.html',
    )

def contact(request):
    """
    View function for contact page of site.
    """
    return render(
        request,
        'contact.html',
    )

def conventions(request):
    """
    View function for conventions page of site.
    """
    return render(
        request,
        'conventions.html',
    )

def database(request):
    """
    View function for database page of site.
    """
    return render(
        request,
        'database.html',
    )

def ecometrics(request):
    """
    View function for ecometrics page of site.
    """
    return render(
        request,
        'ecometrics.html',
    )

def export_maps(request):
    """
    View function for export_maps page of site.
    """
    return render(
        request,
        'export_maps.html',
    )

def faq(request):
    """
    View function for FAQ page of site.
    """
    return render(
        request,
        'faq.html',
    )

def field_archive(request):
    """
    View function for field_archive page of site.
    """
    return render(
        request,
        'field_archive.html',
    )

def index(request):
    """
    View function for home page of site.
    """

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
    )

def links(request):
    """
    View function for links page of site.
    """
    return render(
        request,
        'links.html',
    )

def news(request):
    """
    View function for News page of site.
    """
    return render(
        request,
        'news.html',
    )

def note(request):
    """
    View function for note page of site.
    """
    return render(
        request,
        'note.html',
    )

def publications(request):
    """
    View function for publications page of site.
    """
    return render(
        request,
        'publications.html',
    )
