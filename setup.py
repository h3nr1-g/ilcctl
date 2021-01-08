import os
import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 0):
    print('ilcctl requires Python 3')
    exit(-1)


def get_requirements():
    with open('requirements.txt') as fh:
        return [req for req in fh.readlines() if not req.startswith('-')]


def get_release_version():
    git_tag = os.environ.get('GIT_TAG', '0.1')
    ci_job_number = os.environ.get('BUILD_NUMBER', '1')
    return '%s.%s' % (git_tag, ci_job_number)


if __name__ == '__main__':
    setup(
        name='ilcctl',
        version=get_release_version(),
        description='Package for controlling iLC RGB Bluetooth light bulbs',
        packages=find_packages(exclude=['tests']),
        include_package_data=True,
        install_requires=get_requirements(),
        entry_points='''
            [console_scripts]
            ilcctl=ilcctl.ilcctl:cli
        '''
    )
