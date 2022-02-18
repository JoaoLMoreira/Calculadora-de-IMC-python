

def printa_linha():
    print('#--------------------------------------------#')
 
def coletainformacoes():
    while True:
        try:
            peso = float(input('Digite seu peso : '))
            altura = float(input('Digite sua altura: ')) 
            retorna_imc(calculo_imc(peso, altura))
            break    
        except ValueError:
            print('voce deve digitar valores validos')
            
def mostramenu():
    printa_linha() 
    print('Calculadora de IMC')
    printa_linha() 
    print('1 - calcular IMC')
    print('2 - sair')
    printa_linha() 
    

def iniciaAplicacao(): 
    mostramenu()
    while True:
        try:
            menu  = int(input('Digite: '))
            if(menu == 1):
                printa_linha()
                coletainformacoes() 
                
            else:
                printa_linha() 
                print('Obrigado por usar o programa ! ') 
                printa_linha()
            break
        except ValueError:
            printa_linha()
            print('Escolha entre 1 ou 2 !')
            printa_linha() 
    
def retorna_imc(imc):
    if(imc < 18.5):
        print('voce esta abaixo do peso !') 
    elif(imc >18.5)and(imc <24.9):
        print('Voce esta com o peso normal !')  
    elif(imc >25)and(imc <29.9):
        print('Voce esta com  sobrepeso !') 
    elif(imc >30)and(imc <34.4):
        print('Voce esta com obsidade grau I !') 
    elif(imc >35)and(imc <39.9):
        print('Voce esta com obsidade grau II !')
    elif(imc >40):
        print('Voce esta com obsidade Morbida  !')  
    else:
        print('fora do if')    
    printa_linha() 

def calculo_imc(peso, altura):
    imc_calculado = "{:.1f}".format(peso / altura ** 2)
    printa_linha()
    print('seu imc é : ' + (imc_calculado))
    printa_linha()
    return float(imc_calculado)



iniciaAplicacao() 
input()
          
