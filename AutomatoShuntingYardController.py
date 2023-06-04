import random
from random import randint
import string

class AutomatoShuntingYardController:
    def __init__(self, entrada):
        self.entradaFixa = entrada
        self.pilha = []
        self.fila = []
        self.entrada = entrada
        self.precedencia = {
            'EQUALS': 0,
            'UNION': 1,
            'INTERSECTION': 2,
            'PRODUCT': 3,
            'DIFFERENCE': 4,
            'COMPLEMENT': 5,
            'POWERSET': 6
        }
        self.associatividade = {
            'EQUALS':'left',
            'UNION':'left',
            'INTERSECTION':'left',
            'PRODUCT':'left',
            'DIFFERENCE':'left',
            'COMPLEMENT':'left',
            'POWERSET':'left'
        }
        self.ultimoOperador = ("EMPTY", "EMPTY")

    def resetar(self, entrada):
        self.entradaFixa = entrada
        self.pilha = []
        self.fila = []
        self.entrada = entrada
        self.ultimoOperador = ("EMPTY", "EMPTY")

    def proximo(self):
        if len(self.entrada) == 0 and self.ultimoOperador == ("EMPTY", "EMPTY"):
            if len(self.pilha) > 0:
                self.fila.append(self.pilha.pop())
            else:
                self.ultimoOperador = ("END", "END")
                return self.entrada
        elif self.ultimoOperador == ("EMPTY", "EMPTY"):
            if (self.entrada[0])[0] == "ID" or (self.entrada[0])[0] == "SET":
                self.fila.append(self.entrada.pop(0))
            elif (self.entrada[0])[0] == "LPAREN":
                self.pilha.append(self.entrada.pop(0))
            elif (self.entrada[0])[0] == "RPAREN":
                self.ultimoOperador = self.entrada.pop(0)
            else:
                if len(self.pilha) == 0 or (self.pilha[-1])[0] == "LPAREN":
                    self.pilha.append(self.entrada.pop(0))
                else:
                    entradaPrecedencia = self.precedencia.get((self.entrada[0])[0])
                    entradaAssociatividade = self.associatividade.get((self.entrada[0])[0])
                    pilhaPrecedencia = self.precedencia.get((self.pilha[-1])[0])

                    if (entradaAssociatividade == 'left' and pilhaPrecedencia >= entradaPrecedencia) or (entradaAssociatividade == 'right' and pilhaPrecedencia > entradaPrecedencia):
                        self.ultimoOperador = self.entrada.pop(0)
                    else:
                        self.pilha.append(self.entrada.pop(0))
        elif self.ultimoOperador == ("RPAREN", ')'):
            if (self.pilha[-1])[0] == "LPAREN":
                self.pilha.pop()
                self.ultimoOperador = ("EMPTY", "EMPTY")
            else:
                self.fila.append(self.pilha.pop())
        else:
            if len(self.pilha) == 0 or (self.pilha[-1])[0] == "LPAREN":
                self.pilha.append(self.ultimoOperador)
                self.ultimoOperador = ("EMPTY", "EMPTY")
            else:
                entradaPrecedencia = self.precedencia.get(self.ultimoOperador[0])
                entradaAssociatividade = self.associatividade.get(self.ultimoOperador[0])
                pilhaPrecedencia = self.precedencia.get((self.pilha[-1])[0])

                if (entradaAssociatividade == 'left' and pilhaPrecedencia < entradaPrecedencia) or (entradaAssociatividade == 'right' and pilhaPrecedencia <= entradaPrecedencia):
                    self.pilha.append(self.ultimoOperador)
                    self.ultimoOperador = ("EMPTY", "EMPTY")
                else:
                    self.fila.append(self.pilha.pop())

        return None

    def saida(self):
        tokenGerado = ('EMPTY', 'EMPTY')
        while tokenGerado[0] != 'END':
            passo = self.proximo()
            tokenGerado = ('EMPTY', 'EMPTY') if passo is None else ('END', 'END')
        retorno = self.fila
        self.resetar(self.entradaFixa)
        return retorno