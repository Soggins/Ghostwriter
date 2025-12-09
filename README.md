# Ghostwriter

A lightweight GUI application that automatically types text after a customizable delay. Perfect for automation tasks, testing, or demonstrations.

## Features

- **Simple GUI Interface**: User-friendly tkinter-based application
- **Customizable Delay**: Set the delay time (in seconds) before text is automatically typed
- **Auto-type Functionality**: Uses `pyautogui` to simulate keyboard input
- **Status Feedback**: Real-time countdown and status updates during operation

## Requirements

- Python 3.13+
- `pyautogui>=0.9.54`

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or if using `uv`:
   ```bash
   uv sync
   ```

## Usage

Run the application with:
```bash
python main.py
```

### How to Use

1. **Enter Text**: Type the text you want to auto-type in the first input field
2. **Set Delay**: Specify the delay time in seconds (default: 5 seconds)
3. **Click Ghostwrite**: Click the "Ghostwrite" button to start
4. A countdown will appear before the text is automatically typed

## Building an Executable

To create a standalone executable file:

```bash
pyinstaller --noconfirm --onefile --windowed --name "Ghostwriter" main.py
```

The executable will be created in the `dist/` folder as `Ghostwriter` (on Linux/Mac) or `Ghostwriter.exe` (on Windows).

## Project Structure

```
AutoWrite/
├── main.py          # Entry point
├── autowrite.py     # Core application logic
├── pyproject.toml   # Project dependencies
└── README.md        # This file
```

## Notes

- The application requires `pyautogui` which may need additional system dependencies on Linux (e.g., `scrot` for certain features)
- The delay countdown starts from your specified value and counts down to 0 before typing begins
- The button becomes re-enabled after typing is complete

## License

MIT
