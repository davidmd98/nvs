from setuptools import setup, find_packages

setup(
    name='nvs', 
    version='0.0.0', 
    packages=find_packages(), 
    entry_points={ 
        'console_scripts': [ 
            'demo=nvs.ex_1:main', 
            ], 
        },
    )