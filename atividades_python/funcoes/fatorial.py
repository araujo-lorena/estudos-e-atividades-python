"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""

def fatorial(numero,show=False):
       
        calculo_fatorial = 1

        for x in range(numero,0,-1):

            if show:
                print(x,end="")
                if x > 1:
                    print(" x ",end="")
                else:
                    print(" = ",end="")

            calculo_fatorial *= x

        
        return calculo_fatorial
  
print(fatorial(5,show=True))
      
