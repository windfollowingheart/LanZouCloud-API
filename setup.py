import setuptools

from lanzou_windfollowingheart.api import version

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="lanzou-api-windfollowingheart",
    version=version,
    author="zaxtyson, follower: windfollowingheart",
    author_email="2916311184@qq.com",
    description="LanZouCloud API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/windfollowingheart/LanZouCloud-API",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
        "requests_toolbelt"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
