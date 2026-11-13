from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class ProduitsIndexPage(Page):
    parent_page_types = ["home.HomePage"]
    subpage_types = ["produits.ProduitPage"]

    def get_context(self, request):
        context = super().get_context(request)
        produits = ProduitPage.objects.child_of(self).live()
        context["signatures"] = produits.filter(categorie="signature")
        context["audacieuses"] = produits.filter(categorie="audacieuse")
        return context

class ProduitPage(Page):
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Photo",
    )
    description = RichTextField(blank=True, verbose_name="Description")
    prix = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Prix (€)")
    degre_alcool = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Degré d'alcool (%)")
    categorie = models.CharField(
        max_length=20,
        choices=[
            ("signature", "Produits signatures"),
            ("audacieuse", "Créations audacieuses"),
        ],
        default="signature",
        verbose_name="Catégorie",
    )
    est_vedette = models.BooleanField(default=False, verbose_name="Afficher sur l'accueil")

    parent_page_types = ["produits.ProduitsIndexPage"]
    subpage_types = []

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("description"),
        FieldPanel("prix"),
        FieldPanel("degre_alcool"),
        FieldPanel("categorie"),
        FieldPanel("est_vedette"),
    ]