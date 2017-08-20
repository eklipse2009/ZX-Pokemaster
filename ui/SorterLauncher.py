# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SorterLauncher.ui'
#
# Created: Mon Aug 21 00:19:36 2017
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
        Dialog.resize(500, 550)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(500, 550))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Dialog.setBaseSize(QtCore.QSize(0, 0))
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/pokemaster.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        Dialog.setSizeGripEnabled(False)
        self.gridLayout_3 = QtGui.QGridLayout(Dialog)
        self.gridLayout_3.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnLoadSettings = QtGui.QPushButton(Dialog)
        self.btnLoadSettings.setObjectName(_fromUtf8("btnLoadSettings"))
        self.horizontalLayout.addWidget(self.btnLoadSettings)
        self.btnSaveSettings = QtGui.QPushButton(Dialog)
        self.btnSaveSettings.setObjectName(_fromUtf8("btnSaveSettings"))
        self.horizontalLayout.addWidget(self.btnSaveSettings)
        spacerItem = QtGui.QSpacerItem(158, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnSortFiles = QtGui.QPushButton(Dialog)
        self.btnSortFiles.setObjectName(_fromUtf8("btnSortFiles"))
        self.horizontalLayout.addWidget(self.btnSortFiles)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabMainOptions = QtGui.QWidget()
        self.tabMainOptions.setAccessibleName(_fromUtf8(""))
        self.tabMainOptions.setObjectName(_fromUtf8("tabMainOptions"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabMainOptions)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.tabMainOptions)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btnAddPath = QtGui.QPushButton(self.groupBox)
        self.btnAddPath.setObjectName(_fromUtf8("btnAddPath"))
        self.gridLayout_2.addWidget(self.btnAddPath, 0, 1, 1, 1)
        self.chkTraverseSubdirectories = QtGui.QCheckBox(self.groupBox)
        self.chkTraverseSubdirectories.setChecked(True)
        self.chkTraverseSubdirectories.setObjectName(_fromUtf8("chkTraverseSubdirectories"))
        self.gridLayout_2.addWidget(self.chkTraverseSubdirectories, 3, 0, 1, 1)
        self.lstInputPaths = QtGui.QListWidget(self.groupBox)
        self.lstInputPaths.setObjectName(_fromUtf8("lstInputPaths"))
        self.gridLayout_2.addWidget(self.lstInputPaths, 0, 0, 3, 1)
        self.btnRemovePaths = QtGui.QPushButton(self.groupBox)
        self.btnRemovePaths.setObjectName(_fromUtf8("btnRemovePaths"))
        self.gridLayout_2.addWidget(self.btnRemovePaths, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.tabMainOptions)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.txtOutputPath = QtGui.QLineEdit(self.tabMainOptions)
        self.txtOutputPath.setObjectName(_fromUtf8("txtOutputPath"))
        self.horizontalLayout_2.addWidget(self.txtOutputPath)
        self.btnBrowseOutputPath = QtGui.QToolButton(self.tabMainOptions)
        self.btnBrowseOutputPath.setObjectName(_fromUtf8("btnBrowseOutputPath"))
        self.horizontalLayout_2.addWidget(self.btnBrowseOutputPath)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.groupBox_2 = QtGui.QGroupBox(self.tabMainOptions)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cmbOutputPathStructure = QtGui.QComboBox(self.groupBox_2)
        self.cmbOutputPathStructure.setEditable(False)
        self.cmbOutputPathStructure.setProperty("currentText", _fromUtf8(""))
        self.cmbOutputPathStructure.setObjectName(_fromUtf8("cmbOutputPathStructure"))
        self.gridLayout.addWidget(self.cmbOutputPathStructure, 0, 0, 1, 4)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.btnRemovePattern = QtGui.QPushButton(self.groupBox_2)
        self.btnRemovePattern.setObjectName(_fromUtf8("btnRemovePattern"))
        self.gridLayout.addWidget(self.btnRemovePattern, 1, 2, 1, 1)
        self.btnAddPattern = QtGui.QPushButton(self.groupBox_2)
        self.btnAddPattern.setObjectName(_fromUtf8("btnAddPattern"))
        self.gridLayout.addWidget(self.btnAddPattern, 1, 0, 1, 1)
        self.btnEditPattern = QtGui.QPushButton(self.groupBox_2)
        self.btnEditPattern.setObjectName(_fromUtf8("btnEditPattern"))
        self.gridLayout.addWidget(self.btnEditPattern, 1, 1, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.chkMaxFilesPerFolder = QtGui.QCheckBox(self.tabMainOptions)
        self.chkMaxFilesPerFolder.setObjectName(_fromUtf8("chkMaxFilesPerFolder"))
        self.horizontalLayout_6.addWidget(self.chkMaxFilesPerFolder)
        self.txtMaxFilesPerFolder = QtGui.QSpinBox(self.tabMainOptions)
        self.txtMaxFilesPerFolder.setEnabled(False)
        self.txtMaxFilesPerFolder.setMaximum(999999999)
        self.txtMaxFilesPerFolder.setProperty("value", 255)
        self.txtMaxFilesPerFolder.setObjectName(_fromUtf8("txtMaxFilesPerFolder"))
        self.horizontalLayout_6.addWidget(self.txtMaxFilesPerFolder)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.chkCamelCase = QtGui.QCheckBox(self.tabMainOptions)
        self.chkCamelCase.setFocusPolicy(QtCore.Qt.NoFocus)
        self.chkCamelCase.setObjectName(_fromUtf8("chkCamelCase"))
        self.verticalLayout_2.addWidget(self.chkCamelCase)
        self.chkShortFilenames = QtGui.QCheckBox(self.tabMainOptions)
        self.chkShortFilenames.setFocusPolicy(QtCore.Qt.NoFocus)
        self.chkShortFilenames.setObjectName(_fromUtf8("chkShortFilenames"))
        self.verticalLayout_2.addWidget(self.chkShortFilenames)
        self.chkPlacePokFilesIntoPOKESSubfolders = QtGui.QCheckBox(self.tabMainOptions)
        self.chkPlacePokFilesIntoPOKESSubfolders.setChecked(True)
        self.chkPlacePokFilesIntoPOKESSubfolders.setObjectName(_fromUtf8("chkPlacePokFilesIntoPOKESSubfolders"))
        self.verticalLayout_2.addWidget(self.chkPlacePokFilesIntoPOKESSubfolders)
        self.verticalLayout_2.setStretch(0, 2)
        self.tabWidget.addTab(self.tabMainOptions, _fromUtf8(""))
        self.tabFileFiltering = QtGui.QWidget()
        self.tabFileFiltering.setObjectName(_fromUtf8("tabFileFiltering"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tabFileFiltering)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.tabFileFiltering)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.txtFormatPreference = QtGui.QLineEdit(self.tabFileFiltering)
        self.txtFormatPreference.setInputMask(_fromUtf8(""))
        self.txtFormatPreference.setObjectName(_fromUtf8("txtFormatPreference"))
        self.horizontalLayout_3.addWidget(self.txtFormatPreference)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.tabFileFiltering)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.txtLanguages = QtGui.QLineEdit(self.tabFileFiltering)
        self.txtLanguages.setInputMask(_fromUtf8(""))
        self.txtLanguages.setObjectName(_fromUtf8("txtLanguages"))
        self.horizontalLayout_4.addWidget(self.txtLanguages)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.chkIncludeAlternate = QtGui.QCheckBox(self.tabFileFiltering)
        self.chkIncludeAlternate.setObjectName(_fromUtf8("chkIncludeAlternate"))
        self.verticalLayout.addWidget(self.chkIncludeAlternate)
        self.chkIncludeDemos = QtGui.QCheckBox(self.tabFileFiltering)
        self.chkIncludeDemos.setChecked(True)
        self.chkIncludeDemos.setObjectName(_fromUtf8("chkIncludeDemos"))
        self.verticalLayout.addWidget(self.chkIncludeDemos)
        self.chkIncludeRereleases = QtGui.QCheckBox(self.tabFileFiltering)
        self.chkIncludeRereleases.setChecked(True)
        self.chkIncludeRereleases.setObjectName(_fromUtf8("chkIncludeRereleases"))
        self.verticalLayout.addWidget(self.chkIncludeRereleases)
        self.chkIncludeAlternateFileFormats = QtGui.QCheckBox(self.tabFileFiltering)
        self.chkIncludeAlternateFileFormats.setChecked(True)
        self.chkIncludeAlternateFileFormats.setObjectName(_fromUtf8("chkIncludeAlternateFileFormats"))
        self.verticalLayout.addWidget(self.chkIncludeAlternateFileFormats)
        self.chkIncludeHacked = QtGui.QCheckBox(self.tabFileFiltering)
        self.chkIncludeHacked.setChecked(True)
        self.chkIncludeHacked.setObjectName(_fromUtf8("chkIncludeHacked"))
        self.verticalLayout.addWidget(self.chkIncludeHacked)
        self.chkIncludeXRated = QtGui.QCheckBox(self.tabFileFiltering)
        self.chkIncludeXRated.setChecked(True)
        self.chkIncludeXRated.setObjectName(_fromUtf8("chkIncludeXRated"))
        self.verticalLayout.addWidget(self.chkIncludeXRated)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)
        self.verticalLayout.setStretch(8, 1)
        self.tabWidget.addTab(self.tabFileFiltering, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "ZX Pokemaster", None))
        self.btnLoadSettings.setText(_translate("Dialog", "Load Settings...", None))
        self.btnSaveSettings.setText(_translate("Dialog", "Save Settings...", None))
        self.btnSortFiles.setText(_translate("Dialog", "Sort files", None))
        self.groupBox.setTitle(_translate("Dialog", "Input paths", None))
        self.btnAddPath.setText(_translate("Dialog", "Add path...", None))
        self.chkTraverseSubdirectories.setText(_translate("Dialog", "Traverse subdirectories", None))
        self.btnRemovePaths.setText(_translate("Dialog", "Remove path", None))
        self.label.setText(_translate("Dialog", "Output path:", None))
        self.btnBrowseOutputPath.setText(_translate("Dialog", "...", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Output path structure pattern", None))
        self.btnRemovePattern.setText(_translate("Dialog", "Remove pattern", None))
        self.btnAddPattern.setText(_translate("Dialog", "Add pattern...", None))
        self.btnEditPattern.setText(_translate("Dialog", "Edit pattern...", None))
        self.chkMaxFilesPerFolder.setText(_translate("Dialog", "Max files per folder:", None))
        self.chkCamelCase.setText(_translate("Dialog", "CamelCaseInsteadOfSpaces", None))
        self.chkShortFilenames.setText(_translate("Dialog", "Use 8.3 naming scheme", None))
        self.chkPlacePokFilesIntoPOKESSubfolders.setText(_translate("Dialog", "Place .POK files into POKES subfolders", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMainOptions), _translate("Dialog", "Main options", None))
        self.label_2.setText(_translate("Dialog", "Formats preference:", None))
        self.txtFormatPreference.setPlaceholderText(_translate("Dialog", "tap,z80,sna,dsk,trd,tzx,img,mgt,rom,scl,slt,szx", None))
        self.label_3.setText(_translate("Dialog", "Languages:", None))
        self.txtLanguages.setPlaceholderText(_translate("Dialog", "en,es,ru,pl,cz,fr,de,nl,hu,cr,pl,sr,sl,sv,no", None))
        self.chkIncludeAlternate.setText(_translate("Dialog", "Include alternate files (marked [a] in TOSEC)", None))
        self.chkIncludeDemos.setText(_translate("Dialog", "Include demos (non-full versions of games)", None))
        self.chkIncludeRereleases.setText(_translate("Dialog", "Include re-releases", None))
        self.chkIncludeAlternateFileFormats.setText(_translate("Dialog", "Include alternate file formats (see formats preference order)", None))
        self.chkIncludeHacked.setText(_translate("Dialog", "Include files marked as cracked, hacked or modded", None))
        self.chkIncludeXRated.setText(_translate("Dialog", "Include x-rated games", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFileFiltering), _translate("Dialog", "File filtering", None))

import res_rc
