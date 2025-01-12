import factory
from polls import models
from django.utils import timezone

# https://factoryboy.readthedocs.io/en/stable/
# https://factoryboy.readthedocs.io/en/stable/orms.html

class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Question

    question_text = 'What is your favorite color?'
    pub_date = timezone.now()
