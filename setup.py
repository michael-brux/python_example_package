from setuptools import setup, find_packages

setup(
    name='python_example_package',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
    ],
    entry_points={
        'console_scripts': [
            # Define command-line scripts here
        ],
    },
)
