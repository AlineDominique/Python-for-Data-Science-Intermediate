## 1. Introducing Data Cleaning ##

# Read the text on the left, and then scroll to the bottom
# to find the instructions for the coding exercise

# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`

num_rows=len(moma)
print(num_rows)


## 2. Reading our MoMA Data Set ##

# import the reader function from the csv module
from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('children.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
children = list(read_file)

# remove the first row of the data, which
# contains the column names
children = children[1:]

# Write your code here
opened_file = open('artworks.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

## 3. Replacing Substrings with the replace Method ##

age1 = "I am thirty-one years old"
age2 = age1.replace("thirty-one","thirty-two")


## 4. Cleaning the Nationality and Gender Columns ##

# Variables you create in previous screens
# are available to you, so you don't need
# to read the CSV again

for row in moma:
    nationality = row[2]
    gender = row[5]
    nationality = nationality.replace("(","")
    nationality = nationality.replace(")","")
    gender = gender.replace("(","")
    gender = gender.replace(")","")
    row[2] = nationality
    row[5] = gender
    

## 5. String Capitalization ##

for row in moma:
    gender = row[5]
    nationality = row[2]

    # converte o gênero a primeira letra da palavra para Uppercase
    gender = gender.title()
    nationality = nationality.title()

    #Se não haver gênero na coluna defina uma valor para coluna
    if not gender:
        gender = "Gender Unknown/Other"
    row[5] = gender
    if not nationality:
        nationality = "Nationality Unknown"
    row[2] = nationality

## 6. Errors During Data Cleaning ##

def clean_and_convert(date):
    #checar que nós não tenho uma string vazia 
    if date != "":
        #mover o resto da função para dentro 
        #do if
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

#o Loop percorrer a cada linha do dataset pega o valor da coluna 
# de nascimento e morte faz a limpeza e altera o valor para int
for row in moma:
    birth_date = row[3]
    death_date = row[4]
    
    new_birth = clean_and_convert(birth_date)
    new_death = clean_and_convert(death_date)
   
    row[3] = new_birth
    row[4] = new_death

## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

#Esta função percorre um lista para limpar os dados que possui
#o acumulo de carateres inuteis, o que atrapalha analise sem ruído dos dados
def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

#Criei uma nova lista para adcionar os dados que serão limpos dentro do for
stripped_test_data = []
for i in test_data:
    date = strip_characters(i)
    stripped_test_data.append(date)

## 8. Parsing Numbers from Complex Strings, Part Two ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

# Esta função verifica se a coluna data do dataset possui mais de um valor de data, caso haja ele dividi o valor, transformar o valor em int e faz uma média dos valores. Caso o contrario ele apenas transformar o valor em int.
def process_date(date):
    if "-" in date:
        split_date = date.split("-")
        date_one = int(split_date[0])
        date_two = int(split_date[1])
        date = round((date_one+date_two)/2)
        
    else:
        date = int(date)
    
    return date

#Aqui o código esta utilizando a função de process_date
processed_test_data = []
for d in stripped_test_data:
    date = process_date(d)
    processed_test_data.append(date)

for row in moma:
    date = row[6]
    date = strip_characters(date)
    row[6] = process_date(date)
   
            
            