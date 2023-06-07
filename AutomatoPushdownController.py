import random
from random import randint
import string


class State:
    def __init__(self, dicTransition, dicInsert, dicRemove):
        self.transicao = dicTransition
        self.insere = dicInsert
        self.consome = dicRemove

class AutomatoPushdownController:
    def __init__(self):
        self.pilha = []
        self.estadoAtual = 0
        self.estado = []

        estadoTransicao1 = {
            'ID': 2,
            'SET': 3,
            'LPAREN': 1,
            'POWERSET': 1,
            'COMPLEMENT': 1,
            'empty': 4
        }

        estadoInsere1 = {
            'LPAREN': 'X'
        }

        estadoConsome1 = {
            'empty': 'empty'
        }

        self.estado.append(State(estadoTransicao1, estadoInsere1, estadoConsome1))

        estadoTransicao2 = {
            'ID': 3,
            'SET':3,
            'LPAREN': 1,
            'POWERSET': 1,
            'COMPLEMENT': 1,
        }

        estadoInsere2 = {
            'LPAREN': 'X'
        }

        estadoConsome2 = {
        }

        self.estado.append(State(estadoTransicao2, estadoInsere2, estadoConsome2))

        estadoTransicao3 = {
            'EQUALS': 1,
            'UNION': 1,
            'INTERSECTION': 1,
            'DIFFERENCE': 1,
            'PRODUCT': 1,
            'RPAREN': 3,
            'empty': 4
        }

        estadoInsere3 = {

        }

        estadoConsome3 = {
            'RPAREN': 'X',
            'empty': 'empty'
        }

        self.estado.append(State(estadoTransicao3, estadoInsere3, estadoConsome3))

        estadoTransicao4 = {
            'UNION': 1,
            'INTERSECTION': 1,
            'DIFFERENCE': 1,
            'PRODUCT': 1,
            'RPAREN': 3,
            'empty': 4
        }

        estadoInsere4 = {
        }

        estadoConsome4 = {
            'RPAREN': 'X',
            'empty': 'empty'
        }

        self.estado.append(State(estadoTransicao4, estadoInsere4, estadoConsome4))

        estadoTransicao5 = {

        }

        estadoInsere5 = {

        }

        estadoConsome5 = {
        }

        self.estado.append(State(estadoTransicao5, estadoInsere5, estadoConsome5))

        self.estadosFinais = [4]

    # Recebe uma entrada e a valida
    def analiseSintatica(self, linhaTokensTipo):
        # Prepara o automato para processar a entrada
        linhaTokensTipo.append(('empty', 'empty'))  # Adiciona o token de "final de entrada" a fila de entrada
        self.estadoAtual = 0  # Retorna o automato ao estado inicial
        self.pilha.clear()  # Limpa a pilha
        self.pilha.append(('empty', 'empty'))  # Adiciona o token de "base da pilha" a pilha do automato

        # Processa a entrada
        while len(linhaTokensTipo) > 0:
            token = linhaTokensTipo.pop(0)  # Toma o primeiro token da fila de entrada
            transicao = self.estado[self.estadoAtual].transicao.get(
                token[0])  # Toma o proximo estado do automato conforme o primeiro token da fila de entrada
            insere = self.estado[self.estadoAtual].insere.get(
                token[0])  # Toma o elemento a ser inserido na pilha conforme o primeiro token da fila de entrada
            consome = self.estado[self.estadoAtual].consome.get(
                token[0])  # Toma o elemento a ser removido na pilha conforme o primeiro token da fila de entrada

            if transicao == None:  # Retorna -1 caso não exista transição relacionada ao token da fila de entrada
                #print('Erro1')
                return -1
            if consome != None and len(
                    self.pilha) == 0:  # Retorna -1 caso seja exigido o consumo de um elemento da pilha e a mesma esteja vazia
                #print('Erro2')
                return -1
            if consome != None and consome != self.pilha.pop()[0]:  # Retorna -1 caso seja exigido o consumo de um elemento da pilha e o mesmo não esteja no topo
                #print('Erro3')
                return -1

            self.estadoAtual = transicao  # Muda o estado do automato
            if insere != None:  # Caso seja exigido adiciona um elemento a pilha do automato
                self.pilha.append(insere)

        # Verifica se apos processar a entrada o automato se encontra em estado final, caso sim retorna 0
        if self.estadoAtual in self.estadosFinais:
            return 0
        #print('Erro4')
        return -1