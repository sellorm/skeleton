# Build, package and release

Install the `build` package to perform the build:

```
python3 -m pip install build
```

Remember to bump the version number in `setup.py`, then run:

```
python3 -m build
```

You can install the locally built version with:

(remember to change the `packagename` and version to match your new package!)

```
python3 -m pip install dist/packagename-0.0.1.tar.gz
```

And then, when you're happy, upload with:

```
python3 -m twine upload dist/packagename-0.0.1*
```

This process will require you have a working PyPI.org account.
You can sign up [here](https://pypi.org/account/register/).

This information is mostly distilled from the
[official docs](https://packaging.python.org/tutorials/packaging-projects/).
