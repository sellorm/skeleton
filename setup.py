import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="skeleton",
    version="0.0.1",
    author="Mark Sellors",
    author_email="python@example.com",
    description="A simple skeleton python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sellorm/skeletpon",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pyyaml',
        'requests',
        'importlib-metadata ~= 1.0 ; python_version < "3.8"',
    ],
)
