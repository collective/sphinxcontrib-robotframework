from setuptools import setup

setup(
    name='sphinxcontrib-robotframework',
    version=open('VERSION').read().strip(),
    description='Robot Framework extension for Sphinx',
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGELOG.rst").read()),
    url='http://github.com/datakurre/sphinxcontrib_robotframework',
    author='Asko Soukka',
    author_email='asko.soukka@iki.fi',
    license='GPL',
    zip_safe=True,
    py_modules=[
        'sphinxcontrib_robotframework'
    ],
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
