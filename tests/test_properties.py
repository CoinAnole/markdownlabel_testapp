"""Property-based tests for the Kivy Markdown Demo App."""
import unittest
from hypothesis import given, strategies as st, settings
from unittest.mock import patch
from io import StringIO
from kivy_garden.markdown_label import MarkdownLabel


class TestProperties(unittest.TestCase):
    """Property-based tests using Hypothesis."""

    def setUp(self):
        """Set up test fixtures."""
        # Import here to avoid Kivy initialization issues
        from main import MarkdownDemoApp
        self.app = MarkdownDemoApp()

    def tearDown(self):
        """Clean up after tests."""
        if hasattr(self, 'app') and self.app:
            self.app.stop()

    @given(ref_string=st.text())
    @settings(max_examples=100)
    @patch('sys.stdout', new_callable=StringIO)
    def test_link_event_handler_robustness(self, mock_stdout, ref_string):
        """
        **Feature: kivy-markdown-demo-app, Property 1: Link event handler robustness**
        **Validates: Requirements 4.3**
        
        Property: For any link reference string passed to the on_ref_press event handler,
        the handler should complete without raising exceptions.
        
        This property verifies that the event handler is robust and won't crash
        the application regardless of what string is passed to it.
        """
        # Build the app to get the MarkdownLabel
        root_widget = self.app.build()
        md_label = root_widget.children[0]
        
        # The handler should not raise any exceptions for any string input
        try:
            self.app.on_ref_press(md_label, ref_string)
            # If we reach here, no exception was raised - test passes
        except Exception as e:
            self.fail(f"Handler raised exception for input '{ref_string}': {e}")


if __name__ == '__main__':
    unittest.main()
