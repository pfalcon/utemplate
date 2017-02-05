from setuptools import setup
import optimize_upip


setup(name='utemplate',
      version='1.0',
      description="""Very lightweight, memory-efficient (uses generator
protocol), dependency-free template engine (compiles to Python source).
Particularly well suited for usage with MicroPython.org""",
      url='https://github.com/pfalcon/utemplate',
      author='Paul Sokolovsky',
      author_email='pfalcon@users.sourceforge.net',
      license='MIT',
      cmdclass={'optimize_upip': optimize_upip.OptimizeUpip},
      packages=['utemplate'])
