from django.http import HttpResponse


def robots_txt(request):
    lignes = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /django-admin/",
        "Disallow: /documents/",
        "",
        "Sitemap: %s://%s/sitemap.xml" % (request.scheme, request.get_host()),
    ]
    return HttpResponse("\n".join(lignes), content_type="text/plain")
