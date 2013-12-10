from setuptools import setup, find_packages

setup(name='collectd-carbon',
      version="0.0.1",
      description='collectd plugin to write to Carbon',
      # Krux is not the canonical repo, but this setup.py was added by krux
      # and is not integrated upstream.
      url='https://github.com/krux/collectd-carbon',
      packages=find_packages(),
      )
