from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from AutomatoLexicoController import *
from AutomatoShuntingYardController import *
from AutomatoPushdownController import *
from AutomatoSolverController import *

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(857, 518)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabPrincipal = QtWidgets.QTabWidget(self.centralwidget)
        self.tabPrincipal.setGeometry(QtCore.QRect(20, 40, 821, 451))
        self.tabPrincipal.setObjectName("tabPrincipal")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.outLexicoEntrada = QtWidgets.QTextBrowser(self.tab)
        self.outLexicoEntrada.setGeometry(QtCore.QRect(10, 70, 791, 91))
        self.outLexicoEntrada.setObjectName("outLexicoEntrada")
        self.outLexicoSaida = QtWidgets.QTextBrowser(self.tab)
        self.outLexicoSaida.setGeometry(QtCore.QRect(10, 190, 791, 221))
        self.outLexicoSaida.setObjectName("outLexicoSaida")
        self.btnLexicoAvancar = QtWidgets.QPushButton(self.tab)
        self.btnLexicoAvancar.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.btnLexicoAvancar.setObjectName("btnLexicoAvancar")
        self.lblLexicoEntrada = QtWidgets.QLabel(self.tab)
        self.lblLexicoEntrada.setGeometry(QtCore.QRect(10, 50, 47, 13))
        self.lblLexicoEntrada.setObjectName("lblLexicoEntrada")
        self.lblLexicoSaida = QtWidgets.QLabel(self.tab)
        self.lblLexicoSaida.setGeometry(QtCore.QRect(10, 170, 47, 13))
        self.lblLexicoSaida.setObjectName("lblLexicoSaida")
        self.tabPrincipal.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.stwSintatico = QtWidgets.QStackedWidget(self.tab_2)
        self.stwSintatico.setGeometry(QtCore.QRect(10, 40, 791, 381))
        self.stwSintatico.setObjectName("stwSintatico")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.outSintaticoShuntingYardPilha = QtWidgets.QTextBrowser(self.page)
        self.outSintaticoShuntingYardPilha.setGeometry(QtCore.QRect(600, 20, 191, 351))
        self.outSintaticoShuntingYardPilha.setObjectName("outSintaticoShuntingYardPilha")
        self.lblSintaticoShuntingYardFila = QtWidgets.QLabel(self.page)
        self.lblSintaticoShuntingYardFila.setGeometry(QtCore.QRect(0, 210, 81, 21))
        self.lblSintaticoShuntingYardFila.setObjectName("lblSintaticoShuntingYardFila")
        self.lblSintaticoShuntingYardEntrada = QtWidgets.QLabel(self.page)
        self.lblSintaticoShuntingYardEntrada.setGeometry(QtCore.QRect(0, 40, 81, 21))
        self.lblSintaticoShuntingYardEntrada.setObjectName("lblSintaticoShuntingYardEntrada")
        self.outSintaticoShuntingYardEntrada = QtWidgets.QTextBrowser(self.page)
        self.outSintaticoShuntingYardEntrada.setGeometry(QtCore.QRect(0, 60, 581, 141))
        self.outSintaticoShuntingYardEntrada.setObjectName("outSintaticoShuntingYardEntrada")
        self.outSintaticoShuntingYardFila = QtWidgets.QTextBrowser(self.page)
        self.outSintaticoShuntingYardFila.setGeometry(QtCore.QRect(0, 230, 581, 141))
        self.outSintaticoShuntingYardFila.setObjectName("outSintaticoShuntingYardFila")
        self.btnSintaticoShuntingYardAvancar = QtWidgets.QPushButton(self.page)
        self.btnSintaticoShuntingYardAvancar.setGeometry(QtCore.QRect(0, 10, 75, 23))
        self.btnSintaticoShuntingYardAvancar.setObjectName("btnSintaticoShuntingYardAvancar")
        self.stwSintatico.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stwSintatico.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stwSintatico.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stwSintatico.addWidget(self.page_4)
        self.btnSintaticoProximo = QtWidgets.QPushButton(self.tab_2)
        self.btnSintaticoProximo.setGeometry(QtCore.QRect(260, 10, 91, 23))
        self.btnSintaticoProximo.setObjectName("btnSintaticoProximo")
        self.btnSintaticoAnterior = QtWidgets.QPushButton(self.tab_2)
        self.btnSintaticoAnterior.setGeometry(QtCore.QRect(160, 10, 91, 23))
        self.btnSintaticoAnterior.setObjectName("btnSintaticoAnterior")
        self.lblSintaticoAlgoritmo = QtWidgets.QLabel(self.tab_2)
        self.lblSintaticoAlgoritmo.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.lblSintaticoAlgoritmo.setObjectName("lblSintaticoAlgoritmo")
        self.lblSintaticoAlgoritmoNome = QtWidgets.QLabel(self.tab_2)
        self.lblSintaticoAlgoritmoNome.setGeometry(QtCore.QRect(70, 10, 81, 21))
        self.lblSintaticoAlgoritmoNome.setObjectName("lblSintaticoAlgoritmoNome")
        self.lblSintaticoShuntingYardPilha = QtWidgets.QLabel(self.tab_2)
        self.lblSintaticoShuntingYardPilha.setGeometry(QtCore.QRect(610, 40, 81, 21))
        self.lblSintaticoShuntingYardPilha.setObjectName("lblSintaticoShuntingYardPilha")
        self.tabPrincipal.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tblSemanticoMemoria = QtWidgets.QTableWidget(self.tab_3)
        self.tblSemanticoMemoria.setGeometry(QtCore.QRect(545, 80, 261, 331))
        self.tblSemanticoMemoria.setRowCount(0)
        self.tblSemanticoMemoria.setColumnCount(2)
        self.tblSemanticoMemoria.setObjectName("tblSemanticoMemoria")
        self.lblSemanticoMemoria = QtWidgets.QLabel(self.tab_3)
        self.lblSemanticoMemoria.setGeometry(QtCore.QRect(540, 30, 81, 21))
        self.lblSemanticoMemoria.setObjectName("lblSemanticoMemoria")
        self.outSemanticoEntrada = QtWidgets.QTextBrowser(self.tab_3)
        self.outSemanticoEntrada.setGeometry(QtCore.QRect(10, 60, 521, 351))
        self.outSemanticoEntrada.setObjectName("outSemanticoEntrada")
        self.btnSemanticoAvancar = QtWidgets.QPushButton(self.tab_3)
        self.btnSemanticoAvancar.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.btnSemanticoAvancar.setObjectName("btnSemanticoAvancar")
        self.lblSemanticoEntrada = QtWidgets.QLabel(self.tab_3)
        self.lblSemanticoEntrada.setGeometry(QtCore.QRect(10, 40, 81, 21))
        self.lblSemanticoEntrada.setObjectName("lblSemanticoEntrada")
        self.inpSemanticoConjunto = QtWidgets.QLineEdit(self.tab_3)
        self.inpSemanticoConjunto.setGeometry(QtCore.QRect(610, 50, 111, 20))
        self.inpSemanticoConjunto.setObjectName("inpSemanticoConjunto")
        self.inpSemanticoId = QtWidgets.QLineEdit(self.tab_3)
        self.inpSemanticoId.setGeometry(QtCore.QRect(550, 50, 41, 20))
        self.inpSemanticoId.setObjectName("inpSemanticoId")
        self.lblSemanticoIgual = QtWidgets.QLabel(self.tab_3)
        self.lblSemanticoIgual.setGeometry(QtCore.QRect(590, 50, 16, 21))
        self.lblSemanticoIgual.setObjectName("lblSemanticoIgual")
        self.btnSemanticoAdicionar = QtWidgets.QPushButton(self.tab_3)
        self.btnSemanticoAdicionar.setGeometry(QtCore.QRect(730, 50, 75, 23))
        self.btnSemanticoAdicionar.setObjectName("btnSemanticoAdicionar")
        self.tabPrincipal.addTab(self.tab_3, "")
        self.btnGerar = QtWidgets.QPushButton(self.centralwidget)
        self.btnGerar.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.btnGerar.setObjectName("btnGerar")
        self.inpExpressao = QtWidgets.QLineEdit(self.centralwidget)
        self.inpExpressao.setGeometry(QtCore.QRect(100, 11, 271, 20))
        self.inpExpressao.setObjectName("inpExpressao")
        self.btnConfirmar = QtWidgets.QPushButton(self.centralwidget)
        self.btnConfirmar.setGeometry(QtCore.QRect(380, 10, 75, 23))
        self.btnConfirmar.setObjectName("btnConfirmar")
        self.btnAutomatico = QtWidgets.QPushButton(self.centralwidget)
        self.btnAutomatico.setGeometry(QtCore.QRect(460, 10, 75, 23))
        self.btnAutomatico.setObjectName("btnAutomatico")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabPrincipal.setCurrentIndex(2)
        self.stwSintatico.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Timers
        self.tmrAutomatico = QTimer()
        self.tmrAutomatico.timeout.connect(self.passoTmrAutomatico)
        self.tmrAutomaticoState = ''
        # Variaveis
        self.automatoLexico = AutomatoLexicoController("")
        self.automatoPushdown = AutomatoPushdownController()
        self.automatoShuntingYard = AutomatoShuntingYardController([])
        self.automatoSolver = AutomatoSolverController([], list(range(-101, 101)))
        self.strOutLexicoEntrada = ""
        self.strOutLexicoSaida = ""
        self.strOutSintaticoShuntingYardEntrada = ""
        self.strOutSintaticoShuntingYardFila = ""
        self.strOutSintaticoShuntingYardPilha = ""
        self.strOutSemanticoEntrada = ""
        # Tabela variavel
        self.tblSemanticoMemoria.setHorizontalHeaderLabels(['ID', 'CONJUNTO'])
        self.tblSemanticoMemoria.setItem(0, 1, self.gerarCelulaConjuntoVazia())
        self.tblSemanticoMemoria.setItem(0, 0, self.gerarCelulaConjuntoVazia())
        # Estados pre-setados
        self.outLexicoSaida.setEnabled(False)
        self.outLexicoEntrada.setEnabled(False)
        self.btnLexicoAvancar.setEnabled(False)
        self.outSintaticoShuntingYardEntrada.setEnabled(False)
        self.outSintaticoShuntingYardPilha.setEnabled(False)
        self.outSintaticoShuntingYardFila.setEnabled(False)
        self.btnSintaticoProximo.setEnabled(False)
        self.btnSintaticoAnterior.setEnabled(False)
        self.btnSintaticoShuntingYardAvancar.setEnabled(False)
        self.outSemanticoEntrada.setEnabled(False)
        self.btnSemanticoAvancar.setEnabled(False)
        self.btnSemanticoAdicionar.setEnabled(False)
        self.btnAutomatico.setEnabled(True)
        self.outLexicoSaida.setFontPointSize(14)
        # Botao automatico
        self.btnAutomatico.clicked.connect(self.iniciarTmrAutomatico)
        # Botao gerar
        self.btnGerar.clicked.connect(self.gerarExpressao)
        # Botao confirmar
        self.btnConfirmar.clicked.connect(self.confirmarExpressao)
        # Botao proximo do lexico
        self.btnLexicoAvancar.clicked.connect(self.proximoLexico)
        # Botao proximo do sintatico (Shunting Yard)
        self.btnSintaticoShuntingYardAvancar.clicked.connect(self.proximoSintaticoShuntingYard)
        # Botao adicionar conjunto do semantico
        self.btnSemanticoAdicionar.clicked.connect(self.adicionarSemantico)
        # Botao proximo do semantico
        self.btnSemanticoAvancar.clicked.connect(self.proximoSemantico)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora de conjuntos"))
        self.btnLexicoAvancar.setText(_translate("MainWindow", "Avançar"))
        self.lblLexicoEntrada.setText(_translate("MainWindow", "Entrada"))
        self.lblLexicoSaida.setText(_translate("MainWindow", "Saída"))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.tab), _translate("MainWindow", "Análise léxica"))
        self.lblSintaticoShuntingYardFila.setText(_translate("MainWindow", "Fila"))
        self.lblSintaticoShuntingYardEntrada.setText(_translate("MainWindow", "Entrada"))
        self.btnSintaticoShuntingYardAvancar.setText(_translate("MainWindow", "Avançar"))
        self.btnSintaticoProximo.setText(_translate("MainWindow", "Proximo"))
        self.btnSintaticoAnterior.setText(_translate("MainWindow", "Anterior"))
        self.lblSintaticoAlgoritmo.setText(_translate("MainWindow", "Algoritmo:"))
        self.lblSintaticoAlgoritmoNome.setText(_translate("MainWindow", "Shunting Yard"))
        self.lblSintaticoShuntingYardPilha.setText(_translate("MainWindow", "Plha"))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.tab_2), _translate("MainWindow", "Análise sintática"))
        self.lblSemanticoMemoria.setText(_translate("MainWindow", "Memória"))
        self.btnSemanticoAvancar.setText(_translate("MainWindow", "Avançar"))
        self.lblSemanticoEntrada.setText(_translate("MainWindow", "Entrada"))
        self.lblSemanticoIgual.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; font-weight:600;\">=</span></p></body></html>"))
        self.btnSemanticoAdicionar.setText(_translate("MainWindow", "Adicionar"))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.tab_3), _translate("MainWindow", "Análise semântica"))
        self.btnGerar.setText(_translate("MainWindow", "Gerar"))
        self.btnConfirmar.setText(_translate("MainWindow", "Confirmar"))
        self.btnAutomatico.setText(_translate("MainWindow", "Automático"))

