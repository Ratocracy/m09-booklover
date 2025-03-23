import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`
        book_lover = BookLover("Alice", "alice@example.com", "fantasy")
        book_lover.add_book("The Hobbit", 4)
        # Test
        self.assertTrue(book_lover.has_read("The Hobbit"))

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once
        book_lover = BookLover("Bob", "bob@example.com", "mystery")
        book_lover.add_book("The Catcher in the Rye", 5)
        book_lover.add_book("The Catcher in the Rye", 5)
        # Test
        self.assertEqual(book_lover.num_books_read(), 1)
        self.assertTrue(book_lover.has_read("The Catcher in the Rye"))

    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`
        book_lover = BookLover("Charlie", "charlie@example.com", "science fiction")
        book_lover.add_book("1984", 5)
        # Test
        self.assertTrue(book_lover.has_read("1984"))

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        book_lover = BookLover("Diana", "diana@example.com", "history")
        book_lover.add_book("The Iliad", 4)
        # Test
        self.assertFalse(book_lover.has_read("War and Peace"))

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected
        book_lover = BookLover("Eve", "eve@example.com", "biography")
        book_lover.add_book("Becoming", 5)
        book_lover.add_book("Educated", 4)
        book_lover.add_book("The Glass Castle", 3)
        # Test
        self.assertEqual(book_lover.num_books_read(), 3)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3.
        # Your test should check that the returned books have rating > 3
        book_lover = BookLover("Frank", "frank@example.com", "thriller")
        book_lover.add_book("The Girl with the Dragon Tattoo", 4)
        book_lover.add_book("Gone Girl", 5)
        book_lover.add_book("The Silent Patient", 2)
        # Get the favorite books with rating > 3
        fav_books = book_lover.fav_books()
        # Test
        self.assertTrue(all(rating > 3 for rating in fav_books['book_rating']))

if __name__ == '__main__':
    unittest.main(verbosity=3)
