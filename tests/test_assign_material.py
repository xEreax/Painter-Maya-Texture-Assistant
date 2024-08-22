"""
#******************************************************************
# content = Unit tests for assiging material to Maya object
# author = Edwina Asumang
#******************************************************************
"""
import os

import maya.cmds as cmds
import pytest
from PySide6.QtTest import QTest

@pytest.fixture(scope="session")
def create_maya_dir(tmp_path_factory):
    """create dir"""
    maya_dir = tmp_path_factory.mktemp("clean_maya_dir", True)
    

#TODO:tests - given that object exists

def test_should_assign_correct_texture_file_to_material():
    """TODO"""
    assert False

def test_should_assign_material_to_correct_object():
    """TODO"""
    assert False

def test_should_not_create_material_if_no_object_selected():
    """TODO"""
    assert False

def test_should_not_create_material_if_no_files_selected():
    """TODO"""
    assert False

def test_should_throw_error_message_if_texture_file_connection_fails():
    """TODO"""
    assert False

def test_should_throw_error_message_if_material_assigment_to_object_fails():
    """TODO"""
    assert False

#TODO: tests - given object doesn't exist