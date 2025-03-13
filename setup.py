"""The python wrapper for IQ Option API package setup."""
from setuptools import setup, find_packages
from iqoptionapi.version_control import api_version

setup(
    name="iqoptionapi",
    version=api_version,
    packages=find_packages(),
    install_requires=["pylint", "requests", "websocket-client==0.56", "openpyxl"],
    include_package_data=True,
    description="Best IQ Option API for python",
    long_description="Best IQ Option API for python",
    url="https://github.com/wujileee/iqoptionapi.git",
    author="Wuji Lee",
    author_email='wujiofc@gmail.com',
    zip_safe=False
)
