"""Small helper to compare requested vs actual Kivy window sizes.

This script sets the graphics width/height via `Config` before importing
`Window`, then prints the requested size alongside `Window.size` and
`Window.system_size` to illustrate any scaling or clamping applied by the
window provider.
"""

from kivy.config import Config

# Request a larger window size before importing Window.
Config.set("graphics", "width", "1200")
Config.set("graphics", "height", "1600")

from kivy.core.window import Window  # noqa: E402  (must be imported after Config)


def main():
    requested = (
        Config.getint("graphics", "width"),
        Config.getint("graphics", "height"),
    )
    actual = tuple(Window.size)
    system = tuple(getattr(Window, "system_size", Window.size))

    print(f"Requested size (Config): {requested}")
    print(f"Window.size reported   : {actual}")
    print(f"Window.system_size     : {system}")
    print(f"Difference (Window vs requested): "
          f"({actual[0] - requested[0]}, {actual[1] - requested[1]})")
    print(f"Difference (system vs requested): "
          f"({system[0] - requested[0]}, {system[1] - requested[1]})")


if __name__ == "__main__":
    main()
