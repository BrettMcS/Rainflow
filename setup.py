import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cyclecount",
    version="0.1.1",
    author="Brett McSweeney",
    author_email="brett_mcs@optusnet.com.au",
    description="A python project for counting cycles in a signal using the Rainflow method",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BrettMcS/cyclecount",
    packages=setuptools.find_packages(exclude=['docs', 'tests*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)