from setuptools import setup

setup(
    name='awesome-tech-failures',
    version='1.1.0',
    description='A machine-readable index of technology failures for AI agents.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Antigravity',
    url='https://github.com/rnzor/awesome-tech-failures',
    packages=['awesome_tech_failures'],
    package_dir={'awesome_tech_failures': 'agent'},
    package_data={
        'awesome_tech_failures': ['*.ndjson', '*.json', '*.yaml', '*.md']
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.8',
)
