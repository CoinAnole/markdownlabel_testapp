"""Unit tests for application structure."""
import unittest
from unittest.mock import patch
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy_garden.markdownlabel import MarkdownLabel


class TestApplicationStructure(unittest.TestCase):
    """Test that the app builds successfully and has correct structure."""

    def setUp(self):
        """Set up test fixtures."""
        # Import here to avoid Kivy initialization issues
        from main import MarkdownDemoApp
        self.app = MarkdownDemoApp()

    def tearDown(self):
        """Clean up after tests."""
        if hasattr(self, 'app') and self.app:
            self.app.stop()

    def test_app_builds_successfully(self):
        """Test that app builds successfully."""
        # Requirements: 2.1
        root_widget = self.app.build()
        self.assertIsNotNone(root_widget, "App should build and return a root widget")

    def test_window_size_configuration(self):
        """Test window size configuration."""
        # Requirements: 5.1
        # Build the app to trigger window configuration
        self.app.build()
        
        # Check that window size is set to 800x600
        self.assertEqual(Window.size, (800, 600), "Window size should be 800x600 pixels")

    def test_window_title_configuration(self):
        """Test window title configuration."""
        # Requirements: 5.3
        # Build the app to trigger title configuration
        self.app.build()
        
        # Check that title is descriptive and indicates MarkdownLabel demo
        self.assertIsNotNone(self.app.title, "App should have a title")
        self.assertIn('Markdown', self.app.title, "Title should mention Markdown")
        self.assertIn('demo', self.app.title.lower(), "Title should indicate it's a demo")

    def test_widget_tree_contains_scrollview(self):
        """Test that widget tree contains ScrollView."""
        # Requirements: 2.1, 3.1
        root_widget = self.app.build()
        self.assertIsInstance(root_widget, ScrollView, "Root widget should be a ScrollView")

    def test_widget_tree_contains_markdownlabel(self):
        """Test that widget tree contains MarkdownLabel."""
        # Requirements: 2.1
        root_widget = self.app.build()
        
        # ScrollView should have children
        self.assertGreater(len(root_widget.children), 0, "ScrollView should have children")
        
        # First child should be MarkdownLabel
        md_label = root_widget.children[0]
        self.assertIsInstance(md_label, MarkdownLabel, "ScrollView should contain a MarkdownLabel")

    def test_markdownlabel_has_content(self):
        """Test that MarkdownLabel has non-empty content."""
        # Requirements: 2.1
        root_widget = self.app.build()
        md_label = root_widget.children[0]
        
        self.assertIsNotNone(md_label.text, "MarkdownLabel should have text content")
        self.assertGreater(len(md_label.text), 0, "MarkdownLabel text should not be empty")

    def test_scrollview_configuration(self):
        """Test ScrollView configuration."""
        # Requirements: 3.1
        root_widget = self.app.build()
        
        # Check vertical scrolling is enabled
        self.assertTrue(root_widget.do_scroll_y, "Vertical scrolling should be enabled")
        
        # Check horizontal scrolling is disabled
        self.assertFalse(root_widget.do_scroll_x, "Horizontal scrolling should be disabled")


if __name__ == '__main__':
    unittest.main()
