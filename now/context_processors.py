from django.db.models import Q
from django.utils import timezone

from .models import Notice


def notices(request):
    now = timezone.now()
    active_notices = Notice.objects.filter(active=True).filter(
        Q(starts_at__isnull=True) | Q(starts_at__lte=now),
        Q(ends_at__isnull=True) | Q(ends_at__gte=now),
    )
    return {"active_notices": active_notices}
