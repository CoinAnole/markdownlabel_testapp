#!/usr/bin/env python3
"""
Kivy Markdown Demo App

A demonstration application that showcases the MarkdownLabel widget
and its Label-compatible properties from the kivy_garden.markdownlabel flower.
"""

from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy_garden.markdownlabel import MarkdownLabel


# Sample markdown content used across all variations (Requirement 9.1)
SAMPLE_MARKDOWN = """## Sample Heading

This is a paragraph with some text to demonstrate the property. It includes `inline code` for testing code font preservation.

Another paragraph to show line spacing effects."""


class MarkdownDemoApp(App):
    """Demo app showcasing MarkdownLabel Label-compatible properties."""
    
    def build(self):
        """Build scrollable layout with property demonstration sections."""
        # Configure window size
        Window.size = (800, 1200)
        self.title = "MarkdownLabel Demo - Label Compatibility"
        
        # Create main vertical BoxLayout container
        main_layout = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            spacing=20,
            padding=[10, 10, 10, 10]
        )
        # Bind height to minimum_height for proper scrolling
        main_layout.bind(minimum_height=main_layout.setter('height'))
        
        # Create ScrollView for vertical scrolling (Requirement 8.1)
        scroll_view = ScrollView(
            do_scroll_x=False,
            do_scroll_y=True
        )
        scroll_view.add_widget(main_layout)
        
        # Store reference to main layout for adding sections
        self.main_layout = main_layout
        
        # Add font_name demonstration section (Requirements 1.1, 1.2)
        font_name_variations = [
            ("font_name='Roboto' (default)", {"font_name": "Roboto"}),
            ("font_name='DejaVuSans'", {"font_name": "DejaVuSans"}),
        ]
        font_name_section = self.create_section("font_name", font_name_variations)
        main_layout.add_widget(font_name_section)
        
        # Add font_size demonstration section (Requirements 2.1, 2.2)
        font_size_variations = [
            ("font_size=14", {"font_size": 14}),
            ("font_size=20", {"font_size": 20}),
            ("font_size=28", {"font_size": 28}),
        ]
        font_size_section = self.create_section("font_size", font_size_variations)
        main_layout.add_widget(font_size_section)
        
        # Add color demonstration section (Requirements 3.1, 3.2)
        color_variations = [
            ("color=[1,1,1,1] (white)", {"color": [1, 1, 1, 1]}),
            ("color=[1,1,0,1] (yellow)", {"color": [1, 1, 0, 1]}),
            ("color=[0,1,1,1] (cyan)", {"color": [0, 1, 1, 1]}),
        ]
        color_section = self.create_section("color", color_variations)
        main_layout.add_widget(color_section)
        
        # Add line_height demonstration section (Requirements 4.1, 4.2)
        line_height_variations = [
            ("line_height=1.0", {"line_height": 1.0}),
            ("line_height=1.5", {"line_height": 1.5}),
            ("line_height=2.0", {"line_height": 2.0}),
        ]
        line_height_section = self.create_section("line_height", line_height_variations)
        main_layout.add_widget(line_height_section)
        
        return scroll_view
    
    def create_header(self, title):
        """Create a section header label.
        
        Args:
            title: Header text for the section
            
        Returns:
            Label widget styled as a section header
        """
        header = Label(
            text=f"[b]{title}[/b]",
            markup=True,
            font_size='24sp',
            size_hint_y=None,
            height=50,
            color=[1, 0.8, 0, 1],  # Gold color for headers
            halign='left',
            valign='middle'
        )
        header.bind(size=header.setter('text_size'))
        return header
    
    def create_variation(self, description, **properties):
        """Create a single MarkdownLabel variation with description.
        
        Args:
            description: Text describing the property values
            **properties: Properties to apply to MarkdownLabel
            
        Returns:
            BoxLayout containing description and MarkdownLabel
        """
        variation_layout = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            spacing=5,
            padding=[10, 5, 10, 5]
        )
        
        # Description label (Requirement 8.3)
        desc_label = Label(
            text=description,
            font_size='14sp',
            size_hint_y=None,
            height=30,
            color=[0.7, 0.7, 0.7, 1],  # Gray color for descriptions
            halign='left',
            valign='middle'
        )
        desc_label.bind(size=desc_label.setter('text_size'))
        variation_layout.add_widget(desc_label)
        
        # MarkdownLabel with specified properties (Requirement 9.1, 9.2)
        md_label = MarkdownLabel(
            text=SAMPLE_MARKDOWN,
            size_hint_y=None,
            **properties
        )
        md_label.bind(minimum_height=md_label.setter('height'))
        md_label.bind(on_ref_press=self.on_ref_press)
        variation_layout.add_widget(md_label)
        
        # Calculate total height
        variation_layout.bind(
            minimum_height=variation_layout.setter('height')
        )
        
        return variation_layout
    
    def create_section(self, title, variations):
        """Create a section with header and variations.
        
        Args:
            title: Section header text
            variations: List of (description, property_dict) tuples
            
        Returns:
            BoxLayout containing the section
        """
        section_layout = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            spacing=10,
            padding=[0, 10, 0, 20]
        )
        
        # Add section header (Requirement 8.2)
        header = self.create_header(title)
        section_layout.add_widget(header)
        
        # Add each variation
        for description, props in variations:
            variation = self.create_variation(description, **props)
            section_layout.add_widget(variation)
        
        # Bind height to minimum_height
        section_layout.bind(minimum_height=section_layout.setter('height'))
        
        return section_layout
    
    def on_ref_press(self, instance, ref):
        """Handle link click events from MarkdownLabel.
        
        Args:
            instance: The MarkdownLabel widget instance
            ref: The reference/URL that was clicked
        """
        try:
            print(f"Link clicked: {ref}")
        except Exception as e:
            print(f"Error handling link click: {e}")


if __name__ == '__main__':
    MarkdownDemoApp().run()
