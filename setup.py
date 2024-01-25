from setuptools import setup, find_packages

setup(
    name='Tic Tac Toe with AI',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A implementation of the popular game "Tic Tac Toe" with a minimax algorithm.',
    long_description=open('README.md').read(),
    install_requires=['pytest', 'coverage'],
    url='https://github.com/PedroDiSanti/tic_tac_toe_with_ai',
    author='Pedro Di Santi',
    author_email='-'
)
