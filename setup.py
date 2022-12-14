from setuptools import find_packages, setup

setup(
    name='scratch_downloader',
    packages=find_packages(include=["scratch_downloader"]),
    version='1.0.0-rc',
    description='Download Scratch (www.scratch.mit.edu) SB3 files',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Secret-chest',
    license='Apache-2.0',
    install_requires=["httpx"],
)
