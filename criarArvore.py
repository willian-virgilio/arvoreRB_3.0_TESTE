# Implementing Red-Black Tree in Python


import sys
import datetime



# ALTERADO COM SUCESSO
class No():
    def __init__(self, valor):
        self.valor = valor
        self.sucessor = None
        self.filhoEsquerdo = None
        self.filhoDireito = None
        self.cor = 1



class ArvoreRB():
    #Alterado com sucesso
    def __init__(self):
        self.TNULL = No(0)
        self.TNULL.cor = 0
        self.TNULL.filhoEsquerdo = None
        self.TNULL.filhoDireito = None
        self.raiz = self.TNULL
        self.imprimir = []

    def retornar_valor_corrigido(self):
        return len(self.vetor_grava_versao2)

    def gerar_log(self, menssagem):
        with open('log.txt', 'a') as arqv_log:
            data_e_hora_atuais = datetime.now()
            data_e_hora = "-----------" + str(data_e_hora_atuais) + "-----------\n"
            arqv_log.write(data_e_hora)
            arqv_log.write(menssagem)
            arqv_log.write('\n')
        arqv_log.close()
        with open('saida.txt', 'a') as arqv_saida:
            arqv_saida.write(menssagem)
            arqv_saida.write('\n')
        arqv_saida.close()
        print(menssagem)

    def retornar_versao(self, index, e_sucessor):
        print("Index", index - 1)
        print("lenght vetor", len(self.vetor_grava_versao2))

        if (e_sucessor == True):
            if (index - 1 <= len(self.vetor_grava_versao2)):
                a = self.vetor_grava_versao2[index - 1]
                return a

            else:
                a = self.vetor_grava_versao2[len(self.vetor_grava_versao2) - 1]

                msg = "Alerta: A versão solicitada para ser mostrada ainda é maior,\n " \
                      "que a ultima versão gravada,portanto sera mostrado\n" \
                      "o sucessor nó solicitado , da ultima versão gravada \n" \
                      "----------------------------------------------------------"
                self.gerar_log(msg)

                self.retornar_valor_corrigido()
                return a
        else:
            print("Valor variavel e_sucessor:", e_sucessor)
            print("o valor do indice do vetor grava versão 2 , na função retornar versão é:", index)
            print("O tamanho do vetor grava versão 2 é: ", len(self.vetor_grava_versao2))
            a = self.vetor_grava_versao2[index - 1]
            return a

            print("primeiro elemento do vetor", self.vetor_grava_versao2[0])
            print("Numero do indice do vetor da versão existente: ", index - 1)

    def buscar_sucessor(self, antecessor, versao):
        pass

    def __gravar_versao(self, valor, nivel, cor, lado):

        self.y = "%s;%s;%s;" % (valor, nivel, cor)
        self.z += self.y
        self.vetor_grava_versao1.append(valor)
        self.vetor_grava_versao1.append(str(nivel))
        self.vetor_grava_versao1.append(cor)
        self.vetor_grava_versao1.append(lado)

    def controledeVersao(self):
        self.controle_versao = self.controle_versao + 1
        print("numero de versão: ", self.controle_versao)
        if (self.controle_versao >= 100):
            msg = "O numero de versões alcançou o limite de 100!.\n O arquivo entrada.txt \n" \
                  "contem mais de 100 operacções de modificação( INC = incluir; REM = Remoção \n" \
                  "revise o arquivo de entrada para reduzir a quantidade de Elementos inclusos ou removidos\n" \
                  "---------------------------------------------------------------------------------------------"
            self.gerar_log(msg)
            exit()

    # aLTERADO COM SUCESSO
    def __ajustarAposDeletar(self, key5):
        while key5 != self.raiz and key5.cor == 0:
            if key5 == key5.sucessor.filhoEsquerdo:
                v7 = key5.sucessor.filhoDireito
                if v7.cor == 1:
                    v7.cor = 0
                    key5.sucessor.cor = 1
                    self.rotacao_esquerda(key5.sucessor)
                    v7 = key5.sucessor.filhoDireito

                if v7.filhoEsquerdo.cor == 0 and v7.filhoDireito.cor == 0:
                    v7.cor = 1
                    key5 = key5.sucessor
                else:
                    if v7.filhoDireito.cor == 0:
                        v7.filhoEsquerdo.cor = 0
                        v7.cor = 1
                        self.rotacionar_direita(v7)
                        v7 = key5.sucessor.filhoDireito

                    v7.cor = key5.sucessor.cor
                    key5.sucessor.cor = 0
                    v7.filhoDireito.cor = 0
                    self.rotacao_esquerda(key5.sucessor)
                    key5 = self.raiz
            else:
                v7 = key5.sucessor.filhoEsquerdo
                if v7.cor == 1:
                    v7.cor = 0
                    key5.sucessor.cor = 1
                    self.rotacionar_direita(key5.sucessor)
                    v7 = key5.sucessor.filhoEsquerdo

                if v7.filhoDireito.cor == 0 and v7.filhoDireito.cor == 0:
                    v7.cor = 1
                    key5 = key5.sucessor
                else:
                    if v7.filhoEsquerdo.cor == 0:
                        v7.filhoDireito.cor = 0
                        v7.cor = 1
                        self.rotacao_esquerda(v7)
                        v7 = key5.sucessor.filhoEsquerdo

                    v7.cor = key5.sucessor.cor
                    key5.sucessor.cor = 0
                    v7.filhoEsquerdo.cor = 0
                    self.rotacionar_direita(key5.sucessor)
                    key5 = self.raiz
        key5.cor = 0

    # aLTERADO COM SUCESSO
    def __transposicao_rb(self, v8, key6):
        if v8.sucessor == None:
            self.raiz = key6
        elif v8 == v8.sucessor.filhoEsquerdo:
            v8.sucessor.filhoEsquerdo = key6
        else:
            v8.sucessor.filhoDireito = key6
        key6.sucessor = v8.sucessor

    # Alterado com sucesso
    def __auxDel_no(self, novo_no, key7):
        z = self.TNULL
        while novo_no != self.TNULL:
            if novo_no.valor == key7:
                z = novo_no

            if novo_no.valor <= key7:
                novo_no = novo_no.filhoDireito
            else:
                novo_no = novo_no.filhoEsquerdo

        if z == self.TNULL:
            print("Cannot find key7 in the tree")
            return

        y = z
        y_original_color = y.cor
        if z.filhoEsquerdo == self.TNULL:
            x = z.filhoDireito
            self.__transposicao_rb(z, z.filhoDireito)
        elif (z.filhoDireito == self.TNULL):
            x = z.filhoEsquerdo
            self.__transposicao_rb(z, z.filhoEsquerdo)
        else:
            y = self.minimo(z.filhoDireito)
            y_original_color = y.cor
            x = y.filhoDireito
            if y.sucessor == z:
                x.sucessor = y
            else:
                self.__transposicao_rb(y, y.filhoDireito)
                y.filhoDireito = z.filhoDireito
                y.filhoDireito.sucessor = y

            self.__transposicao_rb(z, y)
            y.filhoEsquerdo = z.filhoEsquerdo
            y.filhoEsquerdo.sucessor = y
            y.cor = z.cor
        if y_original_color == 0:
            self.__ajustarAposDeletar(x)

    # alterado
    def rotacionarInsercao(self, key4):
        while key4.sucessor.cor == 1:
            if key4.sucessor == key4.sucessor.sucessor.filhoDireito:
                u = key4.sucessor.sucessor.filhoEsquerdo
                if u.cor == 1:
                    u.cor = 0
                    key4.sucessor.cor = 0
                    key4.sucessor.sucessor.cor = 1
                    key4 = key4.sucessor.sucessor
                else:
                    if key4 == key4.sucessor.filhoEsquerdo:
                        key4 = key4.sucessor
                        self.rotacionar_direita(key4)
                    key4.sucessor.cor = 0
                    key4.sucessor.sucessor.cor = 1
                    self.rotacao_esquerda(key4.sucessor.sucessor)
            else:
                u = key4.sucessor.sucessor.filhoDireito

                if u.cor == 1:
                    u.cor = 0
                    key4.sucessor.cor = 0
                    key4.sucessor.sucessor.cor = 1
                    key4 = key4.sucessor.sucessor
                else:
                    if key4 == key4.sucessor.filhoDireito:
                        key4 = key4.sucessor
                        self.rotacao_esquerda(key4)
                    key4.sucessor.cor = 0
                    key4.sucessor.sucessor.cor = 1
                    self.rotacionar_direita(key4.sucessor.sucessor)
            if key4 == self.raiz:
                break
        self.raiz.cor = 0





    #Alterado
    def minimo(self, novo_no):
        while novo_no.filhoEsquerdo != self.TNULL:
            novo_no = novo_no.filhoEsquerdo
        return novo_no


    #Alterado
    def rotacao_esquerda(self, key2):
        y = key2.filhoDireito
        key2.filhoDireito = y.filhoEsquerdo
        if y.filhoEsquerdo != self.TNULL:
            y.filhoEsquerdo.sucessor = key2

        y.sucessor = key2.sucessor
        if key2.sucessor == None:
            self.raiz = y
        elif key2 == key2.sucessor.filhoEsquerdo:
            key2.sucessor.filhoEsquerdo = y
        else:
            key2.sucessor.filhoDireito = y
        y.filhoEsquerdo = key2
        key2.sucessor = y
    #Alterado
    def rotacionar_direita(self, key3):
        y = key3.filhoEsquerdo
        key3.filhoEsquerdo = y.filhoDireito
        if y.filhoDireito != self.TNULL:
            y.filhoDireito.sucessor = key3

        y.sucessor = key3.sucessor
        if key3.sucessor == None:
            self.raiz = y
        elif key3 == key3.sucessor.filhoDireito:
            key3.sucessor.filhoDireito = y
        else:
            key3.sucessor.filhoEsquerdo = y
        y.filhoDireito = key3
        key3.sucessor = y
    #Alterado
    def inserirNovoNo(self, key1):
        novo_no = No(key1)
        novo_no.sucessor = None
        novo_no.valor = key1
        novo_no.filhoEsquerdo = self.TNULL
        novo_no.filhoDireito = self.TNULL
        novo_no.cor = 1

        y = None
        x = self.raiz

        while x != self.TNULL:
            y = x
            if novo_no.valor < x.valor:
                x = x.filhoEsquerdo
            else:
                x = x.filhoDireito

        novo_no.sucessor = y
        if y == None:
            self.raiz = novo_no
        elif novo_no.valor < y.valor:
            y.filhoEsquerdo = novo_no
        else:
            y.filhoDireito = novo_no

        if novo_no.sucessor == None:
            novo_no.cor = 0
            return

        if novo_no.sucessor.sucessor == None:
            return

        self.rotacionarInsercao(novo_no)

    #Alterado
    def deletarNo(self, valor):
        self.__auxDel_no(self.raiz, valor)
        self.controledeVersao()

        # Printing the tree

    def __mostrar(self, noVerificado, identador, final, e_raiz, contadory):

        if noVerificado != self.TNULL:
            #  print("valor do nó:", noVerificado.valor)
            sys.stdout.write(identador)
            if final:
                sys.stdout.write("DIR----")
                identador += "     "
            else:
                sys.stdout.write("ESQ----")
                identador += "|    "

            s_color = "R" if noVerificado.cor == 1 else "P"
            print(str(noVerificado.valor) + "(" + s_color + ")")
            self.imprimir.append(noVerificado.valor)
            self.__mostrar(noVerificado.filhoEsquerdo, identador, False, False, contadory=contadory + 1)
            self.__mostrar(noVerificado.filhoDireito, identador, True, False, contadory=contadory + 1)

    def mostrar_arvore(self):
        self.__mostrar (self.raiz,"",True,True,0)

        print(self.imprimir)
        self.imprimir.clear()




       # vetor_grava_versao1.append(self.z)
      #  d = str(vetor_grava_versao1).split(';')
       # print(d,end='\n')

       # self.__mostrar (self.raiz, "", True)
    def buscar_sucessor(self,antecessor,versao):
        pass

if __name__ == "__main__":
    bst = ArvoreRB()

    for i in range(1,21):
        bst.inserirNovoNo(i)
        bst.mostrar_arvore()
   # bst.inserirNovoNo(50)
  #  bst.inserirNovoNo(55)
  #  bst.inserirNovoNo(60)
  #  bst.inserirNovoNo(100)
  #  bst.inserirNovoNo(110)
  #  bst.inserirNovoNo(33)
  #  bst.inserirNovoNo(22)
  #  bst.inserirNovoNo(8)
  #  bst.mostrar_arvore()


    print("------------------------")





    print("\nAfter deleting an element")
  #  bst.deletarNo(8)
  #  bst.deletarNo(8)
    bst.mostrar_arvore()
