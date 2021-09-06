from setuptools import setup

setup(
    name='click_test',
    version='0.1.0',
    py_modules=['Discord_text_edits', "TextEdit"],
    install_requires=[
        'Click', 'pyperclip', 'setuptools'
    ],
    entry_points={
        'console_scripts': [
            'disc = Discord_text_edits:cli',
        ],
    },
)
