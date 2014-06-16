from setuptools import setup


setup(name='utemplate',
      version='0.2.5',
      description="""Very lightweight, memory-efficient (uses generator
protocol), dependency-free template engine (compiles to Python source).
Particularly well suited for usage with MicroPython.org""",
      url='https://github.com/pfalcon/utemplate',
      author='Paul Sokolovsky',
      author_email='pfalcon@users.sourceforge.net',
      license='MIT',
      packages=['utemplate'])
