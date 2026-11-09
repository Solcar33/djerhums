from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


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