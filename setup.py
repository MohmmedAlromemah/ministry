from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ministry/__init__.py
from ministry import __version__ as version

setup(
	name="ministry",
	version=version,
	description="it is app for MTIT",
	author="Alromimah",
	author_email="mromimah@mtit.gov.ye",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
