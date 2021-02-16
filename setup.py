from setuptools import find_packages, setup

setup(
    name="project",
    version="1.0.0",
    url="https://github.com/mypackage.git",
    author="Author Name",
    author_email="author@gmail.com",
    description="Description of my package",
    packages=find_packages(),
    install_requires=["numpy >= 1.11.1", "matplotlib >= 1.5.1"],
)
