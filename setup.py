from setuptools import setup, find_packages

setup(
    name='sphinxcontrib-robotframework',
    version='0.4.4',
    description='Robot Framework extension for Sphinx',
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.txt").read()),
    url='http://github.com/datakurre/sphinxcontrib_robotframework',
    author='Asko Soukka',
    author_email='asko.soukka@iki.fi',
    license='GPL',
    py_modules=[
        'sphinxcontrib_robotframework'
    ],
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Pygments >= 1.6',
        'Sphinx',
        'robotframework >= 2.8.0',
    ],
    extras_require={'docs': [
        'robotframework',
        'robotframework-selenium2library',
        'robotframework-selenium2screenshots [Pillow] >= 0.5.0',
    ]}
)
