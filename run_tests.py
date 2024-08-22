# ******************************************************************
# content = setup and execution of test environment
# author = Edwina Asumang
# ******************************************************************

import os
import sys
import subprocess
import click


def get_maya_path(maya_version: int):
    """Get path where Maya is installed on system.

    Note: only support for Windows system at the moment
    """
    return f'C:/Program Files/Autodesk/Maya{maya_version}'


def get_mayapy_exe_path(maya_version_number: int):
    """Get executable mayapy path on system.

    Note: only support for Windows system at the moment
    """
    return f'C:/Program Files/Autodesk/Maya{maya_version_number}/bin/mayapy.exe'


def create_clean_maya_dir():
    """Make new directory for tests."""
    dir_path = os.path.join(os.getcwd(), 'clean_maya_dir')


def setup_maya_tests(maya_version_number: int):
    """Setup to run Maya tests."""
    mayapy_exe_path = get_mayapy_exe_path(maya_version_number)
    if not os.path.exists(mayapy_exe_path):
        raise RuntimeError('mayapy path could not be found')
    test_setup_filename = os.path.join(
        os.getcwd(),
        'tests',
        'run_maya_tests.py',
    )
    unit_test_setup_path = os.path.join(os.getcwd(), test_setup_filename)

    try:
        # check if in virtual environment
        print(sys.prefix == sys.base_prefix)
        subprocess.run([mayapy_exe_path, unit_test_setup_path, sys.prefix], check=True)
    except subprocess.CalledProcessError:
        pass


@click.command()
@click.option(
    '-m',
    '--maya_version_number',
    type=int, required=True,
    help='Version number of Maya installed on machine',
)
def test_main(maya_version_number):
    """Get command line arguments."""
    setup_maya_tests(maya_version_number)


if __name__ == '__main__':
    test_main()
