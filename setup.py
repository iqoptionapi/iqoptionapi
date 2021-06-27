"""The python wrapper for IQ Option API package setup."""
from setuptools import (setup, find_packages)

setup(name="iqoptionapi",
      version="6.8.9.1",
      packages=find_packages(),
      install_requires=["pylint", "requests", "websocket-client==0.56"],
      include_package_data=True,
      description="Best IQ Option API for python",
      long_description="Best IQ Option API for python",
      url="https://github.com/iqoptionapi/iqoptionapi",
      author="Rafael Faria",
      zip_safe=False)
