try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Example 47 Project for LPTHW',
    'author': 'livefr0g',
    'url': 'URL to get it at.',
    'download_url': 'URL to download it at.',
    'author_email': 'iamlivefr0g@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
