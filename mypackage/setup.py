from setuptools import setup, find_packages
with open("../README.md", "r") as fh:
    long_description=fh.read()
setup(

    name="mypackage",

    version="0.1.0",

    packages=find_packages(),

    author="Aditya Garhwal",

    author_email="adityagarhwal00@gmail.com",

    description="A simple example package",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="https://cloudsmith.io/interview-aditya-choudhary/testrepo/mypackage",

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

    python_requires='>=3.6',

)
