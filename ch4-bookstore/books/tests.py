from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse

from .models import Book, Review


class BookTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@mail.com',
            password='testpassword123',
        )

        cls.special_permission = Permission.objects.get(
            codename='special_status')

        cls.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            price=19.99,
        )

        cls.review = Review.objects.create(
            book=cls.book,
            author=cls.user,
            review='This is a test review from reviewuser',
        )

    def test_book_listing(self):
        #  test string representation of the book
        self.assertEqual(f'{self.book.title}', 'Test Book')
        self.assertEqual(f'{self.book.author}', 'Test Author')
        self.assertEqual(f'{self.book.price}', '19.99')

    def test_book_list_view_for_logged_in_user(self):
        self.client.login(email='reviewuser@mail.com',
                          password='testpassword123')
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "%s?next=/books/" %
                             (reverse("account_login")))
        response = self.client.get("%s?next=/books/" %
                                   (reverse("account_login")))
        self.assertContains(response, 'Log In')

    def test_book_detail_view_with_permissions(self):
        self.client.login(email='reviewuser@mail.com',
                          password='testpassword123')
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Test Book')
        self.assertEqual(response.context['book'].author, 'Test Author')
        self.assertContains(response, 'This is a test review from reviewuser')
        self.assertTemplateUsed(response, 'books/book_detail.html')

    # def test_book_list_view(self):
    #     response = self.client.get(reverse('book_list'))
    #     self.assertEqual(response.status_c'ode, 200)
    #     self.assertContains(response, 'Test Book')
    #     self.assertTemplateUsed(response, 'books/book_list.html')

    # def test_book_detail_view(self):
    #     response = self.client.get(self.book.get_absolute_url())
    #     no_response = self.client.get('/books/12345/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(no_response.status_code, 404)
    #     self.assertContains(response, 'Test Book')
    #     self.assertEqual(response.context['book'].author, 'Test Author')
    #     self.assertContains(response, 'This is a test review from reviewuser')
    #     self.assertTemplateUsed(response, 'books/book_detail.html')
