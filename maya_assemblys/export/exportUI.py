# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\CNCGToolKit\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(813, 378)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 771, 293))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.heiGeoComboPr = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.heiGeoComboPr.setObjectName("heiGeoComboPr")
        self.gridLayout.addWidget(self.heiGeoComboPr, 6, 1, 1, 1)
        self.lowGeoComboAc = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.lowGeoComboAc.setObjectName("lowGeoComboAc")
        self.gridLayout.addWidget(self.lowGeoComboAc, 8, 2, 1, 1)
        self.abcBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.abcBox.setObjectName("abcBox")
        self.gridLayout.addWidget(self.abcBox, 9, 0, 1, 1)
        self.geoLodComboAc = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.geoLodComboAc.setObjectName("geoLodComboAc")
        self.gridLayout.addWidget(self.geoLodComboAc, 7, 2, 1, 1)
        self.gpuComboAc = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.gpuComboAc.setMinimumSize(QtCore.QSize(300, 0))
        self.gpuComboAc.setObjectName("gpuComboAc")
        self.gridLayout.addWidget(self.gpuComboAc, 5, 2, 1, 1)
        self.bBoxBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.bBoxBox.setObjectName("bBoxBox")
        self.gridLayout.addWidget(self.bBoxBox, 10, 0, 1, 1)
        self.hiGeoBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.hiGeoBox.setObjectName("hiGeoBox")
        self.gridLayout.addWidget(self.hiGeoBox, 6, 0, 1, 1)
        self.geoLodBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.geoLodBox.setObjectName("geoLodBox")
        self.gridLayout.addWidget(self.geoLodBox, 7, 0, 1, 1)
        self.lowGeoBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.lowGeoBox.setObjectName("lowGeoBox")
        self.gridLayout.addWidget(self.lowGeoBox, 8, 0, 1, 1)
        self.abcComboPr = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.abcComboPr.setObjectName("abcComboPr")
        self.gridLayout.addWidget(self.abcComboPr, 9, 1, 1, 1)
        self.bBoxComboPr = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.bBoxComboPr.setObjectName("bBoxComboPr")
        self.gridLayout.addWidget(self.bBoxComboPr, 10, 1, 1, 1)
        self.gpuComboPr = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gpuComboPr.sizePolicy().hasHeightForWidth())
        self.gpuComboPr.setSizePolicy(sizePolicy)
        self.gpuComboPr.setMinimumSize(QtCore.QSize(300, 0))
        self.gpuComboPr.setObjectName("gpuComboPr")
        self.gridLayout.addWidget(self.gpuComboPr, 5, 1, 1, 1)
        self.lowGeoComboPr = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.lowGeoComboPr.setObjectName("lowGeoComboPr")
        self.gridLayout.addWidget(self.lowGeoComboPr, 8, 1, 1, 1)
        self.heiGeoComboAc = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.heiGeoComboAc.setObjectName("heiGeoComboAc")
        self.gridLayout.addWidget(self.heiGeoComboAc, 6, 2, 1, 1)
        self.gpuBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.gpuBox.setObjectName("gpuBox")
        self.gridLayout.addWidget(self.gpuBox, 5, 0, 1, 1)
        self.geoLoaComboPr = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.geoLoaComboPr.setObjectName("geoLoaComboPr")
        self.gridLayout.addWidget(self.geoLoaComboPr, 7, 1, 1, 1)
        self.bBoxComboAc = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.bBoxComboAc.setObjectName("bBoxComboAc")
        self.gridLayout.addWidget(self.bBoxComboAc, 10, 2, 1, 1)
        self.abcComboAc = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.abcComboAc.setObjectName("abcComboAc")
        self.gridLayout.addWidget(self.abcComboAc, 9, 2, 1, 1)
        self.layoutBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.layoutBox.setObjectName("layoutBox")
        self.gridLayout.addWidget(self.layoutBox, 11, 0, 1, 1)
        self.layoutComboPr = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.layoutComboPr.setObjectName("layoutComboPr")
        self.gridLayout.addWidget(self.layoutComboPr, 11, 1, 1, 1)
        self.layoutComboAc = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.layoutComboAc.setObjectName("layoutComboAc")
        self.gridLayout.addWidget(self.layoutComboAc, 11, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ExportButton = QtWidgets.QPushButton(Form)
        self.ExportButton.setObjectName("ExportButton")
        self.horizontalLayout.addWidget(self.ExportButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.toolSetButton = QtWidgets.QPushButton(Form)
        self.toolSetButton.setObjectName("toolSetButton")
        self.horizontalLayout.addWidget(self.toolSetButton)
        self.cancelButton = QtWidgets.QPushButton(Form)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Export Definition file"))
        self.label.setText(_translate("Form", "Representation"))
        self.label_2.setText(_translate("Form", "Preparation"))
        self.label_3.setText(_translate("Form", "Action"))
        self.abcBox.setText(_translate("Form", "abc"))
        self.bBoxBox.setText(_translate("Form", "bBox"))
        self.hiGeoBox.setText(_translate("Form", "hiGeo"))
        self.geoLodBox.setText(_translate("Form", "geoLod1"))
        self.lowGeoBox.setText(_translate("Form", "lowGeo"))
        self.gpuBox.setText(_translate("Form", "gpu"))
        self.layoutBox.setText(_translate("Form", "layout"))
        self.ExportButton.setText(_translate("Form", "Export definition file"))
        self.toolSetButton.setText(_translate("Form", "toolSet"))
        self.cancelButton.setText(_translate("Form", "cancel"))
