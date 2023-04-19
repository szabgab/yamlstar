version = '0.0.1'

from setuptools import setup
import pathlib

root = pathlib.Path(__file__).parent.resolve()

long_description = \
  (root / '.long_description.md') \
  .read_text(encoding='utf-8')

setup(
  name = 'yamlstar',
  version = version,
  description = 'A cross-language, common API YAML reference framework',
  license = 'MIT',
  url = 'https://github.com/ingydotnet/yamlstar',

  author = 'Ingy döt Net',
  author_email = 'ingy@ingy.net',

  packages = ['yamlstar'],
  package_dir = {'': 'lib'},

  python_requires = '>=3.6, <4',
  install_requires = [
    'pyyaml',
  ],
  setup_requires = [
    'wheel',
  ],

  keywords = ['yaml', 'language'],
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3 :: Only',
  ],

  long_description = long_description,
  long_description_content_type = 'text/markdown',
)
