# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OutputFolderStructureEditor.ui'
#
# Created: Sat Jan 27 23:55:42 2018
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(427, 459)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btnUnderscore = QtGui.QPushButton(Dialog)
        self.btnUnderscore.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnUnderscore.setObjectName(_fromUtf8("btnUnderscore"))
        self.gridLayout.addWidget(self.btnUnderscore, 11, 2, 1, 1)
        self.btnNumberOfPlayers = QtGui.QPushButton(Dialog)
        self.btnNumberOfPlayers.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnNumberOfPlayers.setObjectName(_fromUtf8("btnNumberOfPlayers"))
        self.gridLayout.addWidget(self.btnNumberOfPlayers, 8, 0, 1, 1)
        self.btnHyphen = QtGui.QPushButton(Dialog)
        self.btnHyphen.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnHyphen.setObjectName(_fromUtf8("btnHyphen"))
        self.gridLayout.addWidget(self.btnHyphen, 11, 1, 1, 1)
        self.btnSlash = QtGui.QPushButton(Dialog)
        self.btnSlash.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnSlash.setObjectName(_fromUtf8("btnSlash"))
        self.gridLayout.addWidget(self.btnSlash, 11, 0, 1, 1)
        self.btnType = QtGui.QPushButton(Dialog)
        self.btnType.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnType.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.btnType.setObjectName(_fromUtf8("btnType"))
        self.gridLayout.addWidget(self.btnType, 9, 0, 1, 1)
        self.btnGenre = QtGui.QPushButton(Dialog)
        self.btnGenre.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnGenre.setObjectName(_fromUtf8("btnGenre"))
        self.gridLayout.addWidget(self.btnGenre, 9, 1, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.btnZXDB_ID = QtGui.QPushButton(Dialog)
        self.btnZXDB_ID.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnZXDB_ID.setObjectName(_fromUtf8("btnZXDB_ID"))
        self.gridLayout.addWidget(self.btnZXDB_ID, 6, 3, 1, 1)
        self.txtOutputFileNameStructure = QtGui.QLineEdit(Dialog)
        self.txtOutputFileNameStructure.setText(_fromUtf8(""))
        self.txtOutputFileNameStructure.setObjectName(_fromUtf8("txtOutputFileNameStructure"))
        self.gridLayout.addWidget(self.txtOutputFileNameStructure, 3, 0, 1, 4)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 14, 1, 1, 3)
        self.txtOutputFolderStructure = QtGui.QLineEdit(Dialog)
        self.txtOutputFolderStructure.setObjectName(_fromUtf8("txtOutputFolderStructure"))
        self.gridLayout.addWidget(self.txtOutputFolderStructure, 1, 0, 1, 4)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 12, 0, 1, 1)
        self.lblExample = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblExample.sizePolicy().hasHeightForWidth())
        self.lblExample.setSizePolicy(sizePolicy)
        self.lblExample.setMinimumSize(QtCore.QSize(0, 100))
        self.lblExample.setMidLineWidth(5)
        self.lblExample.setText(_fromUtf8(""))
        self.lblExample.setScaledContents(False)
        self.lblExample.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblExample.setWordWrap(True)
        self.lblExample.setIndent(10)
        self.lblExample.setObjectName(_fromUtf8("lblExample"))
        self.gridLayout.addWidget(self.lblExample, 13, 0, 1, 4)
        self.btnPublisher = QtGui.QPushButton(Dialog)
        self.btnPublisher.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnPublisher.setObjectName(_fromUtf8("btnPublisher"))
        self.gridLayout.addWidget(self.btnPublisher, 6, 2, 1, 1)
        self.btnModFlags = QtGui.QPushButton(Dialog)
        self.btnModFlags.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnModFlags.setObjectName(_fromUtf8("btnModFlags"))
        self.gridLayout.addWidget(self.btnModFlags, 8, 1, 1, 1)
        self.btnGameName = QtGui.QPushButton(Dialog)
        self.btnGameName.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnGameName.setObjectName(_fromUtf8("btnGameName"))
        self.gridLayout.addWidget(self.btnGameName, 6, 0, 1, 1)
        self.btnNotes = QtGui.QPushButton(Dialog)
        self.btnNotes.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnNotes.setObjectName(_fromUtf8("btnNotes"))
        self.gridLayout.addWidget(self.btnNotes, 8, 2, 1, 1)
        self.btnFormat = QtGui.QPushButton(Dialog)
        self.btnFormat.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnFormat.setObjectName(_fromUtf8("btnFormat"))
        self.gridLayout.addWidget(self.btnFormat, 9, 2, 1, 1)
        self.btnCountry = QtGui.QPushButton(Dialog)
        self.btnCountry.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnCountry.setObjectName(_fromUtf8("btnCountry"))
        self.gridLayout.addWidget(self.btnCountry, 7, 2, 1, 1)
        self.btnLanguage = QtGui.QPushButton(Dialog)
        self.btnLanguage.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnLanguage.setObjectName(_fromUtf8("btnLanguage"))
        self.gridLayout.addWidget(self.btnLanguage, 7, 1, 1, 1)
        self.btnYear = QtGui.QPushButton(Dialog)
        self.btnYear.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnYear.setObjectName(_fromUtf8("btnYear"))
        self.gridLayout.addWidget(self.btnYear, 7, 0, 1, 1)
        self.btnOriginalName = QtGui.QPushButton(Dialog)
        self.btnOriginalName.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnOriginalName.setObjectName(_fromUtf8("btnOriginalName"))
        self.gridLayout.addWidget(self.btnOriginalName, 6, 1, 1, 1)
        self.btnMedia = QtGui.QPushButton(Dialog)
        self.btnMedia.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnMedia.setObjectName(_fromUtf8("btnMedia"))
        self.gridLayout.addWidget(self.btnMedia, 8, 3, 1, 1)
        self.btnMachineType = QtGui.QPushButton(Dialog)
        self.btnMachineType.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnMachineType.setObjectName(_fromUtf8("btnMachineType"))
        self.gridLayout.addWidget(self.btnMachineType, 9, 3, 1, 1)
        self.btnLetter = QtGui.QPushButton(Dialog)
        self.btnLetter.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnLetter.setObjectName(_fromUtf8("btnLetter"))
        self.gridLayout.addWidget(self.btnLetter, 11, 3, 1, 1)
        self.btnAuthor = QtGui.QPushButton(Dialog)
        self.btnAuthor.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnAuthor.setObjectName(_fromUtf8("btnAuthor"))
        self.gridLayout.addWidget(self.btnAuthor, 7, 3, 1, 1)
        self.gridLayout.setRowStretch(13, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.txtOutputFolderStructure, self.txtOutputFileNameStructure)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Edit output folder structure", None))
        self.btnUnderscore.setText(_translate("Dialog", "Underscore(_)", None))
        self.btnNumberOfPlayers.setToolTip(_translate("Dialog", "1P for 1 player, 2P for 2 players etc.", None))
        self.btnNumberOfPlayers.setText(_translate("Dialog", "{MaxPlayers}", None))
        self.btnHyphen.setText(_translate("Dialog", "Hyphen ( - )", None))
        self.btnSlash.setText(_translate("Dialog", "Slash (\\)", None))
        self.btnType.setToolTip(_translate("Dialog", "Games, Applications, Educational, Compilations etc.", None))
        self.btnType.setText(_translate("Dialog", "{Type}", None))
        self.btnGenre.setToolTip(_translate("Dialog", "Action Game, Adventure Game, General - Education etc.", None))
        self.btnGenre.setText(_translate("Dialog", "{Genre}", None))
        self.label.setText(_translate("Dialog", "Output folder structure pattern:", None))
        self.btnZXDB_ID.setToolTip(_translate("Dialog", "game ID as in ZXDB, 0000000 for games not in ZXDB", None))
        self.btnZXDB_ID.setText(_translate("Dialog", "{ZXDB_ID}", None))
        self.label_3.setText(_translate("Dialog", "Output file name structure pattern:", None))
        self.label_2.setText(_translate("Dialog", "Examples:", None))
        self.btnPublisher.setToolTip(_translate("Dialog", "Software publisher", None))
        self.btnPublisher.setText(_translate("Dialog", "{Publisher}", None))
        self.btnModFlags.setToolTip(_translate("Dialog", "[cr]- cracked, [f] - fixed, [h]  hacked, [m] - moded, [p] - pirated, [t] - trainer, [tr] - translation", None))
        self.btnModFlags.setText(_translate("Dialog", "{ModFlags}", None))
        self.btnGameName.setToolTip(_translate("Dialog", "Software release name", None))
        self.btnGameName.setText(_translate("Dialog", "{GameName}", None))
        self.btnNotes.setToolTip(_translate("Dialog", "Square brackets [] contents which is not mod flags", None))
        self.btnNotes.setText(_translate("Dialog", "{Notes}", None))
        self.btnFormat.setToolTip(_translate("Dialog", "Original file extension", None))
        self.btnFormat.setText(_translate("Dialog", "{Format}", None))
        self.btnCountry.setToolTip(_translate("Dialog", "Release country", None))
        self.btnCountry.setText(_translate("Dialog", "{Country}", None))
        self.btnLanguage.setToolTip(_translate("Dialog", "Message language", None))
        self.btnLanguage.setText(_translate("Dialog", "{Language}", None))
        self.btnYear.setToolTip(_translate("Dialog", "Release year", None))
        self.btnYear.setText(_translate("Dialog", "{Year}", None))
        self.btnOriginalName.setToolTip(_translate("Dialog", "Original file name (without extension)", None))
        self.btnOriginalName.setText(_translate("Dialog", "{OriginalName}", None))
        self.btnMedia.setToolTip(_translate("Dialog", "Tape 1 of 3 Side A, Disk 1 of 2 etc.", None))
        self.btnMedia.setText(_translate("Dialog", "{Media}", None))
        self.btnMachineType.setToolTip(_translate("Dialog", "48K, 128K, +2, +2A, +3, Timex, Pentagon etc.", None))
        self.btnMachineType.setText(_translate("Dialog", "{MachineType}", None))
        self.btnLetter.setToolTip(_translate("Dialog", "First letter of game name or \'123\' if starts from digit", None))
        self.btnLetter.setText(_translate("Dialog", "{Letter}", None))
        self.btnAuthor.setToolTip(_translate("Dialog", "Software publisher", None))
        self.btnAuthor.setText(_translate("Dialog", "{Author}", None))

