
import datetime
class ManipularLista():
    def __init__(self):
        self.vetor_grava_versao2 = []
        self.vetor_grava_versao1 = []
        self.z = ''
        self.y = ''


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
