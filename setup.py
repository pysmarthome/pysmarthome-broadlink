from setuptools import setup, find_packages

setup(
    name='pysmarthome-broadlink',
    description='Broadlink plugin for pysmarthome',
    version='1.1.0',
    author='Filipe Alves',
    author_email='filipe.alvesdefernando@gmail.com',
    install_requires=[
        'pysmarthome~=2.1',
        'broadlink',
    ],
    packages=find_packages(),
    url='https://github.com/filipealvesdef/pysmarthome-broadlink',
    zip_zafe=False,
)
