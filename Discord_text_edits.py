# run pip install --editable . for installation
# add eval "$(_DISC_COMPLETE=bash_source disc)" disc to .bashrc for auto-complete
from typing import Union, List, Tuple
from AliasedGroup import AliasedGroup
from TextEdit import TextEdit
import pyperclip
import click

_copy = bool()
_no_copy = bool()


@click.group(cls=AliasedGroup)
@click.option("--copy", "-c", is_flag=True, help="pastes the input from clipboard")
@click.option("--no-copy", "-n", is_flag=True, help="writes the output instead of copying it")
def cli(no_copy: bool, copy: bool):
    """
    This script is used for some text edits useful for Discord. You can use aliases for command names.
    """
    global _copy, _no_copy
    _copy = copy
    _no_copy = no_copy


@cli.command()
def spoiler():
    """puts every char into double vertical bar for spoilers on Discord"""
    end(TextEdit.spoiler(inp()))


@cli.command()
@click.option("--char-space", "-C", help="space between chars, default 1", default=1, type=int)
@click.option("--space-size", "-s", help="amount of space between words, default 3", default=3, type=int)
@click.option("--no-diacritics", "-d", help="removes diacritics", is_flag=True)
def emojify(char_space, space_size, no_diacritics):
    """turns every char and number into emoji character, has optional parameters"""
    end(TextEdit.emojify(inp(), char_space, space_size, not no_diacritics), True)


@cli.command()
def reverse():
    """reverses string"""
    end(TextEdit.reverse(inp()))


@cli.command()
@click.option("--max-num", "-M", help="maximum character space between lower and upper case, default 3", default=3, type=int)
@click.option("--min-num", "-m", help="minimal character space between lower and upper case, default 2", default=2, type=int)
def varied(min_num, max_num):
    """varies the chars with lower and upper case, has optional parameters"""
    try:
        end(TextEdit.varied(inp(), min_num, max_num))
    except ValueError:
        print("min-num must be lower than max-num")
        exit()


def inp() -> str:
    """
    just manages inputs for every edit
    :return: text to be edited
    """
    global _copy
    if _copy:
        return pyperclip.paste()
    else:
        return str(input("Text to edit: "))


def end(text: Union[Tuple[str, List[str]], str], emojify_trigger=False):
    def copy(a: str):
        """
        Just copies text to clipboard or writes it, depending on _no_copy.
        :param a: text to be processed
        """
        global _no_copy
        if _no_copy:
            print(a)
        else:
            pyperclip.copy(a)
            print("Copied to clipboard!")

    if emojify_trigger:
        copy(text[0])
        if text[1]:
            fail = ""
            for i in text[1]:
                fail += i + ""
            print(f"Some chars could not be converted: {fail}")
    else:
        copy(text)


if __name__ == '__main__':
    cli()
