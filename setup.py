from setuptools import find_packages, setup

setup(
    name='scratch_downloader',
    packages=find_packages(include=["scratch_downloader"]),
    version='0.1.0',
    description='Download Scratch (www.scratch.mit.edu) SB3 files',
    long_description=open('README.md').read(),
    author='Secret-chest',
    license='Apache-2.0',
    install_requires=["httpx"],
)
