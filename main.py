#!/usr/bin/env python3
"""
Kivy Markdown Demo App

A simple demonstration application that showcases the MarkdownLabel widget
from the kivy_garden.markdownlabel flower.
"""

from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy_garden.markdownlabel import MarkdownLabel
import os


class MarkdownDemoApp(App):
    """Main application class for the Markdown demo."""
    
    def build(self):
        """Build and return the root widget."""
        # Configure window size to 800x600 pixels (Requirement 5.1)
        Window.size = (800, 600)
        
        # Set descriptive window title (Requirement 5.3)
        self.title = "MarkdownLabel Demo - Kivy Garden"
        
        # Load sample markdown content
        try:
            sample_path = os.path.join(os.path.dirname(__file__), 'sample_markdown.md')
            with open(sample_path, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
        except FileNotFoundError:
            markdown_content = "# Error\n\nCould not find sample_markdown.md file."
        except Exception as e:
            markdown_content = f"# Error\n\nFailed to load sample_markdown.md: {str(e)}"
        
        # Create MarkdownLabel widget
        # MarkdownLabel automatically manages its height via minimum_height
        # Set size_hint_y to None and bind height to minimum_height for proper scrolling
        md_label = MarkdownLabel(
            text=markdown_content,
            size_hint_y=None
        )
        md_label.bind(minimum_height=md_label.setter('height'))
        
        # Bind link click event handler (Requirement 4.1)
        md_label.bind(on_ref_press=self.on_ref_press)
        
        # Create ScrollView with vertical scrolling
        scroll_view = ScrollView(
            do_scroll_x=False,
            do_scroll_y=True
        )
        scroll_view.add_widget(md_label)
        
        # Return the root widget (Requirement 2.1)
        return scroll_view
    
    def on_ref_press(self, instance, ref):
        """Handle link click events from MarkdownLabel.
        
        Args:
            instance: The MarkdownLabel widget instance
            ref: The reference/URL that was clicked
        
        Requirements: 4.1, 4.2, 4.3
        """
        try:
            # Display the clicked URL in console output (Requirement 4.2)
            print(f"Link clicked: {ref}")
        except Exception as e:
            # Error handling to prevent crashes (Requirement 4.3)
            print(f"Error handling link click: {e}")


if __name__ == '__main__':
    MarkdownDemoApp().run()
