#!/usr/bin/env python3

"""The setup script."""

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().strip().split('\n')

with open('README.md') as f:
    long_description = f.read()
setup(
    maintainer='Open Radar Team',
    maintainer_email='',
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
    ],
    description='Provides utility functions for accessing data repository for Project Pythia examples/notebooks',
    install_requires=requirements,
    license='MIT',
    long_description_content_type='text/markdown',
    long_description=long_description,
    include_package_data=True,
    package_data={'open_radar_data': ['registry.txt']},
    keywords='Radar, Pooch',
    name='open-radar-data',
    packages=find_packages(include=['open_radar_data', 'open_radar_data.*']),
    entry_points={},
    url='https://github.com/openradar/open-radar-data',
    project_urls={
        'Documentation': 'https://github.com/openradar/open-radar-data',
        'Source': 'https://github.com/openradar/open-radar-data',
        'Tracker': 'https://github.com/openradar/open-radar-data/issues',
    },
    use_scm_version={
        'version_scheme': 'post-release',
        'local_scheme': 'dirty-tag',
    },
    setup_requires=['setuptools_scm', 'setuptools>=30.3.0'],
    zip_safe=False,
)
