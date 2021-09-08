# Discord Text Edits

---

This python script allows you to do basic edits for input text
shown here:
* emojify - aka replaces chars with their emoji counterparts
* reverse - reverses text
* spoiler - puts chars into double vertical bars, effectively making every char as a spoiler in Discord
* varied - varies the case in text

## How to run and use
The main script is main.py. It can be installed by running `pip install --editable .`
in the same folder both scripts in this repo are. To use the script run main.py with `--help`
command line parametr. Some edits even get additional options which you can utilize
by running main.py with `option --help`. If an edit has options, it's mentioned in the main
`--help` text.

## Examples
Because similar effects can be achieved in markdown, here are examples:

|Edit | Result|
--- | ---
|emojify|🇪 🇲 🇴 🇯 🇮 🇫 🇾 |
|reverse|esrever|
|spoiler|\|\|s\|\|\|\|p\|\|\|\|o\|\|\|\|i\|\|\|\|l\|\|\|\|e\|\|\|\|r\|\||
|varied|VaRieD|

