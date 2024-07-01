from setuptools import setup, find_packages

setup(
    name='hitranXCreader',
    version='1.0.0',
    url=None,#'https://github.com/mypackage.git',
    author='Everett Schlawin',
    author_email='granfalloontoyballoon@hotmail.com',
    description='Read hitran cross section files',
    packages=find_packages(),
    install_requires=['numpy >= 1.11.1'],
)