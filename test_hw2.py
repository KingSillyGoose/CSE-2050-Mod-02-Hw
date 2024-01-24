import unittest
from hw2 import Profile, Activity, Post, Message, User


class TestProfile(unittest.TestCase):
    """Test cases for the Profile class."""    
    def test_init(self):
        p1 = Profile('John', 'password', 'John123', 'john@example.com')
        self.assertEqual(p1.username, 'John')
        self.assertEqual(p1.password, 'password')
        self.assertEqual(p1.screen_name, 'John123')
        self.assertEqual(p1.email, 'john@example.com')
    

    def test_str(self):
        p2 = Profile('Adam', 'password', 'Adam123', 'adam@example.com')
        self.assertEqual(str(p2), "Profile - Username: Adam, Screen Name: Adam123, Email: adam@example.com")


    def test_modify_profile(self):
        p3 = Profile('Luke', 'password', 'Luke123', 'luke@example.com')
        p4 = Profile('Luke', 'wordpass', 'Luke456', 'luke123@example.com')
        p3.modify_profile(password = 'wordpass', screen_name='Luke456', email='luke123@example.com')
        self.assertEqual(str(p3), str(p4))
    

class TestActivity(unittest.TestCase):
    """Test cases for the Activity class."""
    def test_init(self):
        p1 = Profile('John', 'password', 'John123', 'john@example.com')
        content = 'hello'
        a1 = Activity(p1, content)
        self.assertEqual(str(a1), ('John', 'password', 'John123', 'john@example.com'))
        self.assertEqual(a1.content, 'hello')


class TestPost(unittest.TestCase):
    """Test cases for the Post class."""
    pass
        

class TestMessage(unittest.TestCase):
    """Test cases for the Message class."""
    pass

class TestUser(unittest.TestCase):
    """Test cases for the User class."""
    # Add more test cases for other methods and classes
    
    def setUp(self):
        self.user = User("user1", "password1", "User One", "user1@example.com")

    def test_create_post(self):
        """Test creating a post for a user."""
        post = self.user.create_post("Test Post Content")
        # Check if the post is added to the user's posts list
        self.assertIn(post, self.user.posts)
        # Check if the user is correct
        self.assertEqual(post.user, self.user)
        # Check if the content of the post is correct
        self.assertEqual(post.content, "Test Post Content")
    

if __name__ == "__main__":
    unittest.main()

