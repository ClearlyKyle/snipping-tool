
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QGroupBox, QFormLayout, QDialogButtonBox
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QSettings

import AnkiConnect as ak


class AnkiSettingsWindow(QDialog):
    def __init__(self, parent=None):
        super(AnkiSettingsWindow, self).__init__(parent=parent)

        self.field_names = ""

        self.settings = QSettings("AnkiSettings", "App1")
        self.Anki = ak.AnkiConnect()
        self.CreateFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel)
        buttonBox.addButton("save", QDialogButtonBox.ActionRole)
        buttonBox.accepted.connect(self.SaveSettings)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)

        self.setFixedWidth(300)
        self.setFixedHeight(200)

        self.setLayout(mainLayout)
        self.setWindowTitle("Anki Picture Importer - Settings")

        try:
            self.SetComboBoxText(self.deck_comboBox, self.settings.value("deck name"))
            self.SetComboBoxText(self.model_comboBox, self.settings.value("model name"))
            self.SetComboBoxText(self.fields_comboBox, self.settings.value("field name"))
            if self.settings.value("anki url") is not None:
                self.anki_url.setText(self.settings.value("anki url"))

        except ValueError():
            print("Error Loading Settings from \"QSettings\"")
            return

        self.show()

    def CreateFormGroupBox(self):
        self.formGroupBox = QGroupBox("Settings")
        layout = QFormLayout()

        # Ankiconnect URL
        self.anki_url = QtWidgets.QLineEdit("http://127.0.0.1:8765")
        layout.addRow(QtWidgets.QLabel("URL:"), self.anki_url)

        # Decks
        self.deck_comboBox = QtWidgets.QComboBox()
        self.deck_names = self.GetDeckNames()
        self.deck_comboBox.addItems(self.deck_names)
        layout.addRow(QtWidgets.QLabel("Deck:"), self.deck_comboBox)

        # Model
        self.model_comboBox = QtWidgets.QComboBox()
        self.model_names = self.GetModelNames()
        self.model_comboBox.addItems(self.model_names)
        layout.addRow(QtWidgets.QLabel("Model:"), self.model_comboBox)

        # Fields
        self.fields_comboBox = QtWidgets.QComboBox()
        # self.fields_comboBox.addItems(["test1", "test2"])
        layout.addRow(QtWidgets.QLabel("Field:"), self.fields_comboBox)
        self.model_comboBox.currentTextChanged.connect(self.UpdateFields)
        self.UpdateFields()

        # Check Boxes
        hbox = QtWidgets.QHBoxLayout()
        self.subdirectory_checkbox = QtWidgets.QCheckBox("Clear on Sucess")
        self.subdirectory_checkbox.setChecked(False)
        self.subdirectory_checkbox.toggled.connect(self.ClearImageOnSucess)
        hbox.addWidget(self.subdirectory_checkbox, 0, Qt.AlignCenter)
        layout.addRow(hbox)

        self.formGroupBox.setLayout(layout)

    def GetDeckNames(self):
        return self.Anki.invoke("deckNames")

    def GetModelNames(self):
        return self.Anki.invoke("modelNames")

    def UpdateFields(self):
        selected_name = self.model_comboBox.currentText()
        self.field_names = self.Anki.invoke("modelFieldNames", modelName=selected_name)
        self.fields_comboBox.addItems(self.field_names)

    def ClearImageOnSucess(self):
        pass

    def SaveSettings(self):
        print("Saving Settings")
        self.settings.setValue("deck name", self.deck_comboBox.currentText())
        self.settings.setValue("model name", self.model_comboBox.currentText())
        self.settings.setValue("field name", self.fields_comboBox.currentText())
        self.settings.setValue("anki url", self.anki_url.text())

    def SetComboBoxText(self, combo, text):
        index = combo.findText(text, Qt.MatchFixedString)
        if index >= 0:
            combo.setCurrentIndex(index)

    def GetCardSettings(self):
        deck_name = self.settings.value("deck name")
        model_name = self.settings.value("model name")
        field_name = self.settings.value("field name")

        return [deck_name, model_name, field_name]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = AnkiSettingsWindow()
    dialog.exec_()
