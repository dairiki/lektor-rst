from pathlib import Path
from setuptools import setup


setup(
    name='lektor-rst',
    description='Adds reStructuredText support to Lektor.',
    long_description=(Path(__file__).parent / "README.rst").read_text(),
    long_description_content_type="text/x-rst",
    version='0.4.0',
    author=u'Florian Schulze',
    author_email='florian.schulze@gmx.net',
    url='http://github.com/fschulze/lektor-rst',
    license='MIT',
    install_requires=[
        'Lektor',
        'Pygments',
        'docutils>=0.21'],
    extras_require={
        'dev': [
            'pyquery',
            'pytest',
            'pytest-cov',
            'pytest-flake8']},
    py_modules=['lektor_rst'],
    python_requires=">=3.9",
    entry_points={
        'lektor.plugins': [
            'rst = lektor_rst:RstPlugin']})
