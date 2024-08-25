# ParrotSay

ParrotSay is a Cowsay clone written in Python, using a parrot (or other custom ASCII art) instead of a cow.

## Features

- Makes an ASCII parrot "speak"
- Supports custom ASCII art
- Creates a speech bubble with the provided text

## Usage

### Basic Syntax

```python parrotSay.py "<text>" [custom_art_file]```

- `<text>`: The string that the parrot (or custom art) should "say" (mandatory)
- `custom_art_file`: Name of the .txt file containing custom ASCII art (optional)

### Examples

1. Basic usage with the default parrot:

```python parrotSay.py "Hello"```

This command will make the default parrot say "Hello".

2. Usage with custom art:

```python parrotSay.py "Hello" "example.txt"```

This command will make the ASCII art contained in `example.txt` (in this case, a horse) "say" "Hello".

## Custom Art

To use custom ASCII art:

1. Create a .txt file containing your ASCII art
2. Save the file in the `customTxtFolder` directory
3. Use the filename as the third argument when running the program

## Notes

- Ensure your custom ASCII art is formatted to leave space for the speech bubble with text
- The program will automatically insert the provided text in a comic-like speech bubble

## Contributing

You're welcome to contribute to this project! You can do so by:

- Reporting bugs
- Suggesting new features
- Submitting pull requests with code improvements or new features

## License

See LICENSE file