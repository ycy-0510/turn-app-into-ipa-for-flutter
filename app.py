import os
import subprocess
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
    QMessageBox,
    QLabel,
)


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Flutter to IPA Converter For Altstore"
        self.root_dir = ""
        self.output_dir = ""
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.root_title = QLabel("Step1:", self)
        layout.addWidget(self.root_title)

        self.root_button = QPushButton("Select Flutter Project Root Directory", self)
        self.root_button.clicked.connect(self.select_root_dir)
        layout.addWidget(self.root_button)

        self.root_label = QLabel("", self)
        layout.addWidget(self.root_label)

        self.output_title = QLabel("Step2:", self)
        layout.addWidget(self.output_title)

        self.output_button = QPushButton("Select Output Directory", self)
        self.output_button.clicked.connect(self.select_output_dir)
        layout.addWidget(self.output_button)

        self.output_label = QLabel("", self)
        layout.addWidget(self.output_label)

        self.convert_title = QLabel("Step3:", self)
        layout.addWidget(self.convert_title)

        self.convert_button = QPushButton("Convert to IPA", self)
        self.convert_button.setEnabled(False)
        self.convert_button.clicked.connect(self.convert_to_ipa)
        layout.addWidget(self.convert_button)

        self.convert_label = QLabel("", self)
        layout.addWidget(self.convert_label)

        self.license_label = QLabel("Copyright 2024 YCY\nLicensed under the Apache License, Version 2.0 ",self)
        layout.addWidget(self.license_label)
        
        self.setLayout(layout)
        self.show()

    def select_root_dir(self):
        self.root_dir = QFileDialog.getExistingDirectory(
            self, "Select Flutter Project Root Directory"
        )
        if self.root_dir:
            self.root_label.setText(f"Selected: {self.root_dir}")
            if self.output_dir:
                self.convert_button.setEnabled(True)
        else:
            self.root_label.setText("")
            self.convert_button.setEnabled(False)

    def select_output_dir(self):
        self.output_dir = QFileDialog.getExistingDirectory(
            self, "Select Output Directory"
        )
        if self.output_dir:
            self.output_label.setText(f"Selected: {self.output_dir}")
            if self.root_dir:
                self.convert_button.setEnabled(True)
        else:
            self.output_label.setText("")
            self.convert_button.setEnabled(False)

    def convert_to_ipa(self):
        if not self.root_dir or not self.output_dir:
            self.convert_label.setText(
                'Error", "Please select both the root directory and the output directory.'
            )
            QMessageBox.critical(
                self,
                "Error",
                "Please select both the root directory and the output directory.",
            )
            return

        os.chdir(self.root_dir)
        self.convert_label.setText("Building IPA...")
        result = subprocess.run(
            ["flutter", "build", "ipa", "--no-codesign"], capture_output=True, text=True
        )

        if result.returncode != 0:
            QMessageBox.critical(
                self, "Error", f"Failed to build IPA:\n{result.stderr}"
            )

            return

        app_path = os.path.join(
            self.root_dir,
            "build/ios/archive/Runner.xcarchive/Products/Applications/Runner.app",
        )
        if os.path.isdir(app_path):
            os.chdir(self.output_dir)
            os.makedirs("Payload", exist_ok=True)
            subprocess.run(["cp", "-r", app_path, "Payload/"])
            subprocess.run(["zip", "-qr", "Payload.zip", "Payload"], check=True)
            os.rename("Payload.zip", "app.ipa")
            subprocess.run(["rm", "-rf", "Payload"])
            QMessageBox.information(
                self,
                "Success",
                f"app.ipa is created successfully. You can check it out in {self.output_dir}.",
            )
            self.convert_label.setText(
                f'<a href="file://{self.output_dir}/">app.ipa is created successfully. Click here to open.</a>'
            )
            self.convert_label.setOpenExternalLinks(True)
        else:
            QMessageBox.critical(self, "Error", "Runner.app does not exist.")
            self.convert_label.setText('Error", "Runner.app does not exist.')


if __name__ == "__main__":
    app = QApplication([])
    ex = App()
    app.exec_()
