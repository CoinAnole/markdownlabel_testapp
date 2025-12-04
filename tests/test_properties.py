"""Property-based tests for the Kivy Markdown Demo App."""
import unittest
from hypothesis import given, strategies as st, settings
from unittest.mock import patch
from io import StringIO
from kivy_garden.markdownlabel import MarkdownLabel


def find_markdownlabels(widget):
    """Recursively find all MarkdownLabel widgets in the widget tree."""
    labels = []
    if isinstance(widget, MarkdownLabel):
        labels.append(widget)
    if hasattr(widget, 'children'):
        for child in widget.children:
            labels.extend(find_markdownlabels(child))
    return labels


class TestProperties(unittest.TestCase):
    """Property-based tests using Hypothesis."""

    def setUp(self):
        """Set up test fixtures."""
        # Import here to avoid Kivy initialization issues
        from main import MarkdownDemoApp, SAMPLE_MARKDOWN
        self.app = MarkdownDemoApp()
        self.sample_markdown = SAMPLE_MARKDOWN

    def tearDown(self):
        """Clean up after tests."""
        if hasattr(self, 'app') and self.app:
            self.app.stop()

    def test_consistent_sample_content(self):
        """
        **Feature: markdownlabel-label-compatibility, Property 1: Consistent Sample Content**
        **Validates: Requirements 9.1, 9.2**
        
        Property: For any MarkdownLabel variation in the demo app, the text property
        SHALL contain the same sample markdown content including a heading, paragraph,
        and inline code.
        
        This property verifies that all MarkdownLabel instances use consistent content
        for easy comparison across property variations.
        """
        # Build the app
        root_widget = self.app.build()
        
        # Find all MarkdownLabel widgets in the widget tree
        md_labels = find_markdownlabels(root_widget)
        
        # There should be multiple MarkdownLabel instances
        self.assertGreater(len(md_labels), 0, "App should contain MarkdownLabel widgets")
        
        # Verify all MarkdownLabels use the same sample content
        for md_label in md_labels:
            self.assertEqual(
                md_label.text,
                self.sample_markdown,
                f"All MarkdownLabel instances should use consistent sample content"
            )
        
        # Verify the sample content contains required elements (Requirements 9.1)
        self.assertIn('##', self.sample_markdown, "Sample content should contain a heading")
        self.assertIn('paragraph', self.sample_markdown.lower(), "Sample content should contain paragraph text")
        self.assertIn('`', self.sample_markdown, "Sample content should contain inline code")

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
