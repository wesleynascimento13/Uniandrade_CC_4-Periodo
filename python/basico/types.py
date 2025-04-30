class A:
    pass

class B:
    pass

class C(A, B):
    pass

# Type annotations
idade: int = 32
salario: float = 35000.50
nome: str = "Julius"
casado: bool = True

dados: dict = {"nome": nome, "salario": salario, "idade": idade}
array: list = [2.5, "ju", 25, 25, 25]
tupla: tuple = (2.5, 25, 25, 25)
unico: set = {2.5, "ju", 25, 25, 25}

# print(unico)
print(nome.upper())  # método builtin
print(vars())        # imprime class com dict
# help(C)            # ajuda ver internamente

nome: str = "Ana Paula"
eh_casado: bool = True
pessoa: A = A()      # tipo personalizado
A.cargo = "diretor"

# print(A.__dict__)  # armazena valores da class
