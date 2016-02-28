# coding: utf-8
import sys
from django.test import TestCase
from django.utils import timezone
from ..models import *

class BachelorTest(TestCase):
    def test_username_accepts_unicode(self):
        unicode_string = u'☀☁☂☃☄★☆☇☈'
        user = Bachelor(username=unicode_string)
        user.save()
        self.assertTrue(user.pk)

        user = Bachelor.objects.get(username=unicode_string)
        user_representation = str(user)
        if sys.version_info >= (3,0,0):
            user_representation = user_representation.encode('utf-8')
        string_representation = unicode_string.encode('utf-8')
        self.assertEqual(user_representation, string_representation)

class PartyTest(TestCase):
    def test_unicode_shenanigans(self):
        unicode_string = u'☀☁☂☃☄★☆☇☈'
        user = Bachelor(username='testuser')
        user.save()
        self.assertTrue(user.pk)

        Party(when=timezone.now(), where=unicode_string, organizer=user).save()
        party = Party.objects.get(where=unicode_string)
        self.assertEqual(party.where, unicode_string)

        str_representation = str(party)
        if sys.version_info >= (3,0,0):
            self.assertFalse(isinstance(str_representation, bytes))
        else:
            self.assertTrue(isinstance(str_representation, bytes))

    def test_cant_throw_party_without_organizer(self):
        from django.db import IntegrityError
        with self.assertRaises(IntegrityError):
            Party(when=timezone.now(), where='somewhere').save()

class GameTest(TestCase):
    def test_unicode_shenanigans(self):
        unicode_string = u'☀☁☂☃☄★☆☇☈'
        user = Bachelor(username='testuser')
        user.save()
        self.assertTrue(user.pk)

        party = Party(when=timezone.now(), where='somewhere', organizer=user)
        party.save()
        self.assertTrue(party.pk)

        Game(party=party, name=unicode_string).save()
        game = Game.objects.get(name=unicode_string)
        self.assertEqual(game.name, unicode_string)

        str_representation = str(game)
        if sys.version_info >= (3,0,0):
            self.assertFalse(isinstance(str_representation, bytes))
        else:
            self.assertTrue(isinstance(str_representation, bytes))

class RatingTest(TestCase):
    pass
