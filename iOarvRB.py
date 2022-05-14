
from criarArvore import ArvoreRB


class Arquivo:



    def __init__(self,nomeArqv):
        self.nomeArqv = nomeArqv
        self.smsErro = False
        self.vetor = []



    def lerArquivo(self,nome):
        abrir_arquivo = open(nome, 'r')
        for comando in abrir_arquivo:
            comando = comando.rstrip()
            print("Mostrar comandos,",comando)
            self.vetor.append(comando)
        abrir_arquivo.close()

    def loopDeGravacao(self,x):

        arqv_saida = open('saida.txt', 'w')
        for i in range(len(x)):
            a = x[i]
            arqv_saida.write(a + ' ')
        arqv_saida.write('\n')

    def smsdeErro(self,sms):

        self.smsErro = 'V'


    def testeEscrita(self,nome):
       # print(self.controle_versao)

        print("Tamanho do vetor1: ",len(self.vetor))
        arqv_saida = open(nome, 'a')
        arqv_saida.truncate(0)
        arvore = ArvoreRB()


        for i in range(0,len(self.vetor),1):

            # O primeiro elemento da lista separador é o comando, o segundo é o valor lista_comandos_e_valores = [0]
            lista_comandos_e_valores = self.vetor[i].split()
            print("toda a lista :",lista_comandos_e_valores)
           # print("Tamanho da lista apos split: ", len(lista_comandos_e_valores))

            # primeiro if, caso o vetor1addr tenha indices maior que 2, então ele é o comando SUC de sucessor
            if( len(lista_comandos_e_valores) > 2):


                print("A versão de busca do sucessor é:", int(lista_comandos_e_valores[2]))

                 # if (c >= lista_comandos_e_valores[2] ):
                 #    arqv_saida.write(lista_comandos_e_valores[0] + ' ')
                 #   arqv_saida.write(lista_comandos_e_valores[1] + ' ')
                  #  arqv_saida.write(lista_comandos_e_valores[c] + ' ')

                      # print("Elementos salvos desta  versão: ",a)
                valor_de_referencia = int(lista_comandos_e_valores[1])

                print("O valor de pesquisa de sucessor: ",valor_de_referencia)


                corrigido = arvore.retornar_valor_corrigido()
                print("Tipo variavel corrigido: ",type(corrigido))

                print("A versão solicitada ", lista_comandos_e_valores[2])
                versao_referencia = int(lista_comandos_e_valores[2])
                if (versao_referencia > corrigido):
                    print("Valor da versão solicitada agora é: ",corrigido)
                    versao_referencia = corrigido
                print("VErsão corrigido: ", versao_referencia)

                a = arvore.retornar_versao(versao_referencia, True)

                arqv_saida.write(lista_comandos_e_valores[0] + ' ')
                arqv_saida.write(lista_comandos_e_valores[1] + ' ')
                arqv_saida.write(str(versao_referencia) + '\n')

               # nova.buscar_sucessor(int(lista_comandos_e_valores[1]),int(lista_comandos_e_valores[2]))

                x = ''
                tamanho_vetor_a = len(a)
                # if(len(a) == 0)
                print("Tamanho do len de a:",tamanho_vetor_a)

                for i in range(0,tamanho_vetor_a,4):

                    valor_atual = int(a[i])

                    if (valor_de_referencia < valor_atual ):
                        if (tamanho_vetor_a < 5):
                            x = str(a[i])
                            break

                        else:

                            proximo = a[i + 4]
                            print("o valor do proximo nó:")
                            print(proximo,end='\n')

                            if (valor_de_referencia < int(proximo) ):
                                x = str(proximo)
                                break

                    else:
                        x = 'INF'
                    print("este é o sucessor", x)

                arqv_saida.write(str(x))

                arqv_saida.write('\n')
            # verificar erro AttributeError: 'str' object has no attribute 'loopDeGravacao'

            else:
                if(lista_comandos_e_valores[0] == 'INC'):
                #print("O comando é :", lista_comandos_e_valores[0])
                # print("O elemento a ser INCLUIDO é: ", lista_comandos_e_valores[1])






                    arvore.inserirNovoNo(lista_comandos_e_valores[1])

                    print("Novo No: ", lista_comandos_e_valores[1])
                    arvore.mostrar_arvore()





                if(lista_comandos_e_valores[0] == 'REM'):



                # print("O comando é :", lista_comandos_e_valores[0])
                # print("O elemento a ser REMOVIDO é: ", lista_comandos_e_valores[1])

                    arvore.deletarNo(lista_comandos_e_valores[1])
                    print("\n ----- Depois deletar o elemento: ",lista_comandos_e_valores[1])

                    arvore.mostrar_arvore()
                  #  self.controle_versao += self.controle_versao

                if (lista_comandos_e_valores[0] == 'IMP'):
                    concatenar_raiz = ''
                    concatenar_antes = ''
                    concatenar_apos = ''
                    concatenar_no01_nivel01 = ''
                    arqv_saida.write('IMP ')
                    arqv_saida.write(lista_comandos_e_valores[1])
                    arqv_saida.write('\n')


                    # print("O comando é :", lista_comandos_e_valores[0])
                    #  print(ta"O elemento a ser INCLUID é: ", lista_comandos_e_valores[1],end=' ' )

                    # for i in range(len(lista_comandos_e_valores)):
                    print(type(lista_comandos_e_valores[1]))

                    if lista_comandos_e_valores[1] == '0' :
                        msg = "O valor da versão solicitada para impressão IMP é 0," \
                              "\n a primeira versão começa com valor interio 1 \n" \
                              "-----------------------------------------------------"

                        arvore.gerar_log()
                        exit()
                    else:
                        controle = True


                        a = arvore.retornar_versao((int(lista_comandos_e_valores[1])),False)
                        tamanho_vetor_a = len(a)
                        print("Tamanho vetor a antes do for:", tamanho_vetor_a)

                        concatenar_raiz = a[0] + ','
                        concatenar_raiz += a[1] + ','
                        concatenar_raiz += a[2] + ','
                        print("Esta é a raiz: ", concatenar_raiz)
                        if(tamanho_vetor_a <= 4):
                            arqv_saida.write(concatenar_raiz)

                        else:
                            concatenar_antes += a[4] + ','
                            concatenar_antes += a[5] + ','
                            concatenar_antes += a[6] + ','
                            print("Este é o primeiro nó ", concatenar_antes)

      #                          if (lista_comandos_e_valores[1] == '1'):
       #                             arqv_saida.write(concatenar_raiz)
        #                            print("controle antes de 1:", controle)
         #                           controle = False
          #                          print("valor controle depois 1: ",controle)


                          #      if lista_comandos_e_valores[1] == '2':
                           #         arqv_saida.write(concatenar_antes)
                            #        arqv_saida.write(concatenar_raiz)
                             #       print("controle antes de 2:", controle)
                              #      controle = False
                               #     print("valor controle depois 2: ", controle)

                            controle_entrada = False

                            for i in range(8,tamanho_vetor_a,4):
                                print("Valore de i:", i)
                                valor = a[i]
                                nivel = a[i+1]
                                cor = a[i+2]

                                if (nivel != '1'):
                                    if(controle_entrada == False):
                                        concatenar_antes += valor + ','
                                        concatenar_antes += nivel + ','
                                        concatenar_antes += cor + ','
                                        print("Valore concatenado antes da raiz", concatenar_antes)
                                    ################a ser removio###########
                                    if (controle_entrada == True):
                                        concatenar_apos += valor + ','
                                        concatenar_apos += nivel + ','
                                        concatenar_apos += cor + ','
                                        print("Esta é concaternar depois ", concatenar_apos)
                                    #############a ser removido#################

                                    print("Passou do no 1 do nivel 1", controle_entrada)
                                elif (a[i + 1] == '1') and (controle_entrada == False):
                                    concatenar_no01_nivel01 = valor + ','
                                    concatenar_no01_nivel01 += nivel + ','
                                    concatenar_no01_nivel01 += cor + ','
                                    controle_entrada = True
                                    print("Esta é no 01 do nivel 01 ", concatenar_no01_nivel01)

                        if(tamanho_vetor_a>4):

                            arqv_saida.write(concatenar_antes)
                            arqv_saida.write(concatenar_raiz)
                            arqv_saida.write(concatenar_no01_nivel01)
                            arqv_saida.write(concatenar_apos)


                    arqv_saida.write('\n')



        arqv_saida.close()


