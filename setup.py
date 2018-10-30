from setuptools import setup

setup(name='monitoring_smithclent',
      version='0.1',
      description='Monitoring Smith client',
      url='',
      author='Denis Gavrilin',
      author_email='dangavrilin@gmail.com',
      license='MIT',
      packages=['client'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
