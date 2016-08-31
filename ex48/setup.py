try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'livefr0g',
    'url': 'URL to get it at.',
    'download_url': 'URL to download it at.',
    'author_email': 'iamlivefr0g@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
