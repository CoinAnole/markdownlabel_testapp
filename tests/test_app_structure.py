"""Unit tests for application structure."""
import unittest
from unittest.mock import patch
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
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
        # Requirements: 8.1 - scrollable layout for multi-section demo
        # Build the app to trigger window configuration
        self.app.build()
        
        # Check that window size is set to 800x1200 for multi-section layout
        self.assertEqual(Window.size, (800, 1200), "Window size should be 800x1200 pixels")

    def test_window_title_configuration(self):
        """Test window title configuration."""
        # Requirements: 5.3
        # Build the app to trigger title configuration
        self.app.build()
        
        # Check that title is descriptive and indicates MarkdownLabel demo
        self.assertIsNotNone(self.app.title, "App should have a title")
        self.assertIn('Markdown', self.app.title, "Title should mention Markdown")
        self.assertIn('Demo', self.app.title, "Title should indicate it's a demo")

    def test_widget_tree_contains_scrollview(self):
        """Test that widget tree contains ScrollView."""
        # Requirements: 8.1
        root_widget = self.app.build()
        self.assertIsInstance(root_widget, ScrollView, "Root widget should be a ScrollView")

    def test_widget_tree_contains_main_boxlayout(self):
        """Test that ScrollView contains main BoxLayout container."""
        # Requirements: 8.1
        root_widget = self.app.build()
        
        # ScrollView should have children
        self.assertGreater(len(root_widget.children), 0, "ScrollView should have children")
        
        # First child should be BoxLayout (main container)
        main_layout = root_widget.children[0]
        self.assertIsInstance(main_layout, BoxLayout, "ScrollView should contain a BoxLayout")
        self.assertEqual(main_layout.orientation, 'vertical', "Main layout should be vertical")

    def test_main_layout_has_proper_size_hints(self):
        """Test that main layout has proper size hints for scrolling."""
        # Requirements: 8.1
        root_widget = self.app.build()
        main_layout = root_widget.children[0]
        
        # size_hint_y should be None for scrollable content
        self.assertIsNone(main_layout.size_hint_y, "Main layout size_hint_y should be None")

    def test_scrollview_configuration(self):
        """Test ScrollView configuration."""
        # Requirements: 8.1
        root_widget = self.app.build()
        
        # Check vertical scrolling is enabled
        self.assertTrue(root_widget.do_scroll_y, "Vertical scrolling should be enabled")
        
        # Check horizontal scrolling is disabled
        self.assertFalse(root_widget.do_scroll_x, "Horizontal scrolling should be disabled")
    
    def test_helper_methods_exist(self):
        """Test that helper methods for section creation exist."""
        # Requirements: 8.2, 8.3
        self.app.build()
        
        self.assertTrue(hasattr(self.app, 'create_section'), "App should have create_section method")
        self.assertTrue(hasattr(self.app, 'create_variation'), "App should have create_variation method")
        self.assertTrue(hasattr(self.app, 'create_header'), "App should have create_header method")
        self.assertTrue(callable(self.app.create_section), "create_section should be callable")
        self.assertTrue(callable(self.app.create_variation), "create_variation should be callable")
        self.assertTrue(callable(self.app.create_header), "create_header should be callable")


if __name__ == '__main__':
    unittest.main()
