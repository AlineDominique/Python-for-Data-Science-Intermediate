## 1. Introduction ##

from csv import reader
#1. Use a função open() para abrir o arquivo potus_visitors_2015.csv
#2. Use a função reader para ler o arquivo aberto.
#3. Use a função lista para converter o arquivo lido em uma lista de listas: 
    # Atribua a lista a variavel potus
    # Remove a primeira linha do dataset, o qual contêm o nome da colunas.
    
opened_file = open('potus_visitors_2015.csv')
read_file = reader(opened_file)
potus = list(read_file)
potus = potus[1:]

## 3. The Datetime Module ##

# 1. Importe o módulo datetime com o nome dt.
import datetime as dt

## 4. The Datetime Class ##

# 1. Importe o módulo datetime com o nome dt.
import datetime as dt
# 2. Instancie o datetime do objeto que represente meia noite de 16 de junho, 1911.E atribua o objeto a variavel ibm_founded.
ibm_founded = dt.datetime(1911,6,16)
# 3. Instancie o datetime do objeto que represente 8:17p.m de 20 de julho, 1969. Atribua o objeto a variavel man_on_moon
man_on_moon= dt.datetime(1969,7,20,20,17)

## 5. Using Strptime to Parse Strings as Dates ##

# The `potus` list of lists is available from
# the earlier screen where we created it
# 1. Criar uma variavel string date_format com especificações da coluna appt_start_date: 
    # O formato da coluna appt_start_date é {mês}/{dia}/{ dois digitos do ano} {hora 24hr time}:{minutos}
    #  Substitua cada valor dentro das chaves com strings com strftime apropriado da tabela acima.
# 2. Percorra cada linha do potus:
    # Atribua coluna appt_start_date, o index 2, a uma variavel
    # Use o datetime.strptime() para converter a variavel de string para datetime objeto, use o date_format para criando anteriomente.
    # Atribua o datetime objeto ao index 2 da linhas.

date_format = "%m/%d/%y %H:%M"
for row in potus:
    start_date = row[2]
    start_date = dt.datetime.strptime(start_date,date_format)
    row[2] = start_date

## 6. Using Strftime to format dates ##

# 1. Inicialize um dicionário vazio com o nome visitors_per_month.
# 2. Percorra as linhas da lista potus. A cada iiteração:
    # Atribua o datetime objeto da coluna appt_start_date (index 2) a uma variavel.
    # Chame o metodo datetime.strftime()do objeto appt_start_date crie uma string no seguinte formato "January, 1901".
        # Para o mês use no código o %B;
        # Para 4 digitos do ano use o %Y.
    # Se a sequência não for uma chave em visitors_per_month, adicione-a como uma chave com o valor 1.
    # Caso contrário, adicione 1 ao valor existente para essa chave.

visitors_per_month = {}

for row in potus:
    month_dt = row[2]
    month_str = month_dt.strftime("%B, %Y")
    if month_str not in visitors_per_month:
        visitors_per_month[month_str] = 1
    else:
        visitors_per_month[month_str] += 1

## 7. The Time Class ##

# 1. Instancie uma lista appt_times vazia.
# 2. Percorra as linhas da lista do potus. A cada iteração:
    # Atribua o objeto do datetime(index 2) em uma variavel;
    # Criar objeto do time do datetime objeto;
    # Adicione o objeto time na lista appt_times

appt_times = []
for row in potus:
    appt_dt = row[2]
    appt_t = appt_dt.time()
    appt_times.append(appt_t)

## 8. Comparing time objects ##

# A lista do appt_times disponivel na tela anterior na tela.
# 1. Atribua o horário do compromisso mais antigo da lista appt_times à variável min_time.
# 2. Atribua o horário do compromisso mais recente da lista appt_times à variável max_time.

min_time = min(appt_times)
max_time = max(appt_times)

## 9. Calculations with Dates and Times ##

dt_1 = dt.datetime(1981, 1, 31)
dt_2 = dt.datetime(1984, 6, 28)
dt_3 = dt.datetime(2016, 5, 24)
dt_4 = dt.datetime(2001, 1, 1, 8, 24, 13)

#1. Calcule o tempo entre dt_2 e dt_1 e atribua o resultado na variavel answer_1.
#2. Addicione 56 dias para dt_3 e atribua o resultado na variavel answer_2.
#3. Subtrai 3600 secundos para dt_4 e atribua o resultado a variavel answer_3.

answer_1 = dt_2 - dt_1
answer_2 = dt_3 + dt.timedelta(days=56)
answer_3 = dt_4 - dt.timedelta(seconds=3600)

## 10. Summarizing Appointment Lengths ##

for row in potus:
    end_date = row[3]
    end_date = dt.datetime.strptime(end_date, "%m/%d/%y %H:%M")
    row[3] = end_date
#Fornecemos código que converte appt_end_date em objetos de data e hora.
#1. Instancie um dicionário vazio para a nossa tabela de frequências, appt_lengths.
#2. Faça um loop sobre cada linha em potus e:
    # Atribua os valores para appt_start_date (índice 2) e appt_end_date (índice 3) às variáveis.
    # Subtraia appt_start_date de appt_end_date para calcular a duração do compromisso, a duração.
    # Se length não for uma chave em appt_lengths, adicione-a como uma chave com o valor 1.
    # Se length for uma chave em appt_lengths, adicione 1 ao valor existente dessa chave.
#3. Calcule a chave mínima em appt_lengths e atribua o resultado a min_length.
#4. Calcule a chave máxima em appt_lengths e atribua o resultado a max_length.
appt_lengths = {}
for row in potus:
    start_date = row[2]
    end_date = row[3]
    length = end_date - start_date
    if length not in appt_lengths:
        appt_lengths[length] = 1
    else:
        appt_lengths[length] += 1

min_length = min(appt_lengths)
max_length = max(appt_lengths)