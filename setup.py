from setuptools import setup
import sdist_upip


setup(name='utemplate',
      version='1.3',
      description="""Very lightweight, memory-efficient, dependency-free template engine (compiles to Python source).""",
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      url='https://github.com/pfalcon/utemplate',
      author='Paul Sokolovsky',
      author_email='pfalcon@users.sourceforge.net',
      license='MIT',
      cmdclass={'sdist': sdist_upip.sdist},
      packages=['utemplate'])
