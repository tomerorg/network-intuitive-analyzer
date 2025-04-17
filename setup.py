
from setuptools import setup, find_packages

setup(
    name="network-intuitive-analyzer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "pandas>=1.2.0",
        "numpy>=1.20.0",
    ],
    author="",
    author_email="",
    description="Network service implementing Celery and Django and SQLAlchemy architecture",
    keywords="network-intuitive-analyzer, python",
    url="",
)
