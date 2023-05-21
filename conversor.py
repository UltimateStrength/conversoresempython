def litro_para_mililitro(litros):
    return litros * 1000

def mililitro_para_litro(mililitros):
    return mililitros / 1000

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def quilograma_para_grama(quilogramas):
    return quilogramas * 1000

def grama_para_quilograma(gramas):
    return gramas / 1000

def segundos_para_minutos(segundos):
    return segundos / 60

def minutos_para_segundos(minutos):
    return minutos * 60

def quilometros_por_hora_para_metros_por_segundo(kmph):
    return kmph * 1000 / 3600

def metros_por_segundo_para_quilometros_por_hora(mps):
    return mps * 3600 / 1000

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_para_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

def metro_para_centimetro(metros):
    return metros * 100

def centimetro_para_metro(centimetros):
    return centimetros / 100

def quilometro_para_metro(quilometros):
    return quilometros * 1000

def metro_para_quilometro(metros):
    return metros / 1000

def metro_para_milimetro(metros):
    return metros * 1000

def milimetro_para_metro(milimetros):
    return milimetros / 1000

def quilometro_para_centimetro(quilometros):
    return quilometro_para_metro(quilometros) * 100

def centimetro_para_quilometro(centimetros):
    return centimetro_para_metro(centimetros) / 100

def quilometro_para_milimetro(quilometros):
    return quilometro_para_metro(quilometros) * 1000

def milimetro_para_quilometro(milimetros):
    return milimetro_para_metro(milimetros) / 1000

def centimetro_para_milimetro(centimetros):
    return centimetros * 10

def milimetro_para_centimetro(milimetros):
    return milimetros / 10

def quilograma_para_grama(quilogramas):
    return quilogramas * 1000

def grama_para_quilograma(gramas):
    return gramas / 1000

def tonelada_para_quilograma(toneladas):
    return toneladas * 1000

def quilograma_para_tonelada(quilogramas):
    return quilogramas / 1000

def quilograma_para_miligrama(quilogramas):
    return quilogramas * 1000000

def miligrama_para_quilograma(miligramas):
    return miligramas / 1000000

def tonelada_para_grama(toneladas):
    return tonelada_para_quilograma(toneladas) * 1000

def grama_para_tonelada(gramas):
    return grama_para_quilograma(gramas) / 1000

def tonelada_para_miligrama(toneladas):
    return tonelada_para_quilograma(toneladas) * 1000000

def miligrama_para_tonelada(miligramas):
    return miligrama_para_quilograma(miligramas) / 1000000

def grama_para_miligrama(gramas):
    return gramas * 1000

def miligrama_para_grama(miligramas):
    return miligramas / 1000

def segundos_para_minutos(segundos):
    return segundos / 60

def minutos_para_segundos(minutos):
    return minutos * 60

def minutos_para_horas(minutos):
    return minutos / 60

def horas_para_minutos(horas):
    return horas * 60

def horas_para_dias(horas):
    return horas / 24

def dias_para_horas(dias):
    return dias * 24

def dias_para_meses(dias):
    return dias / 30.436875  # Média de dias por mês

def meses_para_dias(meses):
    return meses * 30.436875  # Média de dias por mês

def meses_para_anos(meses):
    return meses / 12

def anos_para_meses(anos):
    return anos * 12

def anos_para_decadas(anos):
    return anos / 10

def decadas_para_anos(decadas):
    return decadas * 10

def anos_para_seculos(anos):
    return anos / 100

def seculos_para_anos(seculos):
    return seculos * 100

def horas_para_semanas(horas):
    return horas / 168  # Média de horas por semana

def semanas_para_horas(semanas):
    return semanas * 168  # Média de horas por semana

def horas_para_meses(horas):
    return horas / 730.001  # Média de horas por mês (considerando anos não bissextos)

def meses_para_horas(meses):
    return meses * 730.001  # Média de horas por mês (considerando anos não bissextos)

def horas_para_anos(horas):
    return horas / 8760  # Média de horas por ano

def anos_para_horas(anos):
    return anos * 8760  # Média de horas por ano

def semanas_para_meses(semanas):
    return semanas / 4.34812  # Média de semanas por mês (considerando anos não bissextos)

def meses_para_semanas(meses):
    return meses * 4.34812  # Média de semanas por mês (considerando anos não bissextos)

def semanas_para_anos(semanas):
    return semanas / 52.1775  # Média de semanas por ano (considerando anos não bissextos)

def anos_para_semanas(anos):
    return anos * 52.1775  # Média de semanas por ano (considerando anos não bissextos)

def meses_para_decadas(meses):
    return meses / 120  # Média de meses por década

def decadas_para_meses(decadas):
    return decadas * 120  # Média de meses por década

def meses_para_seculos(meses):
    return meses / 1200  # Média de meses por século

