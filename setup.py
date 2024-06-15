from setuptools import setup, find_packages

setup(
    name='VidLex',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'customtkinter',
        'pyinstaller'
    ],
    entry_points={
        'console_scripts': [
            'vidlex=main:main',  
        ],
    },
)
