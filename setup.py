from setuptools import setup
setup(
    name = 'fffcli',
    version = '0.1.0',
    packages = ['fffcli'],
    entry_points = {
        'console_scripts': [
            'fffcli = fffcli.__main__:main'
        ]
    })