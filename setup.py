import sys

from setuptools import setup, find_packages

# Little hack to make 'python setup.py test' work on py2.7
try:
    import multiprocessing
    import logging
except:
    pass

# Requirements to install buffet plugins and engines
_extra_genshi = ["Genshi >= 0.3.5"]
_extra_mako = ["Mako >= 0.1.1"]
_extra_jinja = ["Jinja2"]

tests_require = [
    #'BeautifulSoup',
    'nose',
    'sieve',
] + _extra_mako

if sys.version_info[0] == 2 and sys.version_info[1] <= 5:
    tests_require.append('WebTest<2.0')
else:
    tests_require.append('WebTest')

if sys.version_info[0] < 3:
    tests_require.append('FormEncode')

setup(
    name='tw2.bootstrap.forms',
    version='2.2.2.1',
    description="A drop-in replacement for tw2.forms but with bootstrap!",
    long_description=open('README.rst').read(),
    author='Moritz Schlarb, Ralph Bean & contributors',
    author_email='toscawidgets-discuss@googlegroups.com',
    url="http://toscawidgets.org/",
    download_url="https://pypi.python.org/pypi/tw2.bootstrap.forms/",
    license='BSD 2-clause',
    install_requires=[
        "tw2.core",
        "tw2.forms",
        "tw2.jquery",

        "six",

        ## Add other requirements here
        # "Genshi",
        ],
    packages=find_packages(exclude=['ez_setup', 'tests']),
    namespace_packages=[
        'tw2',
        'tw2.bootstrap',
    ],
    zip_safe=False,
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=tests_require,
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets = tw2.bootstrap.forms
    """,
    keywords=[
        'toscawidgets.widgets',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
    ],
)
