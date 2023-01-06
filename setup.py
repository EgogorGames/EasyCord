from setuptools import setup, find_packages


setup(
    name='easycord',
    version='0.6',
    license='MIT',
    author="EgogorGames",
    author_email='egogorgames@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/EgogorGames/EasyCord',
    keywords='easycord',
    install_requires=[
          'scikit-learn',
      ],

)
