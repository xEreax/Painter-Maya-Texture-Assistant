#******************************************************************
# content = functions for assigning material to Maya object
# author = Edwina Asumang
#******************************************************************

import maya.cmds as cmds

texture_file_dict = {
    "BaseColor": "",
    "Emissive": "",
    "Height": "",
    "Metalness": "",
    "Normal": "",
    "Roughness": "",
}

file_to_2dtexture_baseColor_attribute_list = [
    "coverage",
    "translateFrame"
    "rotateFrame",
    "mirrorU",
    "mirrorV",
    "stagger",
    "wrapU",
    "wrapV",
    "repeatUV",
    "offset",
    "rotateUV",
    "noiseUV",
    "vertexUvOne",
    "vertexUvTwo",
    "vertexUvThree",
    "vertexCameraOne",
    ("outUV", "uv"),
    ("outUvFilterSize", "uvFilterSize"),
]

def get_current_selection_name():
    """Gets first object in current selection"""
    #TODO: Deal with case where object list is empty (no object selected)
    selected_object_name: str
    selected_objects: list = cmds.ls(selection=True, objectsOnly=True)
    if selected_objects:
        selected_object_name = selected_objects[0]
        return selected_object_name
    else:
        return ""


def populate_texture_file_dict(filenames: list):
    """Put texture file names in dictionary"""
    for filename in filenames:
        for texture_file_type in texture_file_dict:
            if texture_file_type in filename:
                texture_file_dict[texture_file_type] = filename


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


def create_base_color_file(file_path, base_color_attribute_list):
    "create file and connect attributes to 2d texture node"

    # Create file
    file_node = cmds.shadingNode("file", asTexture=True, isColorManaged=True)
    cmds.setAttr(f"{file_node}.fileTextureName", file_path, type="string")

    # Create 2dTexture
    texture_2d_node = cmds.shadingNode("place2dTexture", asUtility=True)

    # Connect file and 2dTexture attributes
    for attribute in base_color_attribute_list:
        if isinstance(attribute, str):
            cmds.connectAttr(f"{texture_2d_node}.{attribute}",
                             f"{file_node}.{attribute}",
                             force=True)
        elif isinstance(attribute, tuple):
            cmds.connectAttr(f"{texture_2d_node}.{attribute[0]}",
                             f"{file_node}.{attribute[1]}",
                             force=True)

    return file_node


def add_base_color_file_to_arnold_material(material_shader, file_node):
    """Add file to arnold material"""
    cmds.connectAttr(f"{file_node}.outColor", f"{material_shader}.baseColor", force=True)


def assign_material_to_object(material_sg, selected_object_name):
    """Assign material shader group to object"""
    cmds.sets(selected_object_name, edit=True, forceElement=material_sg)
