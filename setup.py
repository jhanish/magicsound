import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="magicsound", # Replace with your own username
    version="0.0.5",
    author="Joe Hanish",
    author_email="joe.hanish@gmail.com",
    description="Super simple sound player",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jhanish/magicsound",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords         = 'sound magicsound playsound music wave wav mp3 media song play audio',
    py_modules       = ['magicsound'],
)
