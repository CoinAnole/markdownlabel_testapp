"""Unit tests for content verification."""
import os
import re
import unittest


class TestSampleContentCompleteness(unittest.TestCase):
    """Test that sample_markdown.md contains all required Markdown elements."""

    @classmethod
    def setUpClass(cls):
        """Load the sample markdown file once for all tests."""
        sample_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sample_markdown.md')
        with open(sample_path, 'r', encoding='utf-8') as f:
            cls.content = f.read()

    def test_sample_file_exists(self):
        """Test that sample_markdown.md exists and is readable."""
        sample_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sample_markdown.md')
        self.assertTrue(os.path.exists(sample_path), "sample_markdown.md should exist")

    def test_all_heading_levels(self):
        """Test that all heading levels (H1-H6) are present."""
        # Requirements: 2.2
        self.assertIn('# ', self.content, "H1 heading should be present")
        self.assertIn('## ', self.content, "H2 heading should be present")
        self.assertIn('### ', self.content, "H3 heading should be present")
        self.assertIn('#### ', self.content, "H4 heading should be present")
        self.assertIn('##### ', self.content, "H5 heading should be present")
        self.assertIn('###### ', self.content, "H6 heading should be present")

    def test_inline_formatting_bold(self):
        """Test that bold formatting is present."""
        # Requirements: 2.3
        self.assertTrue(
            '**' in self.content,
            "Bold formatting (** **) should be present"
        )

    def test_inline_formatting_italic(self):
        """Test that italic formatting is present."""
        # Requirements: 2.3
        self.assertTrue(
            '*' in self.content and '**' in self.content,
            "Italic formatting (* *) should be present"
        )

    def test_inline_formatting_strikethrough(self):
        """Test that strikethrough formatting is present."""
        # Requirements: 2.3
        self.assertIn('~~', self.content, "Strikethrough formatting (~~ ~~) should be present")

    def test_inline_formatting_code(self):
        """Test that inline code formatting is present."""
        # Requirements: 2.3
        # Look for backticks that are not part of code blocks (```)
        lines = self.content.split('\n')
        has_inline_code = any('`' in line and '```' not in line for line in lines)
        self.assertTrue(has_inline_code, "Inline code formatting (` `) should be present")

    def test_unordered_list(self):
        """Test that unordered list is present."""
        # Requirements: 2.4
        self.assertTrue(
            re.search(r'^- ', self.content, re.MULTILINE),
            "Unordered list (- item) should be present"
        )

    def test_ordered_list(self):
        """Test that ordered list is present."""
        # Requirements: 2.4
        self.assertTrue(
            re.search(r'^\d+\. ', self.content, re.MULTILINE),
            "Ordered list (1. item) should be present"
        )

    def test_table_present(self):
        """Test that a table with headers and multiple rows is present."""
        # Requirements: 2.5
        # Tables in Markdown use | for columns
        self.assertIn('|', self.content, "Table structure (|) should be present")
        
        # Check for table header separator (e.g., |---|---|)
        self.assertTrue(
            re.search(r'\|[-:]+\|', self.content),
            "Table header separator should be present"
        )
        
        # Count rows with | characters (should have at least header + separator + 2 data rows = 4)
        table_rows = [line for line in self.content.split('\n') if '|' in line and line.strip()]
        self.assertGreaterEqual(
            len(table_rows), 4,
            "Table should have at least header, separator, and multiple data rows"
        )

    def test_code_block_with_language(self):
        """Test that a code block with language specification is present."""
        # Requirements: 2.6
        self.assertTrue(
            re.search(r'```\w+', self.content),
            "Code block with language specification (```language) should be present"
        )

    def test_blockquote_present(self):
        """Test that a blockquote is present."""
        # Requirements: 2.7
        self.assertTrue(
            re.search(r'^> ', self.content, re.MULTILINE),
            "Blockquote (> text) should be present"
        )

    def test_clickable_links(self):
        """Test that clickable links are present."""
        # Requirements: 2.8
        # Markdown links: [text](url)
        self.assertTrue(
            re.search(r'\[.+?\]\(.+?\)', self.content),
            "Clickable links ([text](url)) should be present"
        )
        
        # Should have at least one link
        links = re.findall(r'\[.+?\]\(.+?\)', self.content)
        self.assertGreater(len(links), 0, "At least one clickable link should be present")


if __name__ == '__main__':
    unittest.main()
