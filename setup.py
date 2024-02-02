# setup.py
from setuptools import setup

setup(
    name='ezlister',
    version='0.1.0',
    py_modules=['ezlister', 'dirlister', 'sublister'],  # Specify your Python modules here
    package_data={
        '': ['directory_wordlists/*', 'subdomain_wordlists/*'],
    },
    include_package_data=True,  # This tells setuptools to include any data files specified in package_data
    install_requires=[
        'requests',
        'pyfiglet',
        'argparse; python_version<"3.2"'  # Only needed for Python versions older than 3.2
    ],
    entry_points={
        'console_scripts': [
            'ezlister=ezlister:main',  # Refers to the main function in ezlister.py
        ],
    },
    author='Yassin Habib',
    description='A simple tool for listing directories and subdomains',     
    keywords='web directory subdomain scanner',
    url='https://github.com/yhabib05/ezlister',
)

 