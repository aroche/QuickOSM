# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/my_queries.ui'
#
# Created: Fri Feb 19 21:51:07 2016
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

class Ui_ui_my_queries(object):
    def setupUi(self, ui_my_queries):
        ui_my_queries.setObjectName(_fromUtf8("ui_my_queries"))
        ui_my_queries.resize(727, 794)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui_my_queries.sizePolicy().hasHeightForWidth())
        ui_my_queries.setSizePolicy(sizePolicy)
        ui_my_queries.setMinimumSize(QtCore.QSize(225, 262))
        self.verticalLayout_3 = QtGui.QVBoxLayout(ui_my_queries)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.scrollArea = QtGui.QScrollArea(ui_my_queries)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 719, 786))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEdit_search = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_search.setObjectName(_fromUtf8("lineEdit_search"))
        self.verticalLayout.addWidget(self.lineEdit_search)
        self.treeQueries = QtGui.QTreeWidget(self.scrollAreaWidgetContents)
        self.treeQueries.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeQueries.setColumnCount(1)
        self.treeQueries.setObjectName(_fromUtf8("treeQueries"))
        self.treeQueries.header().setVisible(False)
        self.verticalLayout.addWidget(self.treeQueries)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setText(_fromUtf8("{{geocodeArea:}}"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_nominatim = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_nominatim.setObjectName(_fromUtf8("lineEdit_nominatim"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_nominatim)
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setText(_fromUtf8("{{bbox}}"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.radioButton_extentMapCanvas = QtGui.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_extentMapCanvas.setChecked(True)
        self.radioButton_extentMapCanvas.setObjectName(_fromUtf8("radioButton_extentMapCanvas"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.radioButton_extentMapCanvas)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.radioButton_extentLayer = QtGui.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_extentLayer.setObjectName(_fromUtf8("radioButton_extentLayer"))
        self.horizontalLayout_5.addWidget(self.radioButton_extentLayer)
        self.comboBox_extentLayer = QgsMapLayerComboBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_extentLayer.sizePolicy().hasHeightForWidth())
        self.comboBox_extentLayer.setSizePolicy(sizePolicy)
        self.comboBox_extentLayer.setObjectName(_fromUtf8("comboBox_extentLayer"))
        self.horizontalLayout_5.addWidget(self.comboBox_extentLayer)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.formLayout)
        self.groupBox = QgsCollapsibleGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_4.setWidget(6, QtGui.QFormLayout.FieldRole, self.label_7)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setText(_fromUtf8("Points"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_10)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.checkBox_points = QtGui.QCheckBox(self.groupBox)
        self.checkBox_points.setText(_fromUtf8(""))
        self.checkBox_points.setChecked(True)
        self.checkBox_points.setObjectName(_fromUtf8("checkBox_points"))
        self.horizontalLayout_4.addWidget(self.checkBox_points)
        self.lineEdit_csv_points = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_csv_points.setInputMask(_fromUtf8(""))
        self.lineEdit_csv_points.setText(_fromUtf8(""))
        self.lineEdit_csv_points.setPlaceholderText(_fromUtf8("col1,col2,col3"))
        self.lineEdit_csv_points.setObjectName(_fromUtf8("lineEdit_csv_points"))
        self.horizontalLayout_4.addWidget(self.lineEdit_csv_points)
        self.formLayout_4.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.checkBox_lines = QtGui.QCheckBox(self.groupBox)
        self.checkBox_lines.setText(_fromUtf8(""))
        self.checkBox_lines.setChecked(True)
        self.checkBox_lines.setObjectName(_fromUtf8("checkBox_lines"))
        self.horizontalLayout_6.addWidget(self.checkBox_lines)
        self.lineEdit_csv_lines = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_csv_lines.setObjectName(_fromUtf8("lineEdit_csv_lines"))
        self.horizontalLayout_6.addWidget(self.lineEdit_csv_lines)
        self.formLayout_4.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setText(_fromUtf8("Lines"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_11)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.checkBox_multilinestrings = QtGui.QCheckBox(self.groupBox)
        self.checkBox_multilinestrings.setText(_fromUtf8(""))
        self.checkBox_multilinestrings.setChecked(True)
        self.checkBox_multilinestrings.setObjectName(_fromUtf8("checkBox_multilinestrings"))
        self.horizontalLayout_7.addWidget(self.checkBox_multilinestrings)
        self.lineEdit_csv_multilinestrings = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_csv_multilinestrings.setPlaceholderText(_fromUtf8(""))
        self.lineEdit_csv_multilinestrings.setObjectName(_fromUtf8("lineEdit_csv_multilinestrings"))
        self.horizontalLayout_7.addWidget(self.lineEdit_csv_multilinestrings)
        self.formLayout_4.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setText(_fromUtf8("Multilinestrings"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_14)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.checkBox_multipolygons = QtGui.QCheckBox(self.groupBox)
        self.checkBox_multipolygons.setText(_fromUtf8(""))
        self.checkBox_multipolygons.setChecked(True)
        self.checkBox_multipolygons.setObjectName(_fromUtf8("checkBox_multipolygons"))
        self.horizontalLayout_8.addWidget(self.checkBox_multipolygons)
        self.lineEdit_csv_multipolygons = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_csv_multipolygons.setPlaceholderText(_fromUtf8(""))
        self.lineEdit_csv_multipolygons.setObjectName(_fromUtf8("lineEdit_csv_multipolygons"))
        self.horizontalLayout_8.addWidget(self.lineEdit_csv_multipolygons)
        self.formLayout_4.setLayout(5, QtGui.QFormLayout.FieldRole, self.horizontalLayout_8)
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setText(_fromUtf8("Multipolygons"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_4.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_12)
        self.verticalLayout_2.addLayout(self.formLayout_4)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit_browseDir = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_browseDir.setObjectName(_fromUtf8("lineEdit_browseDir"))
        self.horizontalLayout.addWidget(self.lineEdit_browseDir)
        self.pushButton_browse_output_file = QtGui.QPushButton(self.groupBox)
        self.pushButton_browse_output_file.setObjectName(_fromUtf8("pushButton_browse_output_file"))
        self.horizontalLayout.addWidget(self.pushButton_browse_output_file)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_filePrefix = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_filePrefix.setObjectName(_fromUtf8("lineEdit_filePrefix"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_filePrefix)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_showQuery = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_showQuery.setObjectName(_fromUtf8("pushButton_showQuery"))
        self.horizontalLayout_3.addWidget(self.pushButton_showQuery)
        self.pushButton_runQuery = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_runQuery.setDefault(True)
        self.pushButton_runQuery.setObjectName(_fromUtf8("pushButton_runQuery"))
        self.horizontalLayout_3.addWidget(self.pushButton_runQuery)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_progress = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_progress.setText(_fromUtf8("text progress"))
        self.label_progress.setObjectName(_fromUtf8("label_progress"))
        self.verticalLayout.addWidget(self.label_progress)
        self.progressBar_execution = QtGui.QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar_execution.setProperty("value", 0)
        self.progressBar_execution.setObjectName(_fromUtf8("progressBar_execution"))
        self.verticalLayout.addWidget(self.progressBar_execution)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)

        self.retranslateUi(ui_my_queries)
        QtCore.QObject.connect(self.checkBox_points, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEdit_csv_points.setEnabled)
        QtCore.QObject.connect(self.checkBox_lines, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEdit_csv_lines.setEnabled)
        QtCore.QObject.connect(self.checkBox_multilinestrings, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEdit_csv_multilinestrings.setEnabled)
        QtCore.QObject.connect(self.checkBox_multipolygons, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEdit_csv_multipolygons.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(ui_my_queries)

    def retranslateUi(self, ui_my_queries):
        ui_my_queries.setWindowTitle(_translate("ui_my_queries", "QuickOSM - My queries", None))
        self.lineEdit_search.setPlaceholderText(_translate("ui_my_queries", "Search", None))
        self.treeQueries.setSortingEnabled(False)
        self.treeQueries.headerItem().setText(0, _translate("ui_my_queries", "Query", None))
        self.radioButton_extentMapCanvas.setText(_translate("ui_my_queries", "Extent of the map canvas", None))
        self.radioButton_extentLayer.setText(_translate("ui_my_queries", "Extent of a layer", None))
        self.groupBox.setTitle(_translate("ui_my_queries", "Advanced", None))
        self.label_3.setText(_translate("ui_my_queries", "Outputs", None))
        self.lineEdit_csv_lines.setPlaceholderText(_translate("ui_my_queries", "or let empty", None))
        self.label_4.setText(_translate("ui_my_queries", "Directory", None))
        self.lineEdit_browseDir.setPlaceholderText(_translate("ui_my_queries", "Save to temporary file", None))
        self.pushButton_browse_output_file.setText(_translate("ui_my_queries", "Browse", None))
        self.label_6.setText(_translate("ui_my_queries", "File prefix", None))
        self.pushButton_showQuery.setText(_translate("ui_my_queries", "Show query", None))
        self.pushButton_runQuery.setText(_translate("ui_my_queries", "Run query", None))

from qgis.gui import QgsMapLayerComboBox, QgsCollapsibleGroupBox
