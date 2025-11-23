from setuptools import setup, find_packages


setup(
    name="webframe-http-client",
    version="0.1.0",
    description="A small reusable HTTP client for API automation",
    author="Aishwarya Suresh",
    packages=find_packages(exclude=("tests", "examples")),
    install_requires=["requests"],
    python_requires=">=3.9",
)

