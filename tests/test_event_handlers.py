"""Unit tests for event handlers."""
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from kivy_garden.markdownlabel import MarkdownLabel


class TestEventHandlers(unittest.TestCase):
    """Test event handler functionality."""

    def setUp(self):
        """Set up test fixtures."""
        # Import here to avoid Kivy initialization issues
        from main import MarkdownDemoApp
        self.app = MarkdownDemoApp()

    def tearDown(self):
        """Clean up after tests."""
        if hasattr(self, 'app') and self.app:
            self.app.stop()

    def test_on_ref_press_handler_exists(self):
        """Test that on_ref_press handler method exists on the app."""
        # Requirements: 4.1
        self.app.build()
        
        # Check that the app has the on_ref_press handler method
        self.assertTrue(
            hasattr(self.app, 'on_ref_press'),
            "App should have on_ref_press handler method"
        )
        self.assertTrue(
            callable(self.app.on_ref_press),
            "on_ref_press should be callable"
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_handler_prints_correct_output(self, mock_stdout):
        """Test that handler prints the correct output."""
        # Requirements: 4.2
        self.app.build()
        
        # Create a mock instance for testing
        mock_instance = MagicMock()
        
        # Simulate a link click with a test URL
        test_url = "https://example.com"
        self.app.on_ref_press(mock_instance, test_url)
        
        # Check that the URL was printed to stdout
        output = mock_stdout.getvalue()
        self.assertIn(test_url, output, "Handler should print the clicked URL")
        self.assertIn("Link clicked:", output, "Handler should include descriptive text")

    @patch('sys.stdout', new_callable=StringIO)
    def test_handler_does_not_crash_with_various_inputs(self, mock_stdout):
        """Test that handler doesn't crash with various input types."""
        # Requirements: 4.3
        self.app.build()
        
        # Create a mock instance for testing
        mock_instance = MagicMock()
        
        # Test with various inputs
        test_inputs = [
            "https://example.com",
            "http://test.org/path?query=value",
            "",
            "not-a-url",
            "mailto:test@example.com",
            "#anchor",
            "/relative/path",
        ]
        
        for test_input in test_inputs:
            with self.subTest(input=test_input):
                try:
                    self.app.on_ref_press(mock_instance, test_input)
                    # If we get here, no exception was raised
                    self.assertTrue(True, "Handler should not raise exception")
                except Exception as e:
                    self.fail(f"Handler raised exception for input '{test_input}': {e}")


if __name__ == '__main__':
    unittest.main()
