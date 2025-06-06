GeezType is a dynamic Amharic keyboard engine that enables fast and intuitive typing in Amharic script on your computer. It uses real-time transliteration and a customizable mapping system to convert phonetic Latin input into Amharic syllabary, making it ideal for both native speakers and learners.

## Features

- **Dynamic Transliteration:** Instantly convert Latin phonetic input to Amharic script.
- **Customizable Mapping:** Easily modify or extend the key-to-syllable mapping via a JSON config.
- **Toggle Typing:** Enable or disable Amharic typing on the fly.
- **Cross-Platform Support:** Works on Windows, macOS, and Linux (requires Python).
- **Lightweight:** Minimal dependencies for smooth performance.

## Installation

1. Clone the repository or download the source code.
2. Install the required Python packages:
    ```bash
    pip install keyboard pynput
    ```
3. Ensure `geez_map.json` (the mapping file) is present in the same directory as `amharic_typing.py`.

## Usage

Run the engine:

```bash
python app.py
```

Once running, start typing using Latin characters. The engine will automatically convert your input to Amharic script based on the mapping. You can toggle Amharic typing on or off as needed.

## Configuration

- **Key Mapping:** Edit `geez_map.json` to customize how Latin keys map to Amharic syllables.
- **Vowel Order:** The engine uses a predefined order for vowels (`A`, `u`, `i`, `a`, `y`, `e`, `o`).

## Contributing

Contributions are welcome! Please open issues or submit pull requests for bug fixes, features, or improvements.

## License

This project is licensed under the MIT License.