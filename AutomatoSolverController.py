from AutomatoLexicoController import *

class AutomatoSolverController:
    def __init__(self, entrada, conjUniverso):
        self.memConjunto = {}
        self.entrada = entrada
        self.pilha = list()
        if isinstance(conjUniverso, list):
            self.conjUniverso = set(conjUniverso)
        else:
            self.conjUniverso = conjUniverso
        self.numArgumento = {
            'EQUALS': 2,
            'UNION': 2,
            'INTERSECTION': 2,
            'PRODUCT': 2,
            'DIFFERENCE': 2,
            'COMPLEMENT': 1,
            'POWERSET': 1
        }
        self.index = len(self.entrada) - 1

    def resetar(self, entrada):
        self.memConjunto = {}
        self.entrada = entrada
        self.pilha = list()
        self.numArgumento = {
            'EQUALS': 2,
            'UNION': 2,
            'INTERSECTION': 2,
            'PRODUCT': 2,
            'DIFFERENCE': 2,
            'COMPLEMENT': 1,
            'POWERSET': 1
        }
        self.index = len(self.entrada) - 1

    def adicionarConjuntoAMemoria(self, strId, conj):
        if isinstance(conj, str):
            automatoLexico = AutomatoLexicoController(conj)
            automatoLexico.proximo()
            tokenConj = automatoLexico.proximo()
            if tokenConj != None and tokenConj[0] == 'SET':
                self.memConjunto[strId] = tokenConj[1]
        elif isinstance(conj, set):
            self.memConjunto[strId] = conj

    def removerConjuntoDaMemoria(self, strId):
        self.memConjunto.pop(strId)

    def uniao(self, conjA, conjB):
        if conjA == None or conjB == None:
            return None
        saida = conjA.union(conjB)
        return saida

    def interseccao(self, conjA, conjB):
        if conjA == None or conjB == None:
            return None
        saida = conjA.intersection(conjB)
        return saida

    def diferenca(self, conjA, conjB):
        if conjA == None or conjB == None:
            return None
        if conjB == set():
            return conjA
        elif conjA == set():
            return set()
        else:
            return conjA.difference(conjB)

    def produtoCartesiano(self, conjA, conjB):
        if conjA == None or conjB == None:
            return None
        saida = set()
        for elemA in conjA:
            for elemB in conjB:
                saida.add((elemA, elemB))
        return saida

    def complemento(self, conjA):
        if conjA == None or self.conjUniverso == None:
            return None
        return self.diferenca(self.conjUniverso, conjA)

    def conjuntoDasPartesCardinalidade(self, conjAOri, cardinalidade):
        conjA = list(conjAOri)
        saida = set()

        ponteiros = []
        cont = 0
        while cont < cardinalidade:
            ponteiros.append(cont)
            cont += 1

        saidaAux = set()
        for Ptr in ponteiros:
            saidaAux.add(conjA[Ptr])
        saida.add(frozenset(saidaAux))

        cont = cardinalidade - 1
        while (ponteiros[0] < len(conjA) - cardinalidade):
            if ponteiros[cont] < len(conjA) - 1:
                ponteiros[cont] += 1
            else:
                cont -= 1
                while (ponteiros[cont] == len(conjA) - (cardinalidade - cont)) and cont >= 0:
                    cont -= 1
                if cont != -1:
                    ponteiros[cont] += 1
                    cont += 1
                while cont != -1 and cont < cardinalidade:
                    ponteiros[cont] = ponteiros[cont - 1] + 1
                    cont += 1
                cont -= 1

            saidaAux = set()
            for ptr in ponteiros:
                saidaAux.add(conjA[ptr])
            saida.add(frozenset(saidaAux))
            # cont = cardinalidade - 1

        return saida

    def conjuntoDasPartes(self, conjA):
        if conjA == None:
            return None
        saida = set()
        if len(conjA) == 0:
            saida.add(frozenset({}))
            return saida
        cont = 1
        while cont <= len(conjA):
            saida = self.uniao(saida, self.conjuntoDasPartesCardinalidade(conjA, cont))
            cont += 1
        saida.add(frozenset({}))
        return saida

    def proximo(self):
        if len(self.entrada) == 0:
            return 'RESULTADO', 'Resultado: ' + str(self.pilha[0])
        token = self.entrada[0]

        if token[0] == 'SET':
            self.pilha.append(token[1])
            self.entrada.pop(0)
            return 'TRANSICAO', 'SET lido com sucesso'
        elif token[0] == 'ID':
            self.pilha.append(token[1])
            self.entrada.pop(0)
            return 'TRANSICAO', 'ID lido com sucesso'

        varDireita = None
        varEsquerda = None
        conjRes = None
        operacaoRealizada = None
        if(self.numArgumento.get(token[0]) == 1):
            if isinstance(self.pilha[-1], str):
                varDireita = self.memConjunto.get(self.pilha[-1])
                if varDireita == None:
                    return 'ERRO', 'SET da direita não encontrado'
                else:
                    #SET encontrado
                    pass
            else:
                varDireita = self.pilha[-1]

            if token[0] == 'COMPLEMENT':
                conjRes = self.complemento(varDireita)
                operacaoRealizada = '~' + str(varDireita)
            elif token[0] == 'POWERSET':
                if (len(varDireita) >= 8):
                    return 'ERRO', 'POWERSET envolvendo conjunto de cardinalidade maior que 8.'
                conjRes = self.conjuntoDasPartes(varDireita)
                operacaoRealizada = 'p' + str(varDireita)
            self.entrada.pop(0)
            self.pilha.pop(-1)
            self.pilha.append(conjRes)
        else:
            #Variavel da direita
            if isinstance(self.pilha[-1], str):
                varDireita = self.memConjunto.get(self.pilha[-1])
                if varDireita == None:
                    return 'ERRO', 'SET da direita não encontrado'
                else:
                    #SET encontrado
                    pass
            else:
                varDireita = self.pilha[-1]
            #Variavel da esquerda
            if isinstance(self.pilha[-2], str):
                if token[0] == 'EQUALS':
                    varEsquerda = self.pilha[-2]
                else:
                    varEsquerda = self.memConjunto.get(self.pilha[-2])
                    if varEsquerda == None:
                        return 'ERRO', 'SET da esquerda não encontrado'
                    else:
                        #SET encontrado
                        pass
            else:
                varEsquerda = self.pilha[-2]

            if token[0] == 'UNION':
                conjRes = self.uniao(varEsquerda, varDireita)
                operacaoRealizada = str(varEsquerda) + '\\/' + str(varDireita)
            elif token[0] == 'INTERSECTION':
                conjRes = self.interseccao(varEsquerda, varDireita)
                operacaoRealizada = str(varEsquerda) + '/\\' + str(varDireita)
            elif token[0] == 'PRODUCT':
                if (len(varDireita)*len(varEsquerda) >= 1000):
                    return 'ERRO', 'PRODUCT com resultado maior que 1000.'
                conjRes = self.produtoCartesiano(varEsquerda, varDireita)
                operacaoRealizada = str(varEsquerda) + 'x' + str(varDireita)
            elif token[0] == 'DIFFERENCE':
                conjRes = self.diferenca(varEsquerda, varDireita)
                operacaoRealizada = str(varEsquerda) + '-' + str(varDireita)
            elif token[0] == 'EQUALS':
                self.adicionarConjuntoAMemoria(varEsquerda, varDireita)
                operacaoRealizada = varEsquerda + '=' + str(varDireita)
                conjRes = varDireita

            self.entrada.pop(0)
            self.pilha.pop(-1)
            self.pilha.pop(-1)
            self.pilha.append(conjRes)

        return 'OPERACAO', operacaoRealizada

#BUG 10 avancar
#((~(((p(((E/\V)xI)x{-4, -3}))\/{4, -1})x{}))-{})xO
#((~(((p((({1,-1}/\{0,1})x{-1,0,1})x{-4, -3}))\/{4, -1})x{}))-{})x{0}