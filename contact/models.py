from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import (
    FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel,
)
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.fields import RichTextField


class FormField(AbstractFormField):
    page = ParentalKey(
        "ContactPage",
        on_delete=models.CASCADE,
        related_name="form_fields",
    )


class ContactPage(AbstractEmailForm):
    intro = RichTextField(blank=True, verbose_name="Introduction")
    thank_you_text = RichTextField(blank=True, verbose_name="Message de remerciement")

    parent_page_types = ["home.HomePage"]
    subpage_types = []

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("intro"),
        InlinePanel("form_fields", label="Champs du formulaire"),
        FieldPanel("thank_you_text"),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel("from_address"),
                    FieldPanel("to_address"),
                ]),
                FieldPanel("subject"),
            ],
            "Envoi par e-mail",
        ),
    ]

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        autocompletes = {
            "nom": "name",
            "entreprise": "organization",
            "email": "email",
            "telephone": "tel",
            "adresse": "street-address",
        }
        for nom_champ, valeur in autocompletes.items():
            if nom_champ in form.fields:
                form.fields[nom_champ].widget.attrs["autocomplete"] = valeur
        return form