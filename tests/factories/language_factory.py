import factory
import datetime

from api.models import Language


class LanguageFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Language

	last_update = datetime.datetime.now(datetime.UTC)
