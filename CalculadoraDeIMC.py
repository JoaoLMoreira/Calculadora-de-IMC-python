

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
            print('Você deve digitar valores numericos')
            
def mostramenu():
    printa_linha() 
    print('Calculadora de IMC')
    printa_linha() 
    print('1 - Calcular IMC')
    print('2 - Sair')
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
        print('Este indice representa "Abaixo do peso" !') 
    elif(imc >18.5)and(imc <24.9):
        print('Este indice representa "Peso normal" !')  
    elif(imc >25)and(imc <29.9):
        print('Este indice representa "Sobrepeso" !') 
    elif(imc >30)and(imc <34.4):
        print('Este indice representa "Obesidade grau I" !') 
    elif(imc >35)and(imc <39.9):
        print('Este indice representa "Obesidade grau II" !')
    elif(imc >40):
        print('Este indice representa "Obesidade morbida" !')   
    printa_linha() 

def calculo_imc(peso, altura):
    imc_calculado = "{:.1f}".format(peso / altura ** 2)
    printa_linha()
    print('seu imc é : ' + (imc_calculado))
    printa_linha()
    return float(imc_calculado)



iniciaAplicacao() 
input()
          
