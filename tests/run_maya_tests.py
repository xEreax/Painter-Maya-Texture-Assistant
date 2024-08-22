import os
import sys

import maya.standalone
import maya.cmds as cmds

#import pytest

def run_tests(venv_path):
    """run tests"""
    #'C:\\Program Files\\Autodesk\\Maya2024\\Python\\lib\\site-packages'
    try:
        print(sys.path)
        if venv_path:
            venv_package_path = os.path.join(venv_path, "Lib", "site-packages")
            if venv_package_path not in sys.path:
                sys.path.append(venv_path)
                sys.path.append(venv_package_path)
                print(sys.path)
                import pytest
    except ImportError:
        print("pytest import failed")
        
    # maya.standalone.initialize()
    # test_file = os.path.join(os.getcwd(), "tests", "test_assign_material.py")

    # pytest.main([test_file])


    # if float(cmds.about(v=True)) >= 2016.0:
    #     maya.standalone.uninitialize()

if __name__ == "__main__":
    run_tests(sys.argv[1])

