# Created by GrandSir in 26.07.2020
# This game developed by GrandSir

import pathlib
path = pathlib.Path(__file__).resolve().parent
icon_path = path.joinpath("icons")
check_path = str(path.joinpath(icon_path, 'check.png')).replace("\\", "/")

stylesheet = ("QLineEdit {\n"
"background-color: rgb(27, 29, 35);\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(27, 29, 35);\n"
"padding-left: 10px;\n"
"color: rgb(180,180,180);\n"
"}\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"QToolTip {\n"
"color: #ffffff;\n"
"background-color: rgba(27, 29, 35, 160);\n"
"border: 1px solid rgb(40, 40, 40);\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton {    \n"
"border: none;\n"
"background-color: rgb(17,17,17);\n"
"border-radius: 7px;\n"
"color: rgb(255,255,255);"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {    \n"
"background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"*{\n"
"background-color: rgb(45,45,45);\n"
"}\n"
"\n"
"QCheckBox{\n"
"background-color: none;\n"
"color: rgb(255,255,255);"
"}\n"
"QCheckBox::indicator {\n"
"border: 3px solid rgb(52, 59, 72);\n"
"width: 15px;\n"
"height: 15px;\n"
"border-radius: 10px;\n"
"background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"background: 3px solid rgb(52, 59, 72);\n"
"border: 3px solid rgb(52, 59, 72);    \n"
f"background-image: url({check_path});\n"
"}\n")

