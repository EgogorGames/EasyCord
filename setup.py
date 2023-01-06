from setuptools import setup, find_packages

readme = ''
with open('README.rst') as f:
    readme = f.read()

setup(
      name='esycord',
      version='1.1.3',
      license='MIT',
      description="EasyCord - Python module for much easier creating discord bots on python!",
      author="EgogorGames",
      author_email="egogorgamescontact@gmail.com",
      long_description=readme,
      long_description_content_type="text/x-rst",
      packages=find_packages('src'),
      package_dir={'': 'src'},
      url='https://github.com/EgogorGames/EasyCord',
      keywords='esycord',
      install_requires=[
            'discord',
            'datetime',
            'discord_webhook'
      ],
      python_requires=">=3.8.0",
      project_urls={
        "Documentation": "https://docs.egogorgames.com/esycord/",
      },
      classifiers=[
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Topic :: Internet',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Libraries :: Python Modules'
      ]
)