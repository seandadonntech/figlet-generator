from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'for brute forcing'
LONG_DESCRIPTION = ' A PACKAGE TO HELP YOU GENERATE FIGLET TEXT WITH PYTHON.'

# Setting up
setup(
    name="blunt force",
    version=0.1,
    author="seandadonntech",
    author_email="lilcryptotech@gmail.com",
    description=DESCRIPTION,
    long_description_content_type= "a package that helps you brute force" ,

    
    long_description=long_description,
    packages=find_packages(),
    install_requires=['colorama', 'random', 'pyaudio'],
    keywords=['python', 'random', 'stream', 'fun', 'TEXT', 'sockets','pyfiglet'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
