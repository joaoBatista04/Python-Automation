import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtWebEngineWidgets
from time import sleep

app = QtWidgets.QApplication(sys.argv)
loader = QtWebEngineWidgets.QWebEngineView()
loader.setZoomFactor(1)
loader.page().pdfPrintingFinished.connect(
    lambda *args: print('finished:', args))
loader.load(QtCore.QUrl('https://app.respondeai.com.br/materias/solucionario/livro/2/edicao/7/exercicio/2341'))

def emit_pdf(finished):
    loader.show()
    loader.page().printToPdf("test.pdf")

sleep(5)
loader.loadFinished.connect(emit_pdf)

app.exec()
