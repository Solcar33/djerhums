from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


class EvenementsIndexPage(Page):
    intro = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Introduction",
    )
    partenaires = RichTextField(blank=True, verbose_name="Partenaires professionnels")
    facebook = models.URLField(blank=True, verbose_name="Page Facebook")
    instagram = models.URLField(blank=True, verbose_name="Compte Instagram")

    parent_page_types = ["home.HomePage"]
    subpage_types = ["evenements.EvenementPage"]

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("partenaires"),
        FieldPanel("facebook"),
        FieldPanel("instagram"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["evenements"] = EvenementPage.objects.child_of(self).live().order_by("date")
        context["liste_partenaires"] = Partenaire.objects.all()
        return context


class EvenementPage(Page):
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Photo",
    )
    date = models.DateField(verbose_name="Date")
    lieu = models.CharField(max_length=150, blank=True, verbose_name="Lieu")
    description = RichTextField(blank=True, verbose_name="Description")

    parent_page_types = ["evenements.EvenementsIndexPage"]
    subpage_types = []

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("date"),
        FieldPanel("lieu"),
        FieldPanel("description"),
    ]

@register_snippet
class Partenaire(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom")
    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Logo",
    )
    lien = models.URLField(blank=True, verbose_name="Site web")

    panels = [
        FieldPanel("nom"),
        FieldPanel("logo"),
        FieldPanel("lien"),
    ]

    class Meta:
        verbose_name = "Partenaire"
        verbose_name_plural = "Partenaires"
        ordering = ["nom"]

    def __str__(self):
        return self.nom