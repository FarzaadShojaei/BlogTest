from unittest import TestCase
import sys
import blog
from blog.post import Post


class PostTest(TestCase):
    def test_create_post(self):
        p=Post('Test','Test Content')

        self.assertEqual('Test',p.title)
        self.assertEqual('Test Content',p.content)

    def test_json(self):
        p=Post('Test','Test Content')
        expected={'title':'Test','Content':'Test Content'}

        self.assertDictEqual(expected,p.json())


