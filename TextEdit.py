from typing import List, Tuple
from random import randint


class TextEdit:
    @staticmethod
    def spoiler(text: str) -> str:
        """
        This function puts every char into double vertical bars.

        :param text: text to add vertical bars to
        :return: result
        """
        b = ""
        for i in text:
            b += f"||{i}||"
        return b

    @staticmethod
    def emojify(text: str, char_space: int = 1, space_size: int = 3, diakritika: bool = True) -> Tuple[str, List[str]]:
        """
        Converts text to emoji form, can also remove basic diacritics.

        :param text: text to convert
        :param char_space: space size between emoji characters
        :param space_size: space size between words
        :param diakritika: determines if diacritics should be removed
        :return: returns tuple of converted text and characters that weren't converted
        """
        text = text.lower()
        if diakritika:
            # níže zmíněný slovník je k odstranění diakritiky
            preklad = str.maketrans("áéíóúýčďěňřšťžů",
                                    "aeiouycdenrstzu")
            text = text.translate(preklad)
        b = ""
        znaky = []
        for i in text:
            if i == " ":  # mezera se nahrazuje za 3 mezery pro lepší čitelnost
                b += space_size * " "
            elif i.isnumeric():  # jde o číslo
                b += i + chr(0x20e3) + char_space * " "
            elif i.isascii():  # znamená, že se jedná o znak abecedy
                b += chr(ord(i) + 127365) + char_space * " "  # posun o 127365 vypíše emoji verzi písmene
            else:  # znaky co nejsou písmena se zaznamenávají do pole
                b += i
                znaky.append(i)

        b = b[:-1]
        return b, znaky

    @staticmethod
    def varied(text: str, min_num=2, max_num=3) -> str:
        """
        Function that creates varied case for the text in random intervals. Converts text to lowercase before varying.

        :param text: text to be converted
        :param min_num: minimal character space between lower and upper case
        :param max_num: maximum character space between lower and upper case
        :return: text with varied text
        """
        b = ""
        rand = 0
        # program cyklí přes text a přes proměnou rand ukládá mezeru mezi znaky, po každém velkém písmenu se rand resetuje
        for i in text:
            if not i.isalpha():
                b += i
                continue
            elif rand:
                b += i.lower()
            else:
                b += i.upper()
                rand = randint(min_num, max_num)
            rand -= 1
        return b

    @staticmethod
    def reverse(text: str) -> str:
        """
        Reverses char order.

        :param text: input text
        :return: reversed string
        """
        a = ""
        for i in reversed(text):
            a += i
        return a
