from setuptools import setup, find_packages

setup(
    name                          = 'OpenDart',
    version                       = '0.0.2',
    description                   = '전자공시 OPEN DART 시스템 API',
    long_description              = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    author                        = 'jihogrammer',
    author_email                  = 'jihogrammer@gmail.com',
    license                       = 'MIT',
    packages                      = find_packages(),
    install_requires              = ['python-dotenv', 'requests', 'xmltodict'],
    classifiers                   = [
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
)
