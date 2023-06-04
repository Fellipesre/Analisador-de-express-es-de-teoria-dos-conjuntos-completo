from AutomatoLexicoController import *

class AutomatoSolverController:
    def __init__(self, entrada, conjUniverso):
        self.memConjunto = {}
        self.entrada = entrada
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
        if len(self.entrada) == 1:
            return

        numArgs = self.numArgumento.get((self.entrada[self.index])[0])

        # Verifica se ha operadores que devem ser resolvidos primeiro
        subIndex = 1
        while subIndex <= numArgs:
            token = self.entrada[self.index - subIndex]
            if token[0] != 'ID' and token[0] != 'SET':
                self.index = self.index - subIndex
                return 'TRANSICAO', self.index - subIndex
            else:
                subIndex = subIndex + 1

        # Toma os conjuntos da memoria
        conj = []
        subIndex = 1
        conjNaoEncontrado = False
        while subIndex <= numArgs:
            token = self.entrada[self.index - subIndex]
            if token[0] == 'SET':
                conj.append(token[1])
            elif token[0] == 'ID':
                conjMem = self.memConjunto.get(token[1])
                if conjMem == None:
                    conjNaoEncontrado = True
                    #conj.append(token[1])
                else:
                    conj.append(conjMem)
            subIndex = subIndex + 1

        # Gera um conjunto novo caso o mesmo nao esteja na memoria

        operacaoRealizada = ''
        if conjNaoEncontrado:
            return 'ERRO', 1
        #elif conjNaoEncontrado and self.ignrCnjNaoDeclr:
        else:
            if (self.entrada[self.index])[0] == 'EQUALS':
                self.entrada.pop(self.index)
                self.entrada.pop(self.index - 1)
                self.entrada.pop(self.index - 2)
                if isinstance(conj[0], set) and isinstance(conj[1], str):
                    self.memConjunto[conj[1]] = conj[0]
                    self.entrada.insert(self.index - 1, ('SET', conj[1]))
                elif isinstance(conj[0], str) and isinstance(conj[1], set):
                    self.memConjunto[conj[0]] = conj[1]
                    self.entrada.insert(self.index - 1, ('SET', conj[0]))
                else:
                    return 'ERRO', 2
                return 'ATRIBUIÇÃO', len(self.memConjunto)
            elif (self.entrada[self.index])[0] == 'COMPLEMENT':
                self.entrada.pop(self.index)
                self.entrada.pop(self.index - 1)
                if isinstance(conj[0], set):
                    conjRes = self.complemento(conj[0])
                    self.entrada.insert(self.index - 1, ('SET', conjRes))
                    operacaoRealizada = '~' + str(conj[0])
                else:
                    return 'ERRO', 3

            elif (self.entrada[self.index])[0] == 'POWERSET':
                self.entrada.pop(self.index)
                self.entrada.pop(self.index - 1)
                if isinstance(conj[0], set):
                    conjRes = self.conjuntoDasPartes(conj[0])
                    self.entrada.insert(self.index - 1, ('SET', conjRes))
                    operacaoRealizada = 'p' + str(conj[0])
                else:
                    return 'ERRO', 4

            elif (self.entrada[self.index])[0] == 'UNION':
                self.entrada.pop(self.index)
                self.entrada.pop(self.index - 1)
                self.entrada.pop(self.index - 2)
                if isinstance(conj[0], set) and isinstance(conj[1], set):
                    conjRes = self.uniao(conj[1], conj[0])
                    self.entrada.insert(self.index - 2, ('SET', conjRes))
                    operacaoRealizada = str(conj[1]) + ' \\/ ' + str(conj[0])
                else:
                    return 'ERRO', 5

            elif (self.entrada[self.index])[0] == 'INTERSECTION':
                self.entrada.pop(self.index)
                self.entrada.pop(self.index - 1)
                self.entrada.pop(self.index - 2)
                if isinstance(conj[0], set) and isinstance(conj[1], set):
                    conjRes = self.interseccao(conj[1], conj[0])
                    self.entrada.insert(self.index - 2, ('SET', conjRes))
                    operacaoRealizada = str(conj[1]) + ' /\\ ' + str(conj[0])
                else:
                    return 'ERRO', 6

            elif (self.entrada[self.index])[0] == 'PRODUCT':
                self.entrada.pop(self.index)
                self.entrada.pop(self.index - 1)
                self.entrada.pop(self.index - 2)
                if isinstance(conj[0], set) and isinstance(conj[1], set):
                    conjRes = self.produtoCartesiano(conj[1], conj[0])
                    self.entrada.insert(self.index - 2, ('SET', conjRes))
                    operacaoRealizada = str(conj[1]) + ' x ' + str(conj[0])
                else:
                    return 'ERRO', 7

            elif (self.entrada[self.index])[0] == 'DIFFERENCE':
                self.entrada.pop(self.index)
                self.entrada.pop(self.index - 1)
                self.entrada.pop(self.index - 2)
                if isinstance(conj[0], set) and isinstance(conj[1], set):
                    conjRes = self.diferenca(conj[1], conj[0])
                    self.entrada.insert(self.index - 2, ('SET', conjRes))
                    operacaoRealizada = str(conj[1]) + ' - ' + str(conj[0])
                else:
                    return 'ERRO', 8

            self.index = len(self.entrada) - 1
            return 'OPERACAO', operacaoRealizada
#BUG 10 avancar
#((~(((p(((E/\V)xI)x{-4, -3}))\/{4, -1})x{}))-{})xO
#((~(((p((({1,-1}/\{0,1})x{-1,0,1})x{-4, -3}))\/{4, -1})x{}))-{})x{0}