from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='Area of figures',
  version='0.0.1',
  author='Yegor \' iseq1 \'Mironov',
  author_email='egorka.mironov.2003@mail.com',
  description='This is the simplest module for finding the area of various shapes..',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/iseq1/Intern-Mindbox',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='area_of_figures ',
  project_urls={
    'GitHub': 'https://github.com/iseq1'
  },
  python_requires='>=3.6'
)
