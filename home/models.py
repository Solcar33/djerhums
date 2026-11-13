from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from produits.models import ProduitPage


class HomePage(Page):
    intro_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Image d'introduction"
    )
    intro_marque = RichTextField(blank=True, verbose_name="Présentation de la marque")
    intro_createur = RichTextField(blank=True, verbose_name="Présentation du créateur")

    content_panels = Page.content_panels + [
        FieldPanel("intro_image"),
        FieldPanel("intro_marque"),
        FieldPanel("intro_createur"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["produits_vedette"] = ProduitPage.objects.live().filter(est_vedette=True)[:3]
        return context


class PageSimple(Page):
    intro = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Introduction",
    )
    corps = RichTextField(blank=True, verbose_name="Contenu")

    parent_page_types = ["home.HomePage"]
    subpage_types = []

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("corps"),
    ]