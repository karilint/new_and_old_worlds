from django import template

register = template.Library()


@register.inclusion_tag("includes/board_node_list.html")
def render_board_nodes(nodes):
    return {"nodes": nodes}


@register.inclusion_tag("includes/board_nav_list.html")
def render_board_nav(nodes):
    return {"nodes": nodes}


@register.filter
def assignment_people(assignments):
    parts = []
    for assignment in assignments:
        label = assignment.person.display_name
        if assignment.note:
            label = f"{label} ({assignment.note})"
        parts.append(label)

    if not parts:
        return ""
    if len(parts) == 1:
        return parts[0]
    if len(parts) == 2:
        return f"{parts[0]} and {parts[1]}"
    return f"{', '.join(parts[:-1])} and {parts[-1]}"
