#******************************************************************
# content = assigns Arnold material to Maya object
# author = Edwina Asumang
#******************************************************************

import maya.cmds as cmds
from PySide2.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFileDialog, QToolBox, QPushButton, QLabel, QLineEdit
from PySide2.QtCore import Qt



class AssignSubstanceTexturesWindow(QMainWindow):
    """UI"""

    def __init__(self):
        super().__init__()

        self.filenames: list
        self.texture_file_dict = {
            "BaseColor": "",
            "Emissive": "",
            "Height": "",
            "Metalness": "",
            "Normal": "",
            "Roughness": "",
        }

        # Set up main window
        main_widget = QWidget()
        self.setWindowTitle("Assign Substance Textures")
        self.setCentralWidget(main_widget)
        self.main_layout = QVBoxLayout(main_widget)

        def change_selected_object():
            selected_object_name: str = get_current_selection_name()
            self.selected_maya_object.setText(selected_object_name)

        # Create event listener for updating the selected object
        self.selection_change_listener = cmds.scriptJob(event=["SelectionChanged", change_selected_object])


        def add_labelled_widget_row(layout: QVBoxLayout, widget_list: list, label_text: str):
            hbox = QHBoxLayout()
            label = QLabel(label_text)
            hbox.addWidget(label)
            for widget in widget_list:
                hbox.addWidget(widget)
            layout.addLayout(hbox)

        def get_current_selection_name() -> str:
            """Gets first object in current selection"""
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
                for texture_file_type in self.texture_file_dict:
                    if texture_file_type in filename:
                        self.texture_file_dict[texture_file_type] = filename

        def display_files():
            self.base_color_file.setText(self.texture_file_dict["BaseColor"])
            self.emissive_file.setText(self.texture_file_dict["Emissive"])
            self.height_file.setText(self.texture_file_dict["Height"])
            self.metalness_file.setText(self.texture_file_dict["Metalness"])
            self.normal_file.setText(self.texture_file_dict["Normal"])
            self.roughness_file.setText(self.texture_file_dict["Roughness"])


        def open_file_selection_dialog():
            dialog = QFileDialog(self)
            dialog.setFileMode(QFileDialog.ExistingFiles)
            dialog.setNameFilter("Images (*.exr)")

            if dialog.exec():
                self.filenames = dialog.selectedFiles()
                populate_texture_file_dict(self.filenames)
                print(self.texture_file_dict)
                display_files()
            #TODO: decide action if no file selected https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QFileDialog.html#PySide6.QtWidgets.QFileDialog.selectedFiles

        # Display Maya object heading
        self.maya_object_section_heading = QLabel("Maya Object", alignment=Qt.AlignVCenter)
        self.main_layout.addWidget(self.maya_object_section_heading)

        # Display selected Maya object name
        self.selected_maya_object = QLineEdit()
        initial_selected_object_name: str = get_current_selection_name()
        self.selected_maya_object.setClearButtonEnabled(True)
        self.selected_maya_object.setText(initial_selected_object_name)
        add_labelled_widget_row(self.main_layout,
                                [self.selected_maya_object],
                                "Selected Object:")

        # Display texture files and options heading
        self.texture_section_heading = QLabel("Texture Files and Options",
                                              alignment=Qt.AlignVCenter)
        self.main_layout.addWidget(self.texture_section_heading)

        # Display button to select all files
        self.select_multiple_files_button = QPushButton("Select files")
        self.select_multiple_files_button.clicked.connect(open_file_selection_dialog)
        self.main_layout.addWidget(self.select_multiple_files_button)

        # Display base color texture file
        self.base_color_file = QLineEdit()
        self.select_base_color_file_button = QPushButton("...")
        self.select_base_color_file_button.clicked.connect(open_file_selection_dialog)
        add_labelled_widget_row(self.main_layout, [self.base_color_file,
                                                   self.select_base_color_file_button],
                                                   "Base Color:")
        # Display emissive texture file
        self.emissive_file = QLineEdit()
        self.select_emissive_file_button = QPushButton("...")
        self.select_emissive_file_button.clicked.connect(open_file_selection_dialog)
        add_labelled_widget_row(self.main_layout, [self.emissive_file,
                                                   self.select_emissive_file_button],
                                                   "Emissive:")
        # Display height texture file
        self.height_file = QLineEdit()
        self.select_height_file_button = QPushButton("...")
        self.select_height_file_button.clicked.connect(open_file_selection_dialog)
        add_labelled_widget_row(self.main_layout, [self.height_file,
                                                   self.select_height_file_button],
                                                   "Height:")
        # Display metalness texture file
        self.metalness_file = QLineEdit()
        self.select_metalness_file_button = QPushButton("...")
        self.select_metalness_file_button.clicked.connect(open_file_selection_dialog)
        add_labelled_widget_row(self.main_layout, [self.metalness_file,
                                                   self.select_metalness_file_button],
                                                   "Metalness:")
        # Display normal texture file
        self.normal_file = QLineEdit()
        self.select_normal_file_button = QPushButton("...")
        self.select_normal_file_button.clicked.connect(open_file_selection_dialog)
        add_labelled_widget_row(self.main_layout, [self.normal_file,
                                                   self.select_normal_file_button],
                                                   "Normal:")
        # Display roughness texture file
        self.roughness_file = QLineEdit()
        self.select_roughness_file_button = QPushButton("...")
        self.select_roughness_file_button.clicked.connect(open_file_selection_dialog)
        add_labelled_widget_row(self.main_layout, [self.roughness_file,
                                                   self.select_roughness_file_button],
                                                   "Roughness:")
    
    def closeEvent(self, event):
        # Stop selection change event listener
        cmds.scriptJob(kill=self.selection_change_listener)
        super().closeEvent(event)
        event.accept()


def create_widget():
    """Display widget"""
    widget = AssignSubstanceTexturesWindow()
    widget.resize(800, 600)
    widget.show()