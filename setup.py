from distutils.core import setup

REQUIRED = [
    'numpy',
    'h5py',
    'python-casacore',
]
setup(name='pyrat',
      version='0.1.0.0',
      description='Python Radio Astronomy Toolkit',
      author="Michael Bell",
      author_email='mrbell@mpa-garching.mpg.de',
      packages=['pyrat'],
      package_dir={'pyrat': ''},
      install_requires=REQUIRED
)
