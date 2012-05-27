from setuptools import setup, find_packages

# Little hack to make 'python setup.py test' work on py2.7
try:
    import multiprocessing
    import logging
except:
    pass

setup(
    name='tw2.bootstrap',
    version='0.1',
    description="A drop-in replacement for tw2.forms but with bootstrap!",
    long_description=open('README.md').read(),
    author='Moritz Schlarb',
    author_email='mail@moritz-schlarb.de',
    url='',
    install_requires=[
        "tw2.core",
        "tw2.forms",
        "tw2.jquery",
        ## Add other requirements here
        # "Genshi",
        ],
    packages=find_packages(exclude=['ez_setup', 'tests']),
    namespace_packages=['tw2'],
    zip_safe=False,
    include_package_data=True,
    test_suite = 'nose.collector',
    tests_require=[
        'nose',

        # Required by tw2.core.testbase
        'formencode',
        'BeautifulSoup',
        'strainer',
        'webtest',

        # Templating engines
        'genshi',
        'mako',
        'jinja2',
        'kajiki',
        'genshi',
    ],
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets = tw2.bootstrap
    """,
    keywords = [
        'toscawidgets.widgets',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
