import time
import timeit
import random
from random import randint
import string

LIMITE_CONJUNTO_DAS_PARTES = 8
LIMITE_PRODUTO_CARTESIANO = 1000

class AutomatoLexicoController:
    def __init__(self, entrada):
        self.entrada = entrada
        self.indexInicioToken = 0
        self.indexFinalToken = 0
        self.estadoAutomato = 0
        self.tokenGerado = ("EMPTY", "EMPTY")

    def resetar(self, entrada):
        self.entrada = entrada
        self.indexInicioToken = 0
        self.indexFinalToken = 0
        self.estadoAutomato = 0
        self.tokenGerado = ("EMPTY", "EMPTY")

    def proximo(self):
        #print('Index inicio: ', end='')
        #print(self.indexInicioToken)
        #print('Index final: ', end='')
        #print(self.indexFinalToken)
        #print('Estado automato: ', end='')
        #print(self.estadoAutomato)
        #if self.indexFinalToken < len(self.entrada):
        #    print('Entrada: ', end='')
        #    print(self.entrada[self.indexFinalToken])
        #print('Token armazenado: ', end='')
        #print(self.tokenGerado)
        #print('-------------------------')

        if self.indexInicioToken >= len(self.entrada):
            if self.indexInicioToken != self.indexFinalToken:
                self.tokenGerado = ("ERRO", "-1")
                return "ERRO", "-1"
            else:
                self.tokenGerado = ("END", "END")
                return "END", "END"

        if self.estadoAutomato == 0:
            if self.entrada[self.indexFinalToken] == ' ':
                self.indexFinalToken += 1
                self.indexInicioToken = self.indexFinalToken
            
            elif self.entrada[self.indexFinalToken] == '\\':
                self.indexFinalToken += 1
                self.estadoAutomato = 1

            elif self.entrada[self.indexFinalToken] == '/':
                self.indexFinalToken += 1
                self.estadoAutomato = 3

            elif 'A' <= self.entrada[self.indexFinalToken] <= 'Z':
                self.indexFinalToken += 1
                self.estadoAutomato = 11

            elif self.entrada[self.indexFinalToken] == '(':
                self.indexFinalToken += 1
                self.estadoAutomato = 9

            elif self.entrada[self.indexFinalToken] == ')':
                self.indexFinalToken += 1
                self.estadoAutomato = 10

            elif self.entrada[self.indexFinalToken] == 'x':
                self.indexFinalToken += 1
                self.estadoAutomato = 6

            elif self.entrada[self.indexFinalToken] == '-':
                self.indexFinalToken += 1
                self.estadoAutomato = 7

            elif self.entrada[self.indexFinalToken] == 'p':
                self.indexFinalToken += 1
                self.estadoAutomato = 8

            elif self.entrada[self.indexFinalToken] == '~':
                self.indexFinalToken += 1
                self.estadoAutomato = 5

            elif self.entrada[self.indexFinalToken] == '=':
                self.indexFinalToken += 1
                self.estadoAutomato = 14

            elif self.entrada[self.indexFinalToken] == '{':
                self.indexFinalToken += 1
                self.estadoAutomato = 13
            else:
                self.tokenGerado = ("ERRO", "0")
                return "ERRO", "0"

        elif self.estadoAutomato == 1:
            if self.entrada[self.indexFinalToken] == '/':
                self.indexFinalToken += 1
                self.estadoAutomato = 2
            else:
                self.tokenGerado = ("ERRO", "1")
                return "ERRO", "1"

        elif self.estadoAutomato == 2:
            self.estadoAutomato = 0
            valor = self.entrada[self.indexInicioToken:self.indexFinalToken]
            self.indexInicioToken = self.indexFinalToken
            self.tokenGerado = ("UNION", valor)
            return "UNION", valor

        elif self.estadoAutomato == 3:
            if self.entrada[self.indexFinalToken] == '\\':
                self.indexFinalToken += 1
                self.estadoAutomato = 4
            else:
                self.tokenGerado = ("ERRO", "3")
                return "ERRO", "3"

        elif self.estadoAutomato == 4:
            self.estadoAutomato = 0
            valor = self.entrada[self.indexInicioToken:self.indexFinalToken]
            self.indexInicioToken = self.indexFinalToken
            self.tokenGerado = ("INTERSECTION", valor)
            return "INTERSECTION", valor

        elif self.estadoAutomato == 5:
            self.estadoAutomato = 0
            valor = self.entrada[self.indexInicioToken:self.indexFinalToken]
            self.indexInicioToken = self.indexFinalToken
            self.tokenGerado = ("COMPLEMENT", valor)
            return "COMPLEMENT", valor

        elif self.estadoAutomato == 6:
            self.estadoAutomato = 0
            valor = self.entrada[self.indexInicioToken:self.indexFinalToken]
            self.indexInicioToken = self.indexFinalToken
            self.tokenGerado = ("PRODUCT", valor)
            return "PRODUCT", valor

        elif self.estadoAutomato == 7:
            self.estadoAutomato = 0
            valor = self.entrada[self.indexInicioToken:self.indexFinalToken]
            self.indexInicioToken = self.indexFinalToken
            self.tokenGerado = ("DIFFERENCE", valor)
            return "DIFFERENCE", valor

        elif self.estadoAutomato == 8:
            self.estadoAutomato = 0
            valor = self.entrada[self.indexInicioToken:self.indexFinalToken]
            self.indexInicioToken = self.indexFinalToken
            self.tokenGerado = ("POWERSET", valor)
            return "POWERSET", valor

        elif self.estadoAutomato == 9:
            self.estadoAutomato = 0
            valor = self.entrada[self.indexInicioToken:self.indexFinalToken]
            self.indexInicioToken = self.indexFinalToken
            self.tokenGerado = ("LPAREN", valor)
            return "LPAREN", valor

        elif self.estadoAutomato == 10:
            self.estadoAutomato = 0
            valor = self.entrada[self.indexInicioToken:self.indexFinalToken]
            self.indexInicioToken = self.indexFinalToken
            self.tokenGerado = ("RPAREN", valor)
            return "RPAREN", valor

        elif self.estadoAutomato == 11:
            if self.indexFinalToken < len(self.entrada) and ('A' <= self.entrada[self.indexFinalToken] <= 'Z' or '0' <= self.entrada[self.indexFinalToken] <= '9'):
                self.indexFinalToken += 1
                self.estadoAutomato = 11
            else:
                #self.indexFinalToken += 1
                self.estadoAutomato = 12

        elif self.estadoAutomato == 12:
            self.estadoAutomato = 0
            valor = self.entrada[self.indexInicioToken:self.indexFinalToken]
            self.indexInicioToken = self.indexFinalToken
            self.tokenGerado = ("ID", valor)
            return "ID", valor

        elif self.estadoAutomato == 13:
            while self.indexFinalToken < len(self.entrada):
                if self.entrada[self.indexFinalToken] == '}':
                    break
                self.indexFinalToken += 1

            valor = self.geraConjunto(self.entrada[self.indexInicioToken:(self.indexFinalToken + 1)])
            if valor == None:
                self.tokenGerado = ("ERRO", "4")
                return "ERRO", "4"
            else:
                self.indexFinalToken += 1
                self.indexInicioToken = self.indexFinalToken
                self.estadoAutomato = 0
                self.tokenGerado = ("SET", valor)
                return "SET", valor

        elif self.estadoAutomato == 14:
            self.estadoAutomato = 0
            valor = self.entrada[self.indexInicioToken:self.indexFinalToken - 1]
            self.indexInicioToken = self.indexFinalToken
            self.tokenGerado = ("EQUALS", valor)
            return "EQUALS", valor

    def saida(self):
        retorno = []

        tokenGerado = ('EMPTY', 'EMPTY')
        while tokenGerado[0] != 'END':
            saidaCiclo = self.proximo()
            if saidaCiclo is None:
                tokenGerado = ('EMPTY', 'EMPTY')
            elif saidaCiclo[0] == 'ERRO':
                self.resetar(self.entrada)
                return None
            else:
                tokenGerado = saidaCiclo
                if tokenGerado != ('END', 'END'):
                    retorno.append(tokenGerado)
        self.resetar(self.entrada)
        return retorno

    def geraConjunto(self, entrada):
        Estado = 0
        PtrIniTkn = 0
        PtrFimTkn = 0
        Saida = set()

        while entrada[PtrIniTkn] != '}':
            # print('Estado', end = ' ')
            # print(Estado)
            # print('IniTkn', end = ' ')
            # print(PtrIniTkn, entrada[PtrIniTkn])
            # print('EndTkn', end = ' ')
            # print(PtrFimTkn, end = ' ')
            # print(entrada[PtrFimTkn])

            # Estado 0
            if entrada[PtrFimTkn] == '{' and Estado == 0:
                PtrIniTkn += 1
                PtrFimTkn += 1
                Estado = 1


            # Estado 1
            elif entrada[PtrFimTkn] == ' ' and Estado == 1:
                PtrIniTkn += 1
                PtrFimTkn += 1
                Estado = 1

            elif (entrada[PtrFimTkn] >= '0' and entrada[PtrFimTkn] <= '9') and Estado == 1:
                # PtrIniTkn += 1
                PtrFimTkn += 1
                Estado = 3

            elif ((entrada[PtrFimTkn] >= 'A' and entrada[PtrFimTkn] <= 'Z') or (
                    entrada[PtrFimTkn] >= 'a' and entrada[PtrFimTkn] <= 'z')) and Estado == 1:
                # PtrIniTkn += 1
                PtrFimTkn += 1
                Estado = 2

            elif entrada[PtrFimTkn] == '.' and Estado == 1:
                # PtrIniTkn += 1
                PtrFimTkn += 1
                Estado = 8

            elif (entrada[PtrFimTkn] == '+' or entrada[PtrFimTkn] == '-') and Estado == 1:
                # PtrIniTkn += 1
                PtrFimTkn += 1
                Estado = 9


            # Estado 2
            elif ((entrada[PtrFimTkn] >= 'A' and entrada[PtrFimTkn] <= 'Z') or (
                    entrada[PtrFimTkn] >= 'a' and entrada[PtrFimTkn] <= 'z')) and Estado == 2:
                PtrFimTkn += 1
                Estado = 2

            elif (entrada[PtrFimTkn] >= '0' and entrada[PtrFimTkn] <= '9') and Estado == 2:
                PtrFimTkn += 1
                Estado = 2

            elif entrada[PtrFimTkn] == ' ' and Estado == 2:
                # print('PALAVRA GERADA')
                Saida.add(entrada[PtrIniTkn:PtrFimTkn])
                PtrIniTkn = PtrFimTkn
                Estado = -1

            elif entrada[PtrFimTkn] == ',' and Estado == 2:
                # print('PALAVRA GERADA')
                Saida.add(entrada[PtrIniTkn:PtrFimTkn])
                PtrFimTkn += 1
                PtrIniTkn = PtrFimTkn
                Estado = 1

            elif entrada[PtrFimTkn] == '}' and Estado == 2:
                # print('PALAVRA GERADA')
                Saida.add(entrada[PtrIniTkn:PtrFimTkn])
                PtrIniTkn = PtrFimTkn


            # Estado 3
            elif (entrada[PtrFimTkn] >= '0' and entrada[PtrFimTkn] <= '9') and Estado == 3:
                PtrFimTkn += 1
                Estado = 3

            elif ((entrada[PtrFimTkn] >= 'A' and entrada[PtrFimTkn] <= 'Z') or (
                    entrada[PtrFimTkn] >= 'a' and entrada[PtrFimTkn] <= 'z')) and Estado == 3:
                PtrFimTkn += 1
                Estado = 2

            elif entrada[PtrFimTkn] == '.' and Estado == 3:
                PtrFimTkn += 1
                Estado = 4

            elif entrada[PtrFimTkn] == ' ' and Estado == 3:
                # print('INTEIRO GERADO')
                Saida.add(int(entrada[PtrIniTkn:PtrFimTkn]))
                PtrIniTkn = PtrFimTkn
                Estado = -1

            elif entrada[PtrFimTkn] == ',' and Estado == 3:
                # print('INTEIRO GERADO')
                Saida.add(int(entrada[PtrIniTkn:PtrFimTkn]))
                PtrFimTkn += 1
                PtrIniTkn = PtrFimTkn
                Estado = 1

            elif entrada[PtrFimTkn] == '}' and Estado == 3:
                # print('INTEIRO GERADO')
                Saida.add(int(entrada[PtrIniTkn:PtrFimTkn]))
                PtrIniTkn = PtrFimTkn


            # Estado 4
            elif (entrada[PtrFimTkn] >= '0' and entrada[PtrFimTkn] <= '9') and Estado == 4:
                PtrFimTkn += 1
                Estado = 4

            elif entrada[PtrFimTkn] == 'e' and Estado == 4:
                PtrFimTkn += 1
                Estado = 5

            elif entrada[PtrFimTkn] == ' ' and Estado == 4:
                # print('FRACIONARIO GERADO')
                Saida.add(float(entrada[PtrIniTkn:PtrFimTkn]))
                PtrIniTkn = PtrFimTkn
                Estado = -1

            elif entrada[PtrFimTkn] == ',' and Estado == 4:
                # print('FRACIONARIO GERADO')
                Saida.add(float(entrada[PtrIniTkn:PtrFimTkn]))
                PtrFimTkn += 1
                PtrIniTkn = PtrFimTkn
                Estado = 1

            elif entrada[PtrFimTkn] == '}' and Estado == 4:
                # print('FRACIONARIO GERADO')
                Saida.add(float(entrada[PtrIniTkn:PtrFimTkn]))
                PtrIniTkn = PtrFimTkn


            # Estado 5
            elif (entrada[PtrFimTkn] == '+' or entrada[PtrFimTkn] == '-') and Estado == 5:
                PtrFimTkn += 1
                Estado = 6

            elif (entrada[PtrFimTkn] >= '0' and entrada[PtrFimTkn] <= '9') and Estado == 5:
                PtrFimTkn += 1
                Estado = 7


            # Estado 6
            elif (entrada[PtrFimTkn] >= '0' and entrada[PtrFimTkn] <= '9') and Estado == 6:
                PtrFimTkn += 1
                Estado = 7

                # Estado 7
            elif (entrada[PtrFimTkn] >= '0' and entrada[PtrFimTkn] <= '9') and Estado == 7:
                PtrFimTkn += 1
                Estado = 7

            elif entrada[PtrFimTkn] == ' ' and Estado == 7:
                # print('FRACIONARIO GERADO')
                Saida.add(float(entrada[PtrIniTkn:PtrFimTkn]))
                PtrIniTkn = PtrFimTkn
                Estado = -1

            elif entrada[PtrFimTkn] == ',' and Estado == 7:
                # print('FRACIONARIO GERADO')
                Saida.add(float(entrada[PtrIniTkn:PtrFimTkn]))
                PtrFimTkn += 1
                PtrIniTkn = PtrFimTkn
                Estado = 1

            elif entrada[PtrFimTkn] == '}' and Estado == 7:
                # print('FRACIONARIO GERADO')
                Saida.add(float(entrada[PtrIniTkn:PtrFimTkn]))
                PtrIniTkn = PtrFimTkn


            # Estado 8
            elif (entrada[PtrFimTkn] >= '0' and entrada[PtrFimTkn] <= '9') and Estado == 8:
                PtrFimTkn += 1
                Estado = 4


            # Estado 9
            elif entrada[PtrFimTkn] == '.' and Estado == 9:
                PtrFimTkn += 1
                Estado = 8

            elif (entrada[PtrFimTkn] >= '0' and entrada[PtrFimTkn] <= '9') and Estado == 9:
                PtrFimTkn += 1
                Estado = 10


            # Estado 10
            elif (entrada[PtrFimTkn] >= '0' and entrada[PtrFimTkn] <= '9') and Estado == 10:
                PtrFimTkn += 1
                Estado = 10

            elif entrada[PtrFimTkn] == '.' and Estado == 10:
                PtrFimTkn += 1
                Estado = 4

            elif entrada[PtrFimTkn] == ' ' and Estado == 10:
                # print('INTEIRO GERADO')
                Saida.add(int(entrada[PtrIniTkn:PtrFimTkn]))
                PtrIniTkn = PtrFimTkn
                Estado = -1

            elif entrada[PtrFimTkn] == ',' and Estado == 10:
                # print('INTEIRO GERADO')
                Saida.add(int(entrada[PtrIniTkn:PtrFimTkn]))
                PtrFimTkn += 1
                PtrIniTkn = PtrFimTkn
                Estado = 1

            elif entrada[PtrFimTkn] == '}' and Estado == 10:
                # print('INTEIRO GERADO')
                Saida.add(int(entrada[PtrIniTkn:PtrFimTkn]))
                PtrIniTkn = PtrFimTkn


            # Estado -1
            elif entrada[PtrFimTkn] == ' ' and Estado == -1:
                PtrIniTkn += 1
                PtrFimTkn += 1
                Estado = -1

            elif entrada[PtrFimTkn] == ',' and Estado == -1:
                PtrFimTkn += 1
                PtrIniTkn = PtrFimTkn
                Estado = 1

            elif entrada[PtrFimTkn] == '}' and Estado == -1:
                PtrIniTkn = PtrFimTkn
                Estado = -1


            # Erro
            else:
                return None

        return Saida

