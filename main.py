#!/usr/bin/env python3
"""
Kivy Markdown Demo App

A simple demonstration application that showcases the MarkdownLabel widget
from the kivy_garden.markdown_label flower.
"""

from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy_garden.markdown_label import MarkdownLabel


class MarkdownDemoApp(App):
    """Main application class for the Markdown demo."""
    
    def build(self):
        """Build and return the root widget."""
        # TODO: Implement in task 3
        pass
    
    def on_ref_press(self, instance, ref):
        """Handle link click events from MarkdownLabel."""
        # TODO: Implement in task 5
        pass


if __name__ == '__main__':
    MarkdownDemoApp().run()
