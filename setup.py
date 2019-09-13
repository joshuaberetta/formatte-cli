import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="formatte-cli-joshuaberetta",
    version="0.0.1",
    author="Joshua Beretta",
    author_email="joshuaberetta@gmail.com",
    description="A small example package to test formatting from CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joshuaberetta/formatte-cli",
    packages=['formatte'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['pandas'],
    entry_points={'console_scripts': ['formatte = formatte.cli.main:main']}
)
