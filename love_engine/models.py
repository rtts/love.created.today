from django.db import models
from django.contrib.auth.models import AbstractUser
from adminsortable.models import SortableMixin, SortableForeignKey

class Bachelor(AbstractUser):
    pass

class Party(models.Model):
    when = models.DateTimeField()
    where = models.CharField(max_length=255)
    organizer = models.ForeignKey(Bachelor, editable=False, related_name='parties_organizing')
    guests = models.ManyToManyField(Bachelor, editable=False, related_name='parties_attending')

class Game(SortableMixin):
    name = models.CharField(max_length=255)
    party = SortableForeignKey(Party, editable=False, related_name='games')
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['order']

class Aspect(SortableMixin):
    description = models.TextField()
    game = SortableForeignKey(Game, editable=False, related_name='aspects')
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['order']

class Rating(models.Model):
    aspect = models.ForeignKey(Aspect, editable=False, related_name='ratings')
    source = models.ForeignKey(Bachelor, editable=False, related_name='given_ratings')
    target = models.ForeignKey(Bachelor, editable=False, related_name='received_ratings')
    number = models.IntegerField()
