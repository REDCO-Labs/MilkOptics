from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread
import os
from pyqtgraph import PlotItem, BarGraphItem
from PyQt5 import uic
import seabreeze.spectrometers as sb
from tools.threadWorker import Worker

import logging


log = logging.getLogger(__name__)

simulationViewUiPath = os.path.dirname(os.path.realpath(__file__)) + "\\simulationViewUi.ui"
Ui_simulationView, QtBaseClass = uic.loadUiType(simulationViewUiPath)


class SimulationView(QWidget, Ui_simulationView):
    s_data_changed = pyqtSignal(dict)

    def __init__(self, model=None, controller=None):
        super(SimulationView, self).__init__()
        self.model = model
        self.plotDict = {}
        self.setupUi(self)
        self.create_plots()
        self.connect_buttons()
        self.connect_signals()
        self.connect_checkbox()

        self.spec = None
        self.isAlive = 1
        self.initialize_device()

    def initialize_device(self):
        devices = sb.list_devices()
        self.spec = sb.Spectrometer(devices[0])
        self.spec.integration_time_micros(int(self.le_acqTime.text())*1000)
        self.pyqtgraphWidget.clear()
        print(devices)

    def connect_buttons(self):
        self.pb_backgroundAcq.clicked.connect(self.start_data_acquisition)
        self.pb_compute.clicked.connect(lambda: print("lol compute computer"))
        self.pb_filterAcq.clicked.connect(lambda: print("lol compute filter"))
        log.info("Connecting simulationView GUI...")

    def connect_checkbox(self):
        pass

    def connect_signals(self):
        log.info("Connecting simulationView Signals...")
        self.s_data_changed.connect(self.update_graph)

    def create_plots(self):
        self.pyqtgraphWidget.clear()
        self.plotItem = self.pyqtgraphWidget.addPlot()
        print(type(self.plotItem))
        self.dataPlotItem = self.plotItem.plot()
        print(self.dataPlotItem)


    @pyqtSlot(dict)
    def update_graph(self, plotData):
        print(plotData)
        x = plotData["x"]
        y = plotData["y"]
        self.dataPlotItem.setData(x, y)

    def update_spectrum_plot(self, *args, **kwargs):
        while self.isAlive:
            waves = self.spec.wavelengths()[2:]
            intens = self.spec.intensities()[2:]
            self.s_data_changed.emit({"x": waves, "y": intens})

    def start_data_acquisition(self, *args):
        self.acqWorker = Worker(self.update_spectrum_plot, *args)
        self.acqThread = QThread()
        self.acqWorker.moveToThread(self.acqThread)
        self.acqThread.started.connect(self.acqWorker.run)
        self.acqThread.start()
