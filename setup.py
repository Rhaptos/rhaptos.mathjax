from setuptools import setup, find_packages
import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = read("rhaptos", "mathjax", "version.txt").strip()

setup(name='rhaptos.mathjax',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES").read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Rhaptos developers',
      author_email='rhaptos@cnx.rice.edu',
      url='http://rhaptos.org',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['rhaptos', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      tests_require = [
           'zope.testing>=3.5',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

