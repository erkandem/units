from distutils.core import setup
import sys
import units

if '--doctest-modules' not in sys.argv:
  setup(name='units',
        version=units.__version__,
        description="Python support for quantities with units",
        long_description=units.__doc__,
        author=units.__author__,
        author_email=units.__contact__,
        license=units.__license__,
        url='https://bitbucket.org/adonohue/units/',
        classifiers=["Development Status :: 4 - Beta",
                     "Intended Audience :: Developers",
                     "Intended Audience :: Science/Research",
                     "Intended Audience :: System Administrators",
                     "License :: OSI Approved :: Python Software Foundation License",
                     "Natural Language :: English",
                     "Operating System :: OS Independent",
                     "Programming Language :: Python",
                     "Topic :: Scientific/Engineering",
                     "Topic :: Software Development :: Libraries :: Python Modules",
                     "Topic :: Utilities"],
        packages=['units', 'units.tests'],
        platforms=["all"],
        provides=['units'],
        )
