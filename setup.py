import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='ubuntu_package',
    author='Vivek Narway',
    author_email='vivek.narway.19032@iitgoa.ac.in',
    description='Ubuntu Package Lab 3 Assignment',
    keywords='example, pypi, package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/narwayvivek/ubuntu-package.git',
    project_urls={
        'Documentation': 'https://github.com/narwayvivek/ubuntu-package.git',
        'Bug Reports':
        'https://github.com/narwayvivek/ubuntu-package.git/issues',
        'Source Code': 'https://github.com/narwayvivek/ubuntu-package.git',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    extras_require={
        'dev': ['check-manifest'],
    },
)
