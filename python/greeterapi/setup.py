import io
import os
import setuptools


dependencies = ["docopt==0.6.2", "grpcio>=1.20.1"]

extras = {}

# Boilerplate below this line
about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "greeterapi", "__version__.py")) as fp:
    exec(fp.read(), about)

readme_filename = os.path.join(here, "README.rst")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

# Namespaces are nice when distributing many
packages = [
    package
    for package in setuptools.find_packages()
    if package.startswith("greeterapi")
]

setuptools.setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/x-rst",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    classifiers=[
        about["__release_status__"],
        "Intended Audience :: Developers",
        "Unlicensed",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    platforms="Posix; MacOS X; Windows",
    packages=packages,
    install_requires=dependencies,
    extras_require=extras,
    python_requires=">2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*",
    entry_points={"console_scripts": ["greeterapi=greeterapi.cli:main"]},
    zip_safe=False,
)
