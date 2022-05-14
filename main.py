import random
import ctypes
from iOarvRB import Arquivo

if __name__ == "__main__":

    x = True
    y = True
    while(x == True) and (y==True):
        print(x)
        print(y)
        x = False

    nova = Arquivo('entrada')
    nova.lerArquivo('entrada.txt')

   # nova.testeEscrita('saida.txt')

       # Arquivo.salvar_erro(" ",err)

       # Arquivo.smsdeErro('teste',True)

   # nova.inserirNovoNo(70)

    #nova.mostrar_arvore()
    #nova.imprimir_sucessor()

   # nova.deletarNo(44)
   # nova.most if(self.controle_versao == 100):rar_arvore()

