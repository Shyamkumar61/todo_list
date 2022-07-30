from django.template.context_processors import request
from .models import newstats
from django.db.models import F

class test:
    def __init__(self, get_response):
        self.get_response = get_response

    def stats(self, os_info):
        if "Windows" in os_info:
            stats = newstats.objects.all()
            if len(stats) == 0:
                form = newstats(win=1)
                form.save()
            else:
                newstats.objects.all().update(win=F('win')+1)
        elif "mac" in os_info:
            stats = newstats.objects.all()
            if len(stats) == 0:
                form = newstats(mac=1)
                form.save()
                newstats.win = F('mac') + 1
            else:
                newstats.objects.all().update(mac=F('mac')+1)
        elif "iPhone" in os_info:
            stats = newstats.objects.all()
            if len(stats) == 0:
                form = newstats(mac=1)
                form.save()
            else:
                newstats.objects.all().update(iph=F('iph')+1)
        elif "Android" in os_info:
            stats = newstats.objects.all()
            if len(stats) == 0:
                form = newstats(android=1)
                form.save()
            else:
                newstats.objects.all().update(android=F('iph')+1)
        else:
            stats = newstats.objects.all()
            if len(stats) == 0:
                form = newstats(oth=1)
                form.save()
            else:
                newstats.objects.all().update(oth=F('oth')+1)

    def __call__(self, request):
        if "admin" not in request.path:
            self.stats(request.META['HTTP_USER_AGENT'])
            response = self.get_response(request)
            return response
        else:
            response = self.get_response(request)
            return response