# Executed on:
# Python 3.12.0
#
# PyAutoGUI 0.9.54
# |   opencv-python 4.8.1.78
# |   |  numpy 1.26.2

# Template by @CodingWithNoDirection on github.com/CodingWithNoDirection/dofus-afk-farming-template
# Original template code used:
#
#    imageOffset = 25
#
#    def checkImage():
#    try:
#       pos = pg.locateOnScreen("./image1.jpg", confidence=0.8)
#       pg.moveTo(pos[0]+imageOffset,pos[1]+imageOffset)
#       pg.click()
#       time.sleep(1)
#    except:
#       print("image loaded but couldn't find it in Dofus")
#
#    checkImage()



import pyautogui as pg
import time
import os

### Pesquisa 5 - IP
ips = [] # Determina quantas vezes será executado.

root = os.getcwd() # Local onde o arquivo foi executado (precisa estar na mesma pasta das imagens).

# Apenas testa se a imagem apareceu na tela
def waitImg(img, xAdd=0, yAdd=0, conf=0.8):
    try:
        print(f"'waitImg': Procurando {img}")
        pos = pg.locateCenterOnScreen(img, confidence=conf)
        pg.moveTo(pos[0]+int(xAdd), pos[1]+int(yAdd)) # Usado apenas para chamar a exception caso necessário.
        print(f"'waitImg': Encontrou {img}")
        time.sleep(0.1)
        return True
    except:
        print(f"'waitImg': Não foi possivel clicar/encontrar em {img}")
        time.sleep(2) # Evita a reprocura instantânea
        return False # Retorna False caso não encontre {img}

# Clica na imagem após checar novamente usa posição e retorna True.
def checkImage(img, xAdd=0, yAdd=0, conf=0.8): 
    try:
        print(f"'checkImage': Procurando {img}")
        pos = pg.locateCenterOnScreen(img, confidence=conf)
        pg.moveTo(pos[0]+int(xAdd), pos[1]+int(yAdd))
        pg.click()
        print(f"'checkImage': Encontrou {img}")
        time.sleep(1) # Concede tempo para o PyAutoGui clicar e a página responder ao click.
        return True
    except:
        print(f"'checkImage': Não foi possivel clicar/encontrar em {img}")
        time.sleep(1) # Evita a reprocura instantânea
        return False # Retorna False caso não encontre {img}

# waitImg("enderecoIP.png") # teste


for ip in ips:

    # Seleciona o campo Endereço IP
    while (waitImg("enderecoIP.png") == False): # Repete até encontrar
        print("\n")
    else:
        checkImage("enderecoIP.png")
        print("Concluido!")

    # Seleciona o conteúdo do campo e digita o IP
    pg.hotkey("ctrl", "a")
    pg.write(f"{ip}")

    # Manda Imprimir o relatório
    while (waitImg("imprimir_btn.png") == False): # Repete até encontrar
        print("\n")
    else:
        checkImage("imprimir_btn.png")
        print("Concluido!")

    # Espera Registro = 1 e clica em salvar ou Registro 0 e adiciona IP em naoEncontrou.txt (espera alcançar um dos fluxos possíveis)
    while ((waitImg("totalDeRegistros1.png") == False) and (waitImg("totalDeRegistros0.png") == False)): # Repete até encontrar (retorna True quando encontra)
        print("...\n")
    else:
        print("----------------------------------------\n")
        if ((waitImg("totalDeRegistros0.png")) == True): # Fluxo quando não houver resultado (registra em ./naoEncontrou.txt os nomes dos relatorios vazios e/ou não encontrados)
            out_file = open(f"{root}/naoEncontrou.txt", "a")
            out_file.write(f"{ip}\n")
            out_file.close()
            print(f"PDF Vazio em {ip}.pdf")

        elif (waitImg("totalDeRegistros1.png") == True): # Fluxo de quando houver resultado
            while (waitImg("salvar_btn.png") == False): # Repete até encontrar
                print("\n")
            else:
                checkImage("salvar_btn.png")
            print("Concluido!")


            # Clica na pasta da Barra de Endereço e escreve o local do arquivo, enter, enter
            while (waitImg("barraDeEnderecoSalvar-btn-54_11.png") == False): # Repete até encontrar
                print("\n")
            else:
                # Digita o IP.pdf
                pg.write(f"{ip}.pdf")

            checkImage("barraDeEnderecoSalvar-btn-54_11.png", 18)
            pg.write(f"{root}")
            pg.press("enter")
            time.sleep(1)
            pg.press("enter")
            print("Baixou!")
        
        else: print("IF e ELIF não encontrao nada")
    time.sleep(1)
    # Clica em relatório para fechar a janela de Downloads
    while (waitImg("relatorio_title.png") == False): # Repete até encontrar
        print("\n")
    else:
        checkImage("relatorio_title.png")
        print("Concluido!")

    # Fecha janela que pesquisa Relatório
    while (waitImg("fechar_btn.png") == False): # Repete até encontrar
        print("\n")
    else:
        checkImage("fechar_btn.png")
        print("Concluido!")


    print("Concluido!")


input() # Impede de fechar o console para poder visuaizar o log.

