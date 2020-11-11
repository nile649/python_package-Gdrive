import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Gdrive_nile649", # Project_name + username = Not necessary. 
    version="0.0.8", # change version
    author="Nilesh Pandey",
    author_email="np9207@rit.edu",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nile649/Gdrive_example",
    packages=setuptools.find_packages(),
    scripts=['Gdrive/Gdrive.sh'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)