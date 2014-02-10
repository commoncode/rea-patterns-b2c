from setuptools import setup, find_packages

setup( name='rea-patterns-b2c',
    version = '0.0.1',
    description = 'B2C Economic REA Patterns for REA and Economica',
    author = 'Daryl Antony',
    author_email = 'daryl@commoncode.com.au',
    url = 'https://github.com/commoncode/rea-patterns-b2c',
    keywords = ['django',],
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    dependency_links = [
        'http://github.com/commoncode/rea/tarball/master#egg=rea-0.0.1',
        'http://github.com/commoncode/cqrs/tarball/master#egg=cqrs-0.0.1',
    ],
    install_requires = [
        'rea',
        'cqrs',
    ],
)
