#******************************************************************
# content = setup and execution of tests
# author = Edwina Asumang
#******************************************************************

import os
import click

def get_maya_path(maya_version: int):
    """Get path where Maya is installed on system
       Note: only support for Windows system at the moment
    """
    return f"C:/Program Files/Autodesk/Maya{maya_version}"

def get_mayapy_path(maya_version_number: int):
    """Get executable mayapy path on system
       Note: only support for Windows system at the moment
    """
    return f"C:/Program Files/Autodesk/Maya{maya_version_number}/bin/mayapy.exe"

def create_clean_maya_dir():
    """make new directory for tests"""


def run_maya_tests(maya_version_number: int):
    """Run Maya tests"""
    mayapy_path = get_mayapy_path(maya_version_number)
    if not os.path.exists(mayapy_path):
        raise RuntimeError('mayapy path could not be found')


@click.command()
@click.option('-m', '--maya_version_number', type=int, required=True, help="Version number of Maya installed on machine")
def test_main(maya_version_number):
    """get command line arguments"""
    run_maya_tests(maya_version_number)