import factory
import datetime

from factory import fuzzy

from api.models import Film
from tests.factories.language_factory import LanguageFactory


class FilmFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Film

	language = factory.SubFactory(LanguageFactory)
	last_update = datetime.datetime.now(datetime.UTC)
	rental_duration = fuzzy.FuzzyInteger(0, 42)
	rental_rate = fuzzy.FuzzyDecimal(0.5, 5.0, 2)
	replacement_cost = fuzzy.FuzzyDecimal(5, 30, 2)
