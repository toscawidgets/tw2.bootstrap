from setuptools import setup, find_packages

# Little hack to make 'python setup.py test' work on py2.7
try:
    import multiprocessing
    import logging
except:
    pass

tests_require=[
    'nose',
    'sieve',
    'webtest',

    # Required by tw2.core.testbase
    'formencode',

    # Templating engines
    'genshi',
    'mako',
    'jinja2',
]

setup(
    name='tw2.bootstrap.forms',
    version='2.2.0',
    description="A drop-in replacement for tw2.forms but with bootstrap!",
    long_description=open('README.rst').read(),
    author='Moritz Schlarb, Ralph Bean',
    author_email='moschlar@metalabs.de, rbean@redhat.com',
    url='http://github.com/toscawidgets/tw2.bootstrap',
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
