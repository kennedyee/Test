from setuptools import setup, find_packages

setup(
    name = 'MyPackage',
    version = '0.1',
    packages = find_packages(exclude= ['tests']),
    license='MIT',
    description='My first package',
    long_description=open('Readme.md').read(),
    install_requires=['numpy'],
    url='https://github.com/kennedyee',
    author='Kennedyee',
    author_email='chegekennedyee@gmail.com'
)
