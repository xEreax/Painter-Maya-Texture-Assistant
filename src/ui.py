#******************************************************************
# content = UI for user to select Maya object and texture files
# author = Edwina Asumang
#******************************************************************

import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFileDialog, QToolBox, QPushButton, QLabel, QLineEdit
from PySide6.QtCore import Qt


class AssignSubstanceTexturesWindow(QMainWindow):
    """UI"""
    def __init__(self):
        super().__init__()

        self.filenames: list

        # Main window
        main_widget = QWidget()
        self.setWindowTitle("Assign Substance Textures")
        self.setCentralWidget(main_widget)
        self.main_layout = QVBoxLayout(main_widget)

        def add_labelled_widget_row(layout: QVBoxLayout, widget_list: list, label_text: str):
            hbox = QHBoxLayout()
            label = QLabel(label_text)
            hbox.addWidget(label)
            for widget in widget_list:
                hbox.addWidget(widget)
            layout.addLayout(hbox)

        def open_file_selection_dialog():
            dialog = QFileDialog(self)
            dialog.setFileMode(QFileDialog.ExistingFiles)
            dialog.setNameFilter("Images (*.exr)")

            if dialog.exec():
                self.filenames = dialog.selectedFiles() #TODO: check if url may be better option
            #TODO: decide action if no file selected https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QFileDialog.html#PySide6.QtWidgets.QFileDialog.selectedFiles
            #TODO: handle case - only one file should be selected
            #TODO: Populate line edits with file names

        # Display selected Maya object name
        self.maya_object_section_heading = QLabel("Maya Object", alignment=Qt.AlignVCenter)
        self.main_layout.addWidget(self.maya_object_section_heading)
        self.selected_maya_object = QLineEdit()
        add_labelled_widget_row(self.main_layout,
                                [self.selected_maya_object],
                                "Selected Object:")

        # Display selected texture files and options
        self.texture_section_heading = QLabel("Texture Files and Options",
                                              alignment=Qt.AlignVCenter)
        self.main_layout.addWidget(self.texture_section_heading)

        # Display button to select all files
        self.select_multiple_files_button = QPushButton("Select files")
        self.select_multiple_files_button.clicked.connect(open_file_selection_dialog)
        self.main_layout.addWidget(self.select_multiple_files_button)

        # Display base color texture file
        self.base_color_file = QLineEdit()
        self.select_file_button = QPushButton("...")
        self.select_file_button.clicked.connect(open_file_selection_dialog)
        add_labelled_widget_row(self.main_layout, [self.base_color_file,
                                                   self.select_file_button],
                                                   "Base Color:")


def create_widget():
    """Display widget"""
    app = QApplication([])
    widget = AssignSubstanceTexturesWindow()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    create_widget()
