from setuptools import setup

with open('../requirements.txt') as f:
    dependencies = f.read().splitlines()

setup(
    name='sentiment-analyzer',
    version='1.0',
    packages=['', 'data', 'config', 'logger'],
    package_dir={'': 'source'},
    url='https://github.com/GeorgiosGoniotakis/sentiment-analyzer',
    license='MIT',
    author='Georgios Goniotakis',
    author_email='georgios.goniotakis@outlook.com',
    description='An advanced Sentiment Analyzer developed in Python.',
    install_requires=dependencies
)
