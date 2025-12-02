# Kivy MarkdownLabel Demo App

A simple demonstration application that showcases the MarkdownLabel widget from the `kivy_garden.markdownlabel` flower. This app serves as a test harness to verify that the MarkdownLabel widget correctly renders various Markdown syntax elements including headings, formatting, lists, tables, code blocks, links, and more.

## Purpose

This demo app is designed to:
- Demonstrate the capabilities of the MarkdownLabel widget
- Provide a visual test harness for Markdown rendering
- Serve as a reference implementation for using MarkdownLabel in Kivy applications
- Verify that all common Markdown syntax elements render correctly

## Prerequisites

Before running this demo app, ensure you have the following system dependencies installed:

### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv
sudo apt-get install -y libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
sudo apt-get install -y libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev
sudo apt-get install -y libgstreamer1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good
```

### macOS
```bash
brew install python3
brew install sdl2 sdl2_image sdl2_ttf sdl2_mixer
```

### Windows
- Install Python 3.8 or higher from [python.org](https://www.python.org/downloads/)
- Kivy dependencies are typically included with pip installation on Windows

## Setup Instructions

Follow these step-by-step instructions to set up and run the demo app:

### 1. Create a Python Virtual Environment

Navigate to the project directory and create a virtual environment:

```bash
python3 -m venv .venv
```

### 2. Activate the Virtual Environment

**Linux/macOS:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

With the virtual environment activated, install the required dependencies:

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

### 4. Install the MarkdownLabel Flower

Install the `kivy_garden.markdownlabel` flower in development mode from the external directory:

```bash
python3 -m pip install -e external/markdownlabel
```

### 5. Verify Installation

Verify that the MarkdownLabel widget can be imported:

```bash
python3 -c "from kivy_garden.markdownlabel import MarkdownLabel; print('Installation successful!')"
```

## Running the Demo App

Once setup is complete, run the demo app with the following command:

```bash
python3 main.py
```

The application window will open displaying a scrollable view of rendered Markdown content. You can:
- Scroll vertically to view all Markdown examples
- Click on links to see the URL printed in the console
- Resize the window to see how the content adapts

## Project Structure

```
.
├── main.py              # Main application entry point
├── sample_markdown.md   # Sample Markdown content with comprehensive examples
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── tests/              # Unit and property-based tests
└── external/           # External dependencies (markdownlabel flower)
```

## Troubleshooting

### Common Issues and Solutions

#### Issue: "ModuleNotFoundError: No module named 'kivy'"

**Solution:** Ensure you have activated the virtual environment and installed dependencies:
```bash
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
python3 -m pip install -r requirements.txt
```

#### Issue: "ModuleNotFoundError: No module named 'kivy_garden.markdownlabel'"

**Solution:** Install the MarkdownLabel flower in development mode:
```bash
python3 -m pip install -e external/markdownlabel
```

#### Issue: SDL2 library errors on Linux

**Solution:** Install the required SDL2 system libraries:
```bash
sudo apt-get install -y libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
```

#### Issue: "python3: command not found"

**Solution:** 
- On Linux/macOS: Install Python 3 using your package manager
- On Windows: Download and install Python from [python.org](https://www.python.org/downloads/)

#### Issue: Application window is blank or not rendering

**Solution:** 
1. Check that `sample_markdown.md` exists in the project root
2. Verify the file is readable and contains content
3. Check the console for any error messages

#### Issue: Links are not clickable

**Solution:** This is expected behavior - the demo app prints clicked URLs to the console rather than opening them in a browser. Check your terminal/console output when clicking links.

#### Issue: Window size is too small or too large

**Solution:** The default window size is 800x600 pixels. You can resize the window manually, or modify the `Config.set()` calls in `main.py` to adjust the default size.

#### Issue: Tests are failing

**Solution:** 
1. Ensure all dependencies are installed: `python3 -m pip install -r requirements.txt`
2. Ensure the MarkdownLabel flower is installed: `python3 -m pip install -e external/markdownlabel`
3. Run tests with: `python3 -m pytest tests/`
4. Check that `sample_markdown.md` and `main.py` exist and are not corrupted

## Running Tests

To run the test suite:

```bash
# Run all tests
python3 -m pytest tests/

# Run specific test file
python3 -m pytest tests/test_content.py

# Run with verbose output
python3 -m pytest tests/ -v
```

## License

This demo application is provided as-is for demonstration and testing purposes.

## Additional Resources

- [Kivy Documentation](https://kivy.org/doc/stable/)
- [MarkdownLabel Flower Documentation](https://github.com/kivy-garden/garden.markdownlabel)
- [Markdown Syntax Guide](https://www.markdownguide.org/basic-syntax/)
