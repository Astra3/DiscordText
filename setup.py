from setuptools import setup

setup(
    name='click_test',
    version='0.1.0',
    py_modules=['main', "TextEdit"],
    install_requires=[
        'Click', 'pyperclip', 'setuptools'
    ],
    entry_points={
        'console_scripts': [
            'disc = main:cli',
        ],
    },
)
