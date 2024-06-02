#******************************************************************
# content = functions for assigning material to Maya object
# author = Edwina Asumang
#******************************************************************

# Functions to create
# get object, listen to maya selection
# get/store name of object (or pointer to object)
# Retrieve files
# save list/dict of files {base_color: <file_path>, ...}
# get name of object and file paths
# Create arnold material THEN assign to object THEN add files
# OR
# Create arnold material THEN add files THEN assign to object

import maya.cmds as cmds


def get_current_selection_name():
    """Gets first object in current selection"""
    #TODO: Deal with case where object list is empty (no object selected)
    selected_object_name: str
    selected_objects: list = cmds.ls(selection=True, objectsOnly=True)
    if selected_objects:
        selected_object_name = selected_objects[0]
    return selected_object_name


def display_current_selection_name(selection_name: str):
    """Display selected object name"""
    #TODO: Set ui to selection name
    return True

#exr file type
texture_file_dict = {
    "BaseColor": "",
    "Emissive": "",
    "Height": "",
    "Metalness": "",
    "Normal": "",
    "Roughness": "",
}


def get_project_directory():
    """Get directory of project"""
    #TODO: Get directory to project location
    return True


def populate_texture_file_dict(filenames: list):
    """Put texture file names in dictionary"""
    for filename in filenames:
        for texture_file_type in texture_file_dict:
            if texture_file_type in filename:
                texture_file_dict[texture_file_type] = filename


def display_texture_files():
    """Display texture files"""
    #TODO: Display file names in ui
    return True


def create_arnold_material_shader(selected_object_name: str):
    """Create AI Arnold Surface material shader"""
    # Create aiStandard material
    material_name="aiStandardSurface"
    shader = cmds.shadingNode(material_name,
                              asShader=True,
                              name=f"{selected_object_name}_{material_name}")

    # Create surface shader group
    sg = cmds.sets(renderable=True,
                   noSurfaceShader=True,
                   empty=True,
                   name=f"{selected_object_name}_{material_name}SG")

    # Connect material to shader
    cmds.connectAttr(f"{shader}.outColor", f"{sg}.surfaceShader", force=True)

    return sg


def add_files_to_arnold_material(material_shader, file_path):
    """Create file and add to arnorld material"""
    # Note: Dealing with only baseColor currently

    # Create file
    file_node = cmds.shadingNode("file", asTexture=True, isColorManaged=True)
    cmds.setAttr(f"{file_node}.fileTextureName", file_path, type="string")

    #TODO: Connect file to a 2d texture node

    # Connect base color texture file to aiStandardSurface base color
    cmds.connectAttr(f"{file_node}.outColor", f"{material_shader}.baseColor", force=True)


def assign_shader_to_object(sg, selected_object_name):
    """Assign shader group to object"""
    cmds.sets(selected_object_name, edit=True, forceElement=sg)