# Metodos gerais
    def iniciarAutomatos(self):
        entrada = self.inpExpressao.text()
        self.automatoLexico.resetar(entrada)
        saidaAutomatoLexico = self.automatoLexico.saida()
        if(saidaAutomatoLexico is None):
            return -1
        if(self.automatoPushdown.analiseSintatica(saidaAutomatoLexico) == 0):
            self.automatoShuntingYard.resetar(self.automatoLexico.saida())
            self.automatoSolver.resetar(self.automatoShuntingYard.saida())
            self.automatoShuntingYard.resetar(self.automatoLexico.saida())
            return 0
        else:
            return -2

    def gerarExpressao(self):
        ale = GeraParsingEsq(9)
        lstEntrada = (ale[0]).ListaTokensValor
        entrada = ''
        for elem in lstEntrada:
           if(str(elem) == 'set()'):
               entrada = entrada + '{}'
           else:
               entrada = entrada + str(elem)

        self.inpExpressao.setText(entrada)

    def confirmarExpressao(self):
        retornoInicializacaoAutomato = self.iniciarAutomatos()
        if (retornoInicializacaoAutomato == 0):
            self.strOutLexicoEntrada = ""
            self.strOutLexicoSaida = ""
            self.strOutSintaticoShuntingYardEntrada = ""
            self.strOutSintaticoShuntingYardFila = ""
            self.strOutSintaticoShuntingYardPilha = ""
            self.inpExpressao.setEnabled(False)
            self.btnConfirmar.setEnabled(False)
            self.btnGerar.setEnabled(False)
            self.btnAutomatico.setEnabled(False)
            self.outLexicoSaida.setEnabled(True)
            self.outLexicoEntrada.setEnabled(True)
            self.btnLexicoAvancar.setEnabled(True)
            self.outSintaticoShuntingYardEntrada.setEnabled(True)
            self.outSintaticoShuntingYardPilha.setEnabled(True)
            self.outSintaticoShuntingYardFila.setEnabled(True)
            self.btnSintaticoProximo.setEnabled(True)
            self.btnSintaticoAnterior.setEnabled(True)
            self.btnSintaticoShuntingYardAvancar.setEnabled(True)
            self.outSemanticoEntrada.setEnabled(True)
            self.btnSemanticoAvancar.setEnabled(True)
            self.btnSemanticoAdicionar.setEnabled(True)
        elif (retornoInicializacaoAutomato == -1):
            self.strOutLexicoEntrada = "ERRO LÉXICO"
            self.strOutLexicoSaida = ""
            self.strOutSintaticoShuntingYardEntrada = "ERRO LÉXICO"
            self.strOutSintaticoShuntingYardFila = ""
            self.strOutSintaticoShuntingYardPilha = ""
            self.inpExpressao.setEnabled(False)
            self.btnConfirmar.setEnabled(False)
            self.btnGerar.setEnabled(False)
            self.btnAutomatico.setEnabled(False)
            self.outLexicoSaida.setEnabled(False)
            self.outLexicoEntrada.setEnabled(False)
            self.btnLexicoAvancar.setEnabled(False)
            self.outSintaticoShuntingYardEntrada.setEnabled(False)
            self.outSintaticoShuntingYardPilha.setEnabled(False)
            self.outSintaticoShuntingYardFila.setEnabled(False)
            self.btnSintaticoProximo.setEnabled(False)
            self.btnSintaticoAnterior.setEnabled(False)
            self.btnSintaticoShuntingYardAvancar.setEnabled(False)
            self.outSemanticoEntrada.setEnabled(False)
            self.btnSemanticoAvancar.setEnabled(False)
            self.btnSemanticoAdicionar.setEnabled(False)
            self.outLexicoEntrada.setHtml(self.strOutLexicoEntrada)
            self.outSintaticoShuntingYardEntrada.setHtml(self.strOutSintaticoShuntingYardEntrada)
        elif(retornoInicializacaoAutomato == -2):
            self.strOutLexicoEntrada = ""
            self.strOutLexicoSaida = ""
            self.strOutSintaticoShuntingYardEntrada = "ERRO SINTÁTICO"
            self.strOutSintaticoShuntingYardFila = ""
            self.strOutSintaticoShuntingYardPilha = ""
            self.inpExpressao.setEnabled(False)
            self.btnConfirmar.setEnabled(False)
            self.btnGerar.setEnabled(False)
            self.btnAutomatico.setEnabled(False)
            self.outLexicoSaida.setEnabled(True)
            self.outLexicoEntrada.setEnabled(True)
            self.btnLexicoAvancar.setEnabled(True)
            self.outSintaticoShuntingYardEntrada.setEnabled(False)
            self.outSintaticoShuntingYardPilha.setEnabled(False)
            self.outSintaticoShuntingYardFila.setEnabled(False)
            self.btnSintaticoProximo.setEnabled(False)
            self.btnSintaticoAnterior.setEnabled(False)
            self.btnSintaticoShuntingYardAvancar.setEnabled(False)
            self.outSemanticoEntrada.setEnabled(False)
            self.btnSemanticoAvancar.setEnabled(False)
            self.btnSemanticoAdicionar.setEnabled(False)
            self.outSintaticoShuntingYardEntrada.setHtml(self.strOutSintaticoShuntingYardEntrada)

    def passoTmrAutomatico(self):
        if self.tmrAutomaticoState == '':
            self.confirmarExpressao()
            self.btnAutomatico.setEnabled(True)
            self.habilitarLexicoTmrAutomatico()
        elif self.tmrAutomaticoState == 'LEX':
            self.proximoLexico()
        elif self.tmrAutomaticoState == 'SIN':
            self.proximoSintaticoShuntingYard()
        elif self.tmrAutomaticoState == 'SEM':
            self.proximoSemantico()

    def iniciarTmrAutomatico(self):
        self.tmrAutomatico.start(1000)
        self.btnAutomatico.clicked.connect(self.finalizarTmrAutomatico)
        self.tabPrincipal.setTabEnabled(1, False)
        self.tabPrincipal.setTabEnabled(2, False)
        self.tabPrincipal.setTabEnabled(3, False)

    def finalizarTmrAutomatico(self):
        self.tmrAutomatico.stop()
        self.btnAutomatico.clicked.connect(self.iniciarTmrAutomatico)

    def habilitarLexicoTmrAutomatico(self):
        self.tmrAutomaticoState = 'LEX'
        self.outLexicoSaida.setEnabled(False)
        self.outLexicoEntrada.setEnabled(False)
        self.btnLexicoAvancar.setEnabled(True)

    def habilitarSintaticoTmrAutomatico(self):
        self.tmrAutomaticoState = 'SIN'
        self.tabPrincipal.setCurrentIndex(1)
        self.outSintaticoShuntingYardEntrada.setEnabled(False)
        self.outSintaticoShuntingYardPilha.setEnabled(False)
        self.outSintaticoShuntingYardFila.setEnabled(False)
        self.btnSintaticoShuntingYardAvancar.setEnabled(True)

    def habilitarSemanticoTmrAutomatico(self):
        self.tmrAutomaticoState = 'SEM'
        self.tabPrincipal.setCurrentIndex(2)
        self.outSemanticoEntrada.setEnabled(False)
        self.btnSemanticoAvancar.setEnabled(False)
        self.btnSemanticoAdicionar.setEnabled(True)

    # Lexico
    def proximoLexico(self):
        token = self.automatoLexico.proximo()
        if token is not None:
            self.strOutLexicoSaida = self.strOutLexicoSaida + " " + str(token)
        self.outLexicoSaida.setText(self.strOutLexicoSaida)

        self.strOutLexicoEntrada = '<font size="6">' + self.automatoLexico.entrada[0:self.automatoLexico.indexInicioToken] + '</font>' + '<b><font color="red" size = "14">→' + self.automatoLexico.entrada[self.automatoLexico.indexInicioToken:self.automatoLexico.indexFinalToken] + '←</font></b>' + '<font size="6">' + self.automatoLexico.entrada[self.automatoLexico.indexFinalToken:len(self.automatoLexico.entrada)] + '</font>'
        self.outLexicoEntrada.setHtml(self.strOutLexicoEntrada)

        if token is not None and token[0] == 'END':
            self.outLexicoSaida.setEnabled(False)
            self.outLexicoEntrada.setEnabled(False)
            self.btnLexicoAvancar.setEnabled(False)
            self.btnAutomatico.setEnabled(True)

            #Transicao do botao automatico
            if self.tmrAutomaticoState == 'LEX':
                self.habilitarSintaticoTmrAutomatico()

    # Sintatico
    def proximoSintaticoShuntingYard(self):
        retorno = self.automatoShuntingYard.proximo()
        self.strOutSintaticoShuntingYardEntrada = self.formatacaoFilaSintaticoShuntingYard(self.automatoShuntingYard.entrada)
        self.strOutSintaticoShuntingYardFila = self.formatacaoFilaSintaticoShuntingYard(self.automatoShuntingYard.fila)
        self.strOutSintaticoShuntingYardPilha = self.formatacaoPilhaSintaticoShuntingYard(self.automatoShuntingYard.pilha)

        self.outSintaticoShuntingYardEntrada.setHtml(self.strOutSintaticoShuntingYardEntrada)
        self.outSintaticoShuntingYardFila.setHtml(self.strOutSintaticoShuntingYardFila)
        self.outSintaticoShuntingYardPilha.setHtml(self.strOutSintaticoShuntingYardPilha)

        # Transicao do botao automatico
        if self.tmrAutomaticoState == 'SIN' and retorno is not None:
            self.habilitarSemanticoTmrAutomatico()

    def formatacaoFilaSintaticoShuntingYard(self, lstTokens):
        retorno = '<font size = "14">'
        index = 0
        while index < len(lstTokens):
            retorno = retorno + str((lstTokens[index])[1]) + ' '
            index = index + 1
        retorno = retorno + '</font>'
        return retorno

    def formatacaoPilhaSintaticoShuntingYard(self, lstTokens):
        retorno = '<font size = "14">'
        index = len(lstTokens) - 1
        while index >= 0:
            retorno = retorno + str((lstTokens[index])[1]) + '<br/>'
            index = index - 1
        retorno = retorno + '</font>'
        return retorno

    # Semantico
    def proximoSemantico(self):
        if self.strOutSemanticoEntrada == 'Entrada: ':
            self.strOutSemanticoEntrada = self.formatacaoEntradaSemantico() + '<br/>'

        passo = self.automatoSolver.proximo()
        if passo[0] == 'OPERACAO':
            self.strOutSemanticoEntrada = self.strOutSemanticoEntrada + '<br/>' + self.formatacaoEntradaSemantico() + '<br/>'
            self.strOutSemanticoEntrada = self.strOutSemanticoEntrada + 'Operacao realizada: ' + passo[1] + '<br/>'
        else:
            self.strOutSemanticoEntrada = self.strOutSemanticoEntrada + '<br/>' + self.formatacaoEntradaSemantico() + '<br/>'
            self.strOutSemanticoEntrada = self.strOutSemanticoEntrada + 'Descricao: ' + passo[1] + '<br/>'

        self.outSemanticoEntrada.setHtml(self.strOutSemanticoEntrada)
        self.outSemanticoEntrada.verticalScrollBar().setValue(self.outSemanticoEntrada.verticalScrollBar().maximum())

    def formatacaoEntradaSemantico(self):
        retorno = 'Entrada: '
        for index, token in enumerate(self.automatoSolver.entrada, start=0):
            if(token[1] == set()):
                retorno = retorno + '{ }' + ' '
            else:
                retorno = retorno + str(token[1]) + ' '
        retorno = retorno + '<br/>Pilha: '
        for index, elem in enumerate(self.automatoSolver.pilha, start=0):
            if (elem == set()):
                retorno = retorno + '{ }' + ' '
            else:
                retorno = retorno + str(elem) + ' '
        return retorno[0:-1]


    def adicionarSemantico(self):
        elemId = self.inpSemanticoId.text()
        elemConjunto = self.inpSemanticoConjunto.text()
        self.automatoSolver.adicionarConjuntoAMemoria(elemId, elemConjunto if elemConjunto is not None else set())

        if len(self.automatoSolver.memConjunto) > self.tblSemanticoMemoria.rowCount():
            valorLinhaNova = self.tblSemanticoMemoria.rowCount()
            self.tblSemanticoMemoria.insertRow(valorLinhaNova)

        for num, idConj in enumerate(self.automatoSolver.memConjunto, start = 0):
            conj = self.automatoSolver.memConjunto.get(idConj)

            colIdConjunto = QtWidgets.QTableWidgetItem(idConj)
            colIdConjunto.setFlags(colIdConjunto.flags() & ~QtCore.Qt.ItemIsEditable)
            colConjunto = QtWidgets.QTableWidgetItem(str(conj))
            colConjunto.setFlags(colIdConjunto.flags() & ~QtCore.Qt.ItemIsEditable)

            self.tblSemanticoMemoria.setItem(num, 0, colIdConjunto)
            self.tblSemanticoMemoria.setItem(num, 1, colConjunto)

    def gerarCelulaConjuntoVazia(self):
        colConjunto = QtWidgets.QTableWidgetItem('')
        colConjunto.setFlags(colConjunto.flags() & ~QtCore.Qt.ItemIsEditable)
        return colConjunto

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    principal = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(principal)
    principal.show()
    sys.exit(app.exec())