class ExpToken:
    def __init__(self):
        self.ListaTokensTipo = []
        self.ListaTokensValor = []

def GeraConj(NumElem):
    Saida = set()
        
    Cont = 0
    while Cont < NumElem:
        Elem = randint(-(2*NumElem), (2*NumElem))
        while Elem in Saida:
            Elem = randint(-(2*NumElem), (2*NumElem))
        Saida.add(Elem)
        Cont += 1
        
    return Saida

def GeraParsingEsq(NumPassos):
    OperadoresTokens = ['UNION', 'INTERSECTION', 'PRODUCT', 'DIFFERENCE', 'COMPLEMENT', 'POWERSET']
    OperadoresSimbolos = ['\\/', '/\\', 'x', '-', '~', 'p']   
    
    Entrada = ExpToken()
    Saida = []
    ConjEsq = ''
    ConjDir = ''
    #Aleatoriza operando da esquerda
    if randint(0, 1) == 0:
        ConjEsq = GeraConj(randint(0, 7))
    else:
        ConjEsq = random.choice(string.ascii_uppercase)
    #Aleatoriza operando da direita
    if randint(0, 1) == 0:
        ConjDir = GeraConj(randint(0, 7))
    else:
        ConjDir = random.choice(string.ascii_uppercase)
    #Aleatoriza operador    
    OpNum = randint(0, 5)
    
    #Operador binario
    if OpNum >= 0 and OpNum <= 3:
        #Operando da esquerda
        Entrada.ListaTokensValor.append(ConjEsq)
        if type(ConjEsq) == set:
            Entrada.ListaTokensTipo.append('SET')
        else:
            Entrada.ListaTokensTipo.append('ID')
        
        #Operador    
        Entrada.ListaTokensValor.append(OperadoresSimbolos[OpNum])
        Entrada.ListaTokensTipo.append(OperadoresTokens[OpNum])
        
        #Operando da direita
        Entrada.ListaTokensValor.append(ConjDir)
        if type(ConjDir) == set:
            Entrada.ListaTokensTipo.append('SET')
        else:
            Entrada.ListaTokensTipo.append('ID')        
            
        #Monta a saida
        Saida.append(ConjEsq)
        Saida.append(ConjDir)
        Saida.append(OperadoresTokens[OpNum])
        
    #Operador unario
    else:
        #Operador    
        Entrada.ListaTokensValor.append(OperadoresSimbolos[OpNum])
        Entrada.ListaTokensTipo.append(OperadoresTokens[OpNum])
        
        #Operando da direita
        Entrada.ListaTokensValor.append(ConjDir)
        if type(ConjDir) == set:
            Entrada.ListaTokensTipo.append('SET')
        else:
            Entrada.ListaTokensTipo.append('ID')
            
        #Monta a saida
        Saida.append(ConjDir)
        Saida.append(OperadoresTokens[OpNum])              
    
    Cont = 1
    while Cont < NumPassos:
        #Aleatoriza operador    
        OpNum = randint(0, 5)
        #Aleatoriza operando da direita
        if OpNum < 3:
            if randint(0, 1) == 0:
                ConjDir = GeraConj(randint(0, 7))
            else:
                ConjDir = random.choice(string.ascii_uppercase)        
        
        #Insercao dos parenteses laterais
        Entrada.ListaTokensTipo.insert(0, 'LPAREN')
        Entrada.ListaTokensValor.insert(0, '(')
        Entrada.ListaTokensTipo.append('RPAREN')
        Entrada.ListaTokensValor.append(')')        
        #Operador binario
        if OpNum >= 0 and OpNum <= 3:
            #Operador    
            Entrada.ListaTokensValor.append(OperadoresSimbolos[OpNum])
            Entrada.ListaTokensTipo.append(OperadoresTokens[OpNum])
            
            #Operando da direita
            Entrada.ListaTokensValor.append(ConjDir)
            if type(ConjDir) == set:
                Entrada.ListaTokensTipo.append('SET')
            else:
                Entrada.ListaTokensTipo.append('ID')        
                
            #Monta a saida
            Saida.append(ConjDir)
            Saida.append(OperadoresTokens[OpNum])
            
        #Operador unario
        else:
            #Operador    
            Entrada.ListaTokensValor.insert(0, OperadoresSimbolos[OpNum])
            Entrada.ListaTokensTipo.insert(0, OperadoresTokens[OpNum])
                
            #Monta a saida
            Saida.append(OperadoresTokens[OpNum])         
        
        Cont += 1
        
    return [Entrada, Saida]

#ale = GeraParsingEsq(9)
#lstEntradaTokens = (ale[0]).ListaTokensTipo
#lstEntrada = (ale[0]).ListaTokensValor
#entrada = ''
#for elem in lstEntrada:
#    if(str(elem) == 'set()'):
#        entrada = entrada + '{}'
#    else:
#        entrada = entrada + str(elem)

#print(entrada)
#lstSaida = []
#novo = AutomatoLexicoController(entrada)
#while (novo.tokenGerado[1] != 'END' and novo.tokenGerado[0] != 'ERRO'):
#    aux = novo.proximo()
#    if(aux != None and aux[0] != 'END'):
#        lstSaida.append(aux[0])
#print(novo.tokenGerado)
#print(lstEntradaTokens)
#print(lstSaida)
#Erros
#'((p((((((F/\R)xA)/\D)/\Q)/\F)-F))\/{8, -12, -10, -8, -3, -1})\/L'