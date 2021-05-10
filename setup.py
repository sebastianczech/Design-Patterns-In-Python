from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='design-patterns',
    version='0.1.0',
    description='Design patterns in Python',
    long_description=readme,
    author='Sebastian Czech',
    author_email='sebaczech@gmail.com',
    url='https://github.com/sebastianczech/Design-Patterns-In-Python',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)