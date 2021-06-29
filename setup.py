from setuptools import setup, find_packages

setup(
    name='newsletter_tools',
    version='0.1.0',
    author='Kelvin Lee',
    description='Python functions for the AstroPAH newsletter build pipeline.',
    packages=find_packages(),
    install_requires=["ruamel.yaml"]
)