def seculos_para_meses(seculos):
    return seculos * 1200  # Média de meses por século

# Dicionário com as opções de conversão
opcoes_conversao = {
    'comprimento': {
        'metro para centimetro': metro_para_centimetro,
        'centimetro para metro': centimetro_para_metro,
        'quilometro para metro': quilometro_para_metro,
        'metro para quilometro': metro_para_quilometro,
        'metro para milimetro': metro_para_milimetro,
        'milimetro para metro': milimetro_para_metro,
        'quilometro para centimetro': quilometro_para_centimetro,
        'centimetro para quilometro': centimetro_para_quilometro,
        'quilometro para milimetro': quilometro_para_milimetro,
        'milimetro para quilometro': milimetro_para_quilometro,
        'centimetro para milimetro': centimetro_para_milimetro,
        'milimetro para centimetro': milimetro_para_centimetro
    },
    'volume': {
        'litro para mililitro': litro_para_mililitro,
        'mililitro para litro': mililitro_para_litro
    },
    'temperatura': {
        'celsius para fahrenheit': celsius_para_fahrenheit,
        'fahrenheit para celsius': fahrenheit_para_celsius,
        'celsius para kelvin': celsius_para_kelvin,
        'kelvin para celsius': kelvin_para_celsius,
        'fahrenheit para kelvin': fahrenheit_para_kelvin,
        'kelvin para fahrenheit': kelvin_para_fahrenheit
    },
    'massa': {
        'quilograma para grama': quilograma_para_grama,
        'grama para quilograma': grama_para_quilograma,
        'tonelada para quilograma': tonelada_para_quilograma,
        'quilograma para tonelada': quilograma_para_tonelada,
        'quilograma para miligrama': quilograma_para_miligrama,
        'miligrama para quilograma': miligrama_para_quilograma,
        'tonelada para grama': tonelada_para_grama,
        'grama para tonelada': grama_para_tonelada,
        'tonelada para miligrama': tonelada_para_miligrama,
        'miligrama para tonelada': miligrama_para_tonelada,
        'grama para miligrama': grama_para_miligrama,
        'miligrama para grama': miligrama_para_grama
    },
    'tempo': {
        'segundos para minutos': segundos_para_minutos,
        'minutos para segundos': minutos_para_segundos,
        'minutos para horas': minutos_para_horas,
        'horas para minutos': horas_para_minutos,
        'horas para dias': horas_para_dias,
        'dias para horas': dias_para_horas,
        'dias para meses': dias_para_meses,
        'meses para dias': meses_para_dias,
        'meses para anos': meses_para_anos,
        'anos para meses': anos_para_meses,
        'anos para decadas': anos_para_decadas,
        'decadas para anos': decadas_para_anos,
        'anos para seculos': anos_para_seculos,
        'seculos para anos': seculos_para_anos
        
    },
    'velocidade': {
        'quilometros por hora para metros por segundo': quilometros_por_hora_para_metros_por_segundo,
        'metros por segundo para quilometros por hora': metros_por_segundo_para_quilometros_por_hora
    }
}

# Exibir opções disponíveis
print("Tipos de conversão disponíveis:")
for tipo in opcoes_conversao:
    print(f"- {tipo}")

# Solicitar escolha do tipo de conversão
tipo_conversao = input("Escolha o tipo de conversão: ")

# Verificar se o tipo de conversão é válido
if tipo_conversao not in opcoes_conversao:
    print("Tipo de conversão inválido.")
    exit()

# Exibir opções de conversão para o tipo selecionado
print(f"Opções de conversão para {tipo_conversao}:")
for opcao in opcoes_conversao[tipo_conversao]:
    print(f"- {opcao}")

# Solicitar escolha da conversão
conversao = input("Escolha a conversão: ")

# Verificar se a conversão é válida
if conversao not in opcoes_conversao[tipo_conversao]:
    print("Conversão inválida.")
    exit()

# Solicitar valor para conversão
valor = float(input("Digite o valor a ser convertido: "))

# Executar a conversão
resultado = opcoes_conversao[tipo_conversao][conversao](valor)

# Exibir o resultado
print(f"Resultado: {resultado}")

opcoes_conversao['tempo'].update({
    'horas para semanas': horas_para_semanas,
    'semanas para horas': semanas_para_horas,
    'horas para meses': horas_para_meses,
    'meses para horas': meses_para_horas,
    'horas para anos': horas_para_anos,
    'anos para horas': anos_para_horas,
    'semanas para meses': semanas_para_meses,
    'meses para semanas': meses_para_semanas,
    'semanas para anos': semanas_para_anos,
    'anos para semanas': anos_para_semanas,
    'meses para décadas': meses_para_decadas,
    'décadas para meses': decadas_para_meses,
    'meses para séculos': meses_para_seculos,
    'séculos para meses': seculos_para_meses
})