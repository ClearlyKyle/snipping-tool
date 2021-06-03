import sys
from PyQt5.QtCore import QPoint, Qt, QRect
from PyQt5.QtWidgets import QAction, QMainWindow, QApplication, QPushButton, QMenu, QFileDialog, QDialog, QGroupBox, QFormLayout, QDialogButtonBox
from PyQt5 import QtWidgets

class AnkiImageImport(QDialog):
    def __init__(self):
        super(AnkiImageImport, self).__init__()

        self.CreateFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.StartButtonFunction)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)

        self.setFixedWidth(300)
        self.setFixedHeight(200)

        self.setLayout(mainLayout)
        self.setWindowTitle("Anki Picture Importer - Settings")

    def CreateFormGroupBox(self):
        self.formGroupBox = QGroupBox("Settings")
        layout = QFormLayout()

        btn = QPushButton("...")
        btn.clicked.connect(self.GetFile)
        btn.setMaximumWidth(20)
        hbox = QtWidgets.QHBoxLayout()

        # Ankiconnect URL
        self.ankiconnect_url = QtWidgets.QLineEdit()
        self.ankiconnect_url.setReadOnly(False)

        layout.addRow(QtWidgets.QLabel("Url:"), hbox)
        hbox.addWidget(self.ankiconnect_url)
        hbox.addWidget(btn)
        
        # Decks
        self.deck_comboBox = QtWidgets.QComboBox()
        self.deck_comboBox.addItems(["test1", "test2", "test3"])
        layout.addRow(QtWidgets.QLabel("Deck:"), self.deck_comboBox)

        # Model
        self.model_comboBox = QtWidgets.QComboBox()
        self.model_comboBox.addItems(["test1", "test2", "test3"])
        layout.addRow(QtWidgets.QLabel("Model:"), self.model_comboBox)

        # Fields
        self.fields_comboBox = QtWidgets.QComboBox()
        layout.addRow(QtWidgets.QLabel("Field:"), self.fields_comboBox)
        self.model_comboBox.currentTextChanged.connect(self.UpdateFields)
        self.UpdateFields()

        # Check Boxes
        hbox = QtWidgets.QHBoxLayout()
        self.subdirectory_checkbox = QtWidgets.QCheckBox("Search Subdirectories")
        self.subdirectory_checkbox.setChecked(False)
        self.subdirectory_checkbox.toggled.connect(self.SubDirCheckBoxClicked)
        hbox.addWidget(self.subdirectory_checkbox, 0, Qt.AlignCenter)
        layout.addRow(hbox)

        self.formGroupBox.setLayout(layout)

    def GetFile(self):
        pass
        #self.subdirectory_checkbox.setEnabled(False)

        ## Get path to Image Folder
        #self.folderpath = QFileDialog.getExistingDirectory(self, "Select Folder")
        ## showInfo("folderpath\n{}".format(self.folderpath))

        #if self.folderpath == "":
        #    return  # No path selected

        #self.file_path_box.setText(self.folderpath)

        #self.GetFilePaths(self.folderpath)

        #self.subdirectory_checkbox.setEnabled(True)

    def GetFilePaths(self, folder_path):
        pass
        #self.image_paths = []
        #for path, subdirs, files in os.walk(folder_path):
        #    for image_name in files:
        #        if image_name.lower().endswith((".png", ".jpg", ".jpeg")):
        #            self.image_paths.append(os.path.join(path, image_name))

        #    if self.subdirectory_checkbox.isChecked() is False:
        #        break

        #self.formGroupBox.setTitle("{} images found".format(len(self.image_paths)))

    def SubDirCheckBoxClicked(self):
        pass
        #if self.folderpath == "":
        #    return  # No path selected

        #self.subdirectory_checkbox.setEnabled(False)
        #self.GetFilePaths(self.folderpath)
        #self.subdirectory_checkbox.setEnabled(True)

    def UpdateFields(self):
        pass
        # self.fields_comboBox.clear()

        # selected_model = mw.col.models.byName(self.model_comboBox.currentText())

        # list of fields for selected note type
        # fields = mw.col.models.fieldNames(selected_model)
        # self.fields_comboBox.addItems(fields)

    def StartButtonFunction(self):
        pass
        #selected_deck = self.deck_comboBox.currentText()
        #selected_model = self.model_comboBox.currentText()
        #selected_field = self.fields_comboBox.currentText()

        ## Set the model
        #set_model = mw.col.models.byName(selected_model)
        #mw.col.decks.current()["mid"] = set_model["id"]

        ## Get the deck
        #self.deck = mw.col.decks.byName(selected_deck)

        ## Fields
        #fields = mw.col.models.fieldMap(set_model)
        #self.field_index = fields[selected_field][0]

        ## Start Processing New Cards
        ## self.hide()
        #self.GenerateNewCards()
        ## self.show()

    def GenerateNewCards(self):
        pass
        #progress = QProgressDialog(self, Qt.WindowTitleHint)    # remove "?" hint button
        #progress.setWindowModality(Qt.ApplicationModal)
        #progress.setLabelText("Generating Cards from Images...")
        #progress.setMaximum(100)
        #progress.setMinimumDuration(0)      # time delay before showing progress bar
        #progress.setCancelButton(None)      # remove cancel button
        #progress.setMinimumWidth(350)       # window width
        #progress.setAutoClose(True)         # close after 100%

        #progress.setValue(0)
        #progress.setValue(1)
        #progress.setValue(0)

        #progressbar_steps = 100 / len(self.image_paths)

        #for idx, image_path in enumerate(self.image_paths):
        #    # Write image to collection.media folder and return its new Filename
        #    new_filename = mw.col.media.add_file(image_path)

        #    # Create a new Note to add image to
        #    new_note = mw.col.newNote()
        #    new_note.model()["did"] = self.deck["id"]

        #    image_field = '<img src="' + new_filename + '" />'
        #    new_note.fields[self.field_index] = image_field

        #    mw.col.addNote(new_note)

        #    # progressbar.setValue(idx * progressbar_steps)
        #    progress.setValue((idx + 1) * progressbar_steps)

        #    if(progress.wasCanceled()):
        #        break

        #    time.sleep(0.05)

        #mw.col.save()
        #showInfo("Sucess!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = AnkiImageImport()
    dialog.exec_()