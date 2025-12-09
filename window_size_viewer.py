"""Interactive viewer to observe requested vs actual Kivy window size.

Usage (after activating the venv):
    ./.venv/bin/python3 window_size_viewer.py --width 1400 --height 900

Options:
  --width/--height: values sent to Kivy Config before Window import
  --fullscreen: request fullscreen via Config
  --borderless: request a borderless window via Config

The app shows the requested size, `Window.size`, and `Window.system_size`
inside the window and also prints them to stdout whenever they change.
"""

from __future__ import annotations

import argparse
import os

# Prevent Kivy from consuming custom CLI args (must be set before any Kivy import).
os.environ.setdefault("KIVY_NO_ARGS", "1")

from kivy.config import Config


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--width", type=int, default=1200, help="Requested width")
    parser.add_argument("--height", type=int, default=1600, help="Requested height")
    parser.add_argument(
        "--fullscreen", action="store_true", help="Request fullscreen via Config"
    )
    parser.add_argument(
        "--borderless", action="store_true", help="Request borderless window"
    )
    return parser.parse_args()


args = parse_args()

# Apply graphics settings before importing Window.
Config.set("graphics", "width", str(args.width))
Config.set("graphics", "height", str(args.height))
if args.fullscreen:
    Config.set("graphics", "fullscreen", "1")
if args.borderless:
    Config.set("graphics", "borderless", "1")

from kivy.app import App  # noqa: E402  (must follow Config)
from kivy.clock import Clock  # noqa: E402
from kivy.core.window import Window  # noqa: E402
from kivy.uix.label import Label  # noqa: E402
from kivy.uix.boxlayout import BoxLayout  # noqa: E402


class SizeViewerApp(App):
    def __init__(self, requested_size, **kwargs):
        super().__init__(**kwargs)
        self.requested_size = requested_size
        self.label = None

    def build(self):
        root = BoxLayout()
        self.label = Label(halign="left", valign="middle")
        self.label.bind(size=self._resize_text)
        root.add_widget(self.label)

        Window.bind(size=self._on_window_size_change, system_size=self._on_system_size)

        # Populate once the window is ready.
        Clock.schedule_once(lambda *_: self._report("initial"))
        return root

    def _resize_text(self, instance, _value):
        instance.text_size = instance.size

    def _on_window_size_change(self, *args):
        self._report("Window.size change")

    def _on_system_size(self, *args):
        self._report("Window.system_size change")

    def _report(self, reason):
        requested = self.requested_size
        actual = tuple(Window.size)
        system = tuple(getattr(Window, "system_size", Window.size))

        diff_actual = (actual[0] - requested[0], actual[1] - requested[1])
        diff_system = (system[0] - requested[0], system[1] - requested[1])

        info_lines = [
            f"Reason: {reason}",
            f"Requested (Config): {requested}",
            f"Window.size       : {actual}  Δ: {diff_actual}",
            f"Window.system_size: {system}  Δ: {diff_system}",
            f"DPI: {getattr(Window, 'dpi', 'unknown')}",
        ]
        info = "\n".join(info_lines)

        if self.label:
            self.label.text = info

        # Mirror to stdout for terminal visibility.
        print(info)


def main():
    requested = (
        Config.getint("graphics", "width"),
        Config.getint("graphics", "height"),
    )
    SizeViewerApp(requested_size=requested).run()


if __name__ == "__main__":
    main()
