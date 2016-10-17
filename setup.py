from setuptools import setup

name = "py3jasperclient"
version = "0.1"

setup(
    name=name,
    version=version,
    description='JasperServer SOAP client for Python3',
    packages=['py3jasperclient', ],
    install_requires=['suds-py3'],
    url='https://github.com/tomasgarzon/pyjasperclient',
    license='Apache',
    author='Tomas Garzon',
    author_email='tomasgarzonhervas[at]gmail.com'
)
