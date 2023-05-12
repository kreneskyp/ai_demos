from django.db import models
from django.utils.translation import gettext_lazy as _

class CatMeme(models.Model):
    """Model representing a cat meme."""
    title = models.CharField(_("Title"), max_length=200)
    image = models.ImageField(_("Image"), upload_to='memes/images/')
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    def __str__(self) -> str:
        return self.title
