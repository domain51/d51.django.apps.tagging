from d51.django.apps.tagging.models import *
from django.test import TestCase
from project.mysite.models import *
import random


def generate_random_tag():
    return Tag.objects.create(title=random.randint(1, 100))

def generate_random_tags(number):
    return [generate_random_tag() for i in range(number)]

class TagTestCase(TestCase):
    def test_tags_can_have_other_tags(self):
        [a, b] = generate_random_tags(2)
        a.parent = b
        a.save()
        b.save()

        self.assertEqual(a.parent, b)
        self.assertEqual(b.children.all()[0], a)

    def test_should_return_list_of_tags_for_given_model(self):
        p = Post.objects.create(title="foobar")
        tag = Tag.objects.create(title="awesome")
        p.tags.add(tag)

        tagged_posts = Post.objects.filter(tags__in=[tag])
        self.assertEqual(1, tagged_posts.count())

    def test_models_can_define_tags(self):
        article = Article.objects.create(title="foobar")
        [a, b, c] = generate_random_tags(3)

        for tag in [a, b]:
            article.tags.add(tag)

        self.assertEqual(2, article.tags.count())
        self.assert_(a in article.tags.all())
        self.assert_(b in article.tags.all())

