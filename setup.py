import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MockQuerPy-peakBreaker",
    version="0.0.1",
    author="peakbreaker",
    author_email="andershurum@gmail.compile",
    description="A google bigquery client library mocker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/peakbreaker/MockQuerPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
