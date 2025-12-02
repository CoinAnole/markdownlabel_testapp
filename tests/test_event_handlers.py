"""Unit tests for event handlers."""
import unittest
from unittest.mock import patch
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

    def test_on_ref_press_handler_is_bound(self):
        """Test that on_ref_press handler is bound to MarkdownLabel."""
        # Requirements: 4.1
        root_widget = self.app.build()
        
        # Get the MarkdownLabel from the ScrollView
        md_label = root_widget.children[0]
        self.assertIsInstance(md_label, MarkdownLabel, "Should have MarkdownLabel widget")
        
        # Check that on_ref_press event is bound
        # In Kivy, bound events are stored in the widget's event dispatcher
        self.assertTrue(
            md_label.is_event_type('on_ref_press'),
            "MarkdownLabel should support on_ref_press event"
        )
        
        # Verify the handler is bound by checking if it's in the event callbacks
        # The bind() method adds callbacks to the event
        bound_callbacks = md_label.get_property_observers('on_ref_press')
        self.assertGreater(
            len(bound_callbacks), 0,
            "on_ref_press should have at least one bound callback"
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_handler_prints_correct_output(self, mock_stdout):
        """Test that handler prints the correct output."""
        # Requirements: 4.2
        root_widget = self.app.build()
        md_label = root_widget.children[0]
        
        # Simulate a link click with a test URL
        test_url = "https://example.com"
        self.app.on_ref_press(md_label, test_url)
        
        # Check that the URL was printed to stdout
        output = mock_stdout.getvalue()
        self.assertIn(test_url, output, "Handler should print the clicked URL")
        self.assertIn("Link clicked:", output, "Handler should include descriptive text")

    @patch('sys.stdout', new_callable=StringIO)
    def test_handler_does_not_crash_with_various_inputs(self, mock_stdout):
        """Test that handler doesn't crash with various input types."""
        # Requirements: 4.3
        root_widget = self.app.build()
        md_label = root_widget.children[0]
        
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
                    self.app.on_ref_press(md_label, test_input)
                    # If we get here, no exception was raised
                    self.assertTrue(True, "Handler should not raise exception")
                except Exception as e:
                    self.fail(f"Handler raised exception for input '{test_input}': {e}")


if __name__ == '__main__':
    unittest.main()
