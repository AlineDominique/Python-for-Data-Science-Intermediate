## 1. Reading our MoMA Data Set ##

from csv import reader

# Ler o arquivo `artworks_clean.csv` 
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convertendo os valores a data de nascimento
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convertendo os calores da data de morte 
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Convertendo os valores da coluna data
for row in moma:
    date = row[6]
    if date != "":
        date = int(date)
    row[6] = date



## 2. Calculating Artist Ages ##

#1. Crie uma lista vazia com o nome ages(idades)para armazenar as idades dos artistas.
#2. Usar o loop para percorrer as linhas do data moma
# 3. A cada interação,atribuir o ano da arte do artista a variavel date e o ano de nascimento do artista a variavel birth
    #Se o birth é int, calcule a idade do artista no momento da criação da sua obra e atribua-a à variável age.
    #Se a variavel não for do tipo int, atribua-a 0 a variavel age.
#Adicione a variavel age a lista ages.

ages = []
for row in moma:
    birth = row[3]
    date = row[6]
    if type(birth) == int:
        age = date - birth
    else:
        age = 0
    ages.append(age)
    
#4. Crie uma lista vazia com o nome final_ages, para armazenar as idades finais do dado.
#5. Use o loop para percorrer as idades na lista ages.
    #Se a idade for maior que 20, atribua o valor a variavel final_age.
    #Se a idade for menor que 20, atribua o valor Unknown(Desconhecido) a variavel final_age.
    # Adicione variavel final_age a lista final_ages.
final_ages = []
for age in ages:
    if age > 20:
        final_age = age
    else:
        final_age = "Unknown"
    final_ages.append(final_age)
        

## 3. Converting Ages to Decades ##

# A variável final_ages está disponível na tela anterior
# 1. Crie uma lista vazia com o nome decades para armanezar a decada do artista.
# 2. Percorra os valores da lista final_ages. E cada iteração:
    # Se a idade for Unknown(Desconhecido), atribua o valor a variavel decade
    # Se a idade não for Unknown(Desconhecido):
        # Converta o valor para string e atribua a variavel decade;
        # Use o slicing para remover o caratere final decade;
        # Use o operador de + para adicionar a substring "0" no final da string decade.
# 3. Adicione decade na lista decades.

decades = []
for age in final_ages:
    if age == "Unknown":
        decade = age
    else:
        decade = str(age)
        decade = decade[:-1]+"0s"
    decades.append(decade)
        

## 4. Summarizing the Decade Data ##

# A variável decades está disponível na tela anterior.
# 1. Crie um dicionário vázio, com o nome decade_frequency
# 2. Percorra cada valor da lista decades. E cada iteração:
    # Se o valor não for uma chave do dicionário decade_frequency, adicione como chave com o valor 1.
    # Se o valor for uma chave do dicionário decade_frequency, adicione +1 ao valor existente.
    
decade_frequency = {}
for d in decades:
    if d not in decade_frequency:
        decade_frequency[d] = 1
    else:
        decade_frequency[d]+=1
        

## 5. Inserting Variables Into Strings ##

# Nós providenciamos o nome e ano de nascimento do artista nas variavéis artist e birth_year.
# 1. Crie um template string e insira as variaveis artist e birth_year na string, usando o formato providenciado acima. Você escolhe qual das 3 técnicas que aprendeu como especificar as variaveis preenche qual espaço.
#2. Use o str.format() para inserir as 2 variavais no seu template string, atribua o resultado a variável.
#3. Use a função print() para imprimir a variable.

artist = "Pablo Picasso"
birth_year = 1881

template = "{name}'s birth year is {year}"
output = template.format(name=artist,year=birth_year)
print(output)

## 6. Creating an Artist Frequency Table ##

# 1. Crie um dicionário vázio com, o nome artist_freq.
# 2. Percorra cada valor da base de dados moma. E a cada iteração: 
    # Atribua o nome do artista a variável artist;
    # Se o artist não for uma chave do dicionário artist_freq, adicione como chave com o valor 1.
    # Se o artist for uma chave do dicionário artist_freq, adicine +1 ao valor da chave.

artist_freq = {}
for row in moma:
    artist = row[1]
    if artist not in artist_freq:
        artist_freq[artist] = 1
    else:
        artist_freq[artist]+=1

## 7. Creating an Artist Summary Function ##

# 1. Crie a função artist_summary(),que aceita apenas o argumento nome do artista.
# 2. A função deve imprimir um sumário com os nomes dos artistas, usando os seguintes passos abaixo:
    # Recupere o número de obras de cada artista do dicionário artist_freq, e atribua a uma variável.
    # Crie uma variável strig com nome de template e use as chaves ({})para inserir o nome e variaveis na string, usando o método format.
    # Use método str.format() para inserir o nome do artista e o numero de obras no template.
    # Use a função print() para imprimir a string final.
# 3. Use sua função para imprimir o sumário do artista Henri Matisse.

def artist_summary(artist):
    num_artworks = artist_freq[artist]
    template = "There are {number} artworks by {name} in the data set"
    output = template.format(name=artist, number = num_artworks)
    print(output)

artist_summary("Henri Matisse")
        

## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

# 1. Crie um template de String que insira nome do país e a população como mostrado no exemplo acima.
    # O população do país deve ter a precisão de apenas 2 numeros e usar a vírgula como separador.
# 2. Use o loop(for) para percorrer a lista pop_millions e cada iteração:
    # Atribua o nome do país e a população a duas variáveis.
    # Use str.format() para inserir as duas variaveis ao template.
    # Use a função print para mostrar o resultado do str.format().

template = "The population of {city} is {population:,.2f} million"
for country in pop_millions:
    name = country[0]
    pop = country[1]
    output = template.format(city=name,population=pop)
    print(output)

## 9. Challenge: Summarizing Artwork Gender Data ##

#1. Crie a tabela de frequência dos valores de Gender
#2. Percorrar os pares key-value do dicionário. E Imprima um sumário com cada pair usando format

gender_freq = {}

for row in moma:
    gender = row[5]
    if gender not in gender_freq:
        gender_freq[gender] = 1
    else:
        gender_freq[gender] += 1

for gender,num in gender_freq.items():
    template = "There are {n:,} artworks by {g} artists"
    print(template.format(g=gender, n=num))