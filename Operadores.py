def LeiaInt(msg:str):
    while True:
        valor = input(msg)
        try:
            int(valor)
        except (TypeError, ValueError):
            print('Digite apenas números')
        else:
            return int(valor)

def Menu(lista:list, title:str, maxn:int, minn:int, return_name=False):
    while True:
        print(f'{"-" * 5} {title} {"-" * 5}')
        for ind, ele in enumerate(lista):
            print(f'[ {ind + 1} ] - {ele}')
        print(f'{"-" * 6}{"-" * len(title)}{"-" *6}')
        num = LeiaInt('Qual sua opção: ')
        if num > maxn or num < minn:
            print(f'Digite um valor de {minn} a {maxn}')
        else:
            if return_name:
                return lista[num - 1]
            else:
                return num

class Verificar:
    def Verificar_Positivo(self, numero:int, us=True):
        if numero < 0:
            if not us:
                return False
            print(f'O número [ {numero} ] é Negativo')
        else:
            if not us:
                return True
            print(f'O número [ {numero} ] é Positivo')

    def Verificar_Par(self, numero:int, us=True):
        if numero % 2 == 0:
            if not us:
                return 'Par'
            print(f'O número [ {numero} ] é Par')
        else:
            if not us:
                return 'Impar'
            print(f'O número [ {numero} ] é Impar')
    
    def Tabuada(self, numero:int):
        qtd = LeiaInt('Quantidade de multiplicações: ')
        for c in range(qtd+1):
            if c == 0:
                continue
            print(f'{numero} x {c} = {numero * c}')

    def Verificar_Primo(self, numero:int):
        cont = 0
        for c in range(1, numero+1):
            if numero % c == 0:
                cont += 1
        if cont == 2:
            print(f'O número [ {numero} ] é Primo')
        else:
            print(f'O número [ {numero} ] Não é Primo')

class Calculadora:
    def __init__(self):
        list_calc = ['Adição', 'Subtração', 'Divisão', 'Multiplicação', 'Voltar']
        while True:
            operator_math = Menu(list_calc, 'Escolha a operação:', 5, 0, False)
            if operator_math == 5:
                break
            number_one = LeiaInt(f'Qual o Primeiro número para fazer a {list_calc[operator_math - 1]}:')
            number_two = LeiaInt(f'Qual o Segundo número para fazer a {list_calc[operator_math - 1]}:')
            self.calcular(operator_math, number_one, number_two)

    def calcular(self, esc, num1:int, num2:int) ->int:
        list_function = (self.Adicao(num1, num2), self.Subtracao(num1, num2), self.Divisao(num1, num2), self.multiplicacao(num1, num2))
        print(f'O resultado é {list_function[esc-1]}')
        return

    def Adicao(self, num_one:int, num_two:int) -> int:
        return num_one + num_two

    def Subtracao(self, num_one:int, num_two:int) -> int:
        return num_one - num_two

    def Divisao(self, num_one:int, num_two:int) -> int:
        return num_one / num_two

    def multiplicacao(self, num_one:int, num_two:int) -> int:
        return num_one * num_two


class Beemo(Verificar, Calculadora):
    def __init__(self):
        print("""
                                                        ██████╗ ███████╗███████╗███╗   ███╗ ██████╗ 
                                                        ██╔══██╗██╔════╝██╔════╝████╗ ████║██╔═══██╗
                                                        ██████╔╝█████╗  █████╗  ██╔████╔██║██║   ██║
                                                        ██╔══██╗██╔══╝  ██╔══╝  ██║╚██╔╝██║██║   ██║
                                                        ██████╔╝███████╗███████╗██║ ╚═╝ ██║╚██████╔╝
                                                        ╚═════╝ ╚══════╝╚══════╝╚═╝     ╚═╝ ╚═════╝
            """)
        while True:
            escolha_init = Menu(['Verificar números', 'Calcular números'], 'Categorias', 2, 0, True)
            if escolha_init == 'Verificar números':
                while True:
                    escolha = Menu(['Número primo', 'Números negativos/positívos', 'Números pares/ímpares', 'Tabuada de um número', 'Voltar'], 'Verificar Numero', 5, 0, True)
                    if escolha == 'Voltar':
                        break
                    number = LeiaInt('Digite o número para a verificação: ')
                    if escolha == 'Número primo':
                        self.Verificar_Primo(number)
                    elif escolha == 'Números negativos/positívos':
                        self.Verificar_Positivo(number)
                    elif escolha == 'Números pares/ímpares':
                        self.Verificar_Par(number)
                    elif escolha == 'Tabuada de um número':
                        self.Tabuada(number)
            if escolha_init == 'Calcular números':
                Calculadora.__init__(self)

if __name__ == "__main__":
    beemo = Beemo()