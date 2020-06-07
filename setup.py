from setuptools import setup
setup(
    name = 'sonos',
    version = '0.1.0',
    packages = ['sonos'],
    entry_points = {
        'console_scripts': [
            'sonos = sonos.__main__:main'
        ]
    })