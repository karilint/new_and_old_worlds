from collections import defaultdict
import os
import time

from django.conf import settings
from django.db.models import Prefetch
from django.template.response import TemplateResponse
from django.urls import resolve

from .models import Alert, BoardAssignment, BoardNode, Publication

# add_mod_date:
# Use a decorator for displaying the last modification date of the template file (html)
# https://community.simpleisbetterthancomplex.com/t/displaying-the-last-modification-date-of-the-template-file/952/4


def add_mod_date(template):
    def outer_wrapper(func):
        def wrapper(request, *args, **kwargs):
           match = resolve(request.path)
           app_name = match.app_name or match.namespace or match.func.__module__.split(".")[0]
           template_path = os.path.join(
               settings.BASE_DIR,
               app_name,
               settings.TEMPLATE_URL,
               template,
           )
           r = func(request, *args, **kwargs)
           context = getattr(r, "context_data", {}) or {}
           context.update(
               {
                   "last_modified": time.ctime(os.path.getmtime(template_path)),
                   "board_nav_roots": _build_board_nav_tree(),
               }
           )
           r.context_data = context
           return r.render()
        return wrapper
    return outer_wrapper


def _attach_children(nodes, child_attr):
    children_by_parent = defaultdict(list)
    for node in nodes:
        node.anchor_id = f"board-node-{node.id}"
        children_by_parent[node.parent_id].append(node)

    for node in nodes:
        setattr(node, child_attr, children_by_parent.get(node.id, []))

    return children_by_parent.get(None, [])


def _annotate_depth(nodes, depth=0):
    for node in nodes:
        node.depth = depth
        _annotate_depth(getattr(node, "prefetched_children", []), depth + 1)


def _limit_tree_depth(nodes, child_attr, max_depth, depth=0):
    for node in nodes:
        children = list(getattr(node, child_attr, []))
        if depth >= max_depth:
            setattr(node, child_attr, [])
            continue
        _limit_tree_depth(children, child_attr, max_depth, depth + 1)


def _group_assignments(node):
    grouped = []
    current_key = object()
    current_group = None

    for assignment in getattr(node, "prefetched_assignments", []):
        role = assignment.role
        key = role.id if role else None
        if key != current_key:
            current_group = {
                "role": role,
                "assignments": [],
            }
            grouped.append(current_group)
            current_key = key
        current_group["assignments"].append(assignment)

    node.assignment_groups = grouped


def _build_board_nav_tree():
    nodes = list(BoardNode.objects.only("id", "name", "parent_id").order_by("order", "name", "id"))
    root_nodes = _attach_children(nodes, "nav_children")
    _limit_tree_depth(root_nodes, "nav_children", max_depth=1)
    return root_nodes


def _build_board_tree():
    assignment_qs = BoardAssignment.objects.select_related("person", "role").order_by(
        "role__order",
        "role__name",
        "order",
        "person__surname",
        "person__first_name",
        "id",
    )
    nodes = list(
        BoardNode.objects.select_related("parent")
        .prefetch_related(
            Prefetch("assignments", queryset=assignment_qs, to_attr="prefetched_assignments")
        )
        .order_by("order", "name", "id")
    )

    for node in nodes:
        _group_assignments(node)

    root_nodes = _attach_children(nodes, "prefetched_children")
    _annotate_depth(root_nodes)
    return root_nodes


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
    return TemplateResponse(request, "board.html", {"board_roots": _build_board_tree()})


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
    active_alerts = Alert.objects.filter(start__isnull=False, end__isnull=True)
    return TemplateResponse(request, "index.html", {"front_page_alerts": active_alerts})


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
    pubs = Publication.objects.all().order_by("-year", "authors")
    return TemplateResponse(request, "publications.html", {"publications": pubs})


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
