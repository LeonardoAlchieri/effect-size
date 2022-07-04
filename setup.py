from setuptools import setup
# NOTE: necessary to import __version__
# exec(open("apple_heartrate_pandas/_version.py").read())

from os import path
with open(path.join(path.abspath(path.dirname(__file__)), "README.md")) as f:
    readme = f.read()

setup(
    name='affect_size',
    version="0.1.0",
    license='MIT',
    url='https://github.com/LeonardoAlchieri/affect-size',
    author='Leonardo Alchieri',
    author_email='leonardo@alchieri.eu',
    description='Some affect size methods',
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords=['affect', 'size', 'delta', 'cliff','confidence interval'],
    packages=['affect_size'],
    # py_modules=['apple_heartrate_pandas'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
    install_requires=[
    'python_version>="3.6"',
]
)