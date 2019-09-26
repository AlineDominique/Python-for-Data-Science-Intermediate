## 1. Introduction ##

l = [1, 2, 3]
s = "string"
d = {"a": 1, "b": 2}

#No editor de código, nós definimos três tipos de variveis que já trabalhamos.Siga as instruções abaixo, na ordem.
    # 1. Use a função print() para mostra o tipo da lista l.
print(type(l))
    # 2. Use a função print() para mostra o tipo da string s.
print(type(s))
    # 3. Use a função print() para mostra o tipo do dicionário d.
print(type(d))

## 3. Defining a Class ##

# 1. Defina uma nova classe chamada NewList()
    #Use o pass no corpo da sua classe para evitar o erro SyntaxError

class NewList():
    pass

## 4. Instantiating a Class ##

# 1. Defina uma nova Classe chamada NewList;
    # Use a Classe NewList(DQ) quando definir a classe, então nós podemos checar a resposta da sua Classe;
    # Use a palavra chave pass desta forma sua classe vazia para terá o erro SytantaxError.
# 2. Crie uma instâcia da Classe NewList. E atribua o valor a varíavel de nome newlist_1.
# 3. Imprima o tipo da variavel newlist_1.

class NewList(DQ):
    pass

newlist_1 = NewList()
print(type(newlist_1))

## 5. Creating Methods ##

#1. Defina uma nova classe chamada NewList:
    # Usar NewList(DQ)quando definir a classe, então nós podemos checar a reposta da sua classe;
#2. Dentro da Classe, defina o metodo chamado first_method.
#3. Dentro do metodo, retorne a string "This is my first method".
#4. Crie uma instancia da classe NewList. E atribua o valor a variavel newlist.

class NewList(DQ):
    def first_method():
        return "This is my first method"

newlist = NewList()

## 6. Understanding 'self' ##

#1. Nós providenciamos a resposta da tela anterior no editor de código em forma de cometário. Para descometar é só selecionar as linhas e presionar os botões ctrl + / (PC) ou ⌘ + / (Mac).
#2. Modifique o método first_method adicionando self com argumento.
#3. Crie uma instancia da classe NewList. Atribua a variavel newlist o valor.
#4. Chame o método newlist.first_method().Atribua o valor a variavel result.

class NewList(DQ):
    def first_method(self):
        return "This is my first method"

newlist = NewList()
result = newlist.first_method()

## 7. Creating a Method That Accepts an Argument ##

#1. Defina uma nova classe chamada NewList()
    # Para conseguir checar a resposta da classe use a definição NewList(DQ).
#2. Dentro da classe, defina o método chamado return_list():
    #O método deve aceitar apenas um argumento input_list quando chamado.
    #Dentro do método, retornar input_list.
#3. Criar uma instancia da classe NewList, e atribuir o valor a variavel newlist.
#4. Chamar o metodo newlist.return_list() com o argumento [1,2,3].E atribuir o resultado a variavel result.

class NewList(DQ):
    def return_list(self, input_list):
        return input_list

newlist = NewList()
result = newlist.return_list([1, 2, 3])

## 8. Attributes and the Init Method ##

#1. Defina uma nova classe chamada NewList()
    # Para conseguir checar a resposta da classe use a definição NewList(DQ).
#2. Criar o método init que aceite apenas o argumento initial_state.
#3. Dentro do método init, atribua o initial_state ao atributo chamado data.
#4. Instancie o objeto da classe NewList, com a lista[1,2,3,4,5] como argumento. Atribua o objeto a variavel my_list.
# 5. Use a função print() para mostrar o atibuto data do my_list.

class NewList(DQ):
    def __init__(self, initial_state):
        self.data = initial_state

my_list = NewList([1, 2, 3, 4, 5])
print(my_list.data)

## 9. Creating an Append Method ##

# The NewList definition from the previous
# screen is copied here for your convenience

#1. A solução da tela anterior está comentada pois será usada neste exercício. Então apenas é só descomentar.
#2. Na classe NewList, adicione uma novo método chamado NewList.append()
    # O método irá requerer um argumento que será fornecido quando for chamado;
    # O método modificará o atributo NewList.data, acrescentando o argumento à lista;
    # o método não deverá retornar nenhum valor.
#3. Crie um objeto NewList com a lista [1, 2, 3, 4, 5]. Atribua o objeto a variavel my_list.
    # Use a função print() para mostrar o atributo my_list.data
#4. Use o NewList.append() método para inserir o 6 ao objeto my_list 
    # Use a função print() para mostrar o atributo my_list.data.
class NewList(DQ):
    """     A Python list with some extras!  """
    def __init__(self, initial_state):
        self.data = initial_state
        
    def append(self,new_item):
        self.data = self.data + [new_item]

my_list = NewList([1, 2, 3, 4, 5])
print(my_list.data)
my_list.append(6)
print(my_list.data)
        

## 10. Creating and Updating an Attribute ##

# The NewList definition from the previous
# screen is copied here for your convenience

#1. Fornecemos a solução da tela anterior como comentários no editor de código. Selecione todas essas linhas e pressione ctrl + / (PC) ou ⌘ + / (Mac) para remover o comentário dessas linhas, para que você possa fazer modificações.
#2. Adicione um método auxiliar chamado calc_length () à nossa classe NewList, que calcula o comprimento da lista armazenada no objeto e a armazena em um novo atributo NewList.length.
#3. Adicione o método auxiliar ao final dos métodos __init __ () e append ().
#4. Teste se o novo atributo funciona conforme o esperado:
    #Crie um novo objeto NewList contendo a lista [1, 1, 2, 3, 5] e atribua-o ao nome da variável fibonacci.
    #Use a função print () para exibir o atributo length do objeto fibonacci.
    #Acrescente o valor 8 a fibonacci
    #Use a função print () para exibir o atributo de comprimento atualizado do objeto fibonacci.



class NewList(DQ):
    """
    A Python list with some extras!
    """
    def __init__(self, initial_state):
        self.data = initial_state
        self.calc_length()
    
    def append(self, new_item):
        """
        Append `new_item` to the NewList
        """
        self.data = self.data + [new_item]
        self.calc_length()
    
    def calc_length(self):
        length = 0
        for item in self.data:
            length += 1
        self.length = length

fibonacci = NewList([1, 1, 2, 3, 5])
print(fibonacci.length)
fibonacci.append(8)
print(fibonacci.length)    