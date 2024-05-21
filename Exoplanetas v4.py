from math import sqrt

# Constantes físicas
G = 6.67e-11
Pi = 3.14159265358979
Boltz = 5.67037442e-8
UA = 1.496e11
Massa_do_sol = 1.98892e30
Raio_do_sol = 6.9634e8
Luminosidade_do_sol = 3.827e26
Massa_da_terra = 5.972e24
Raio_da_terra = 6.3781e6
Massa_de_jupter = 1.898e27
Raio_de_jupter = 6.9911e7
Albedo = 0.367

def obter_dados():
    print('\nColoque os valores solicitados referentes a estrela e ao exoplaneta')
    print('Todos os valores solicitados serão apenas aqueles que podem ser utilizados de acordo com as regras do trabalho\n')
    
    print('Estrela')
    Massa_estrela = float(input('Massa da estrela em Massas solares:')) * Massa_do_sol
    Raio_da_estrela = float(input('Raio da estrela em Raios solares:')) * Raio_do_sol
    Temperatura_estrela = float(input('Temperatura da estrela em k:'))
    
    print('\nPlaneta')
    Profundidade_de_transito = float(input('Transit Depth[%] (Profundidade de transito):')) / 100
    Velocidade_radial = float(input('Radial Velocity Amplitude [m/s] (Velocidade radial):'))
    Periodo_orbital = float(input('Orbital Period [days] (Periodo orbital em dias):'))
    Excentricidade = float(input('Excentricidade:'))
    
    return (Massa_estrela, Raio_da_estrela, Temperatura_estrela, Profundidade_de_transito, 
            Velocidade_radial, Periodo_orbital, Excentricidade)

def calcular_parametros(Massa_estrela, Raio_da_estrela, Temperatura_estrela, 
                       Profundidade_de_transito, Velocidade_radial, 
                       Periodo_orbital, Excentricidade):
    
    # Convertendo período orbital para segundos
    Periodo_orbital_segundos = Periodo_orbital * 86400
    
    # Calculando o raio orbital
    Raio_orbital = ((G * Massa_estrela * (Periodo_orbital_segundos ** 2)) / (4 * (Pi ** 2))) ** (1/3)
    
    # Calculando massa do exoplaneta
    Massa_do_exoplaneta = (Velocidade_radial * sqrt(Raio_orbital * (1 - Excentricidade ** 2))) / (G ** (1/3) * (Massa_estrela ** (2/3)))
    
    # Calculando raio do exoplaneta
    Raio_do_exoplaneta = sqrt(Profundidade_de_transito) * Raio_da_estrela
    
    # Calculando probabilidade de transito
    Probabilidade_de_transito = (Raio_da_estrela + Raio_do_exoplaneta) / Raio_orbital
    
    # Calculando tempo de transito
    Tempo_de_transito = (Raio_da_estrela * sqrt((1 + Raio_do_exoplaneta / Raio_da_estrela) ** 2 - Excentricidade ** 2) * Periodo_orbital_segundos) / (Pi * Raio_orbital)
    
    # Calculando luminosidade da estrela
    Luminosidade_da_estrela = Boltz * 4 * Pi * (Raio_da_estrela ** 2) * (Temperatura_estrela ** 4)
    
    # Calculando temperatura de equilibrio
    Temperatura_de_equilibrio = Temperatura_estrela * sqrt(Raio_da_estrela / (2 * Raio_orbital)) * (1 - Albedo) ** 0.25
    
    # Calculando zonas habitáveis
    Zona_habitavel_interna = 0.95 * sqrt(Luminosidade_da_estrela / Luminosidade_do_sol)
    Zona_habitavel_central = sqrt(Luminosidade_da_estrela / Luminosidade_do_sol)
    Zona_habitavel_externa = 1.37 * sqrt(Luminosidade_da_estrela / Luminosidade_do_sol)
    
    # Calculando insolação do exoplaneta
    Insolação_do_exoplaneta = (Luminosidade_da_estrela / Luminosidade_do_sol) * (UA ** 2 / Raio_orbital ** 2)
    
    # Calculando densidade do exoplaneta
    Densidade_do_exoplaneta = Massa_do_exoplaneta / ((4 / 3) * Pi * (Raio_do_exoplaneta ** 3))
    
    # Calculando baricentro
    Baricentro = (Raio_orbital * Massa_do_exoplaneta) / (Massa_estrela + Massa_do_exoplaneta)
    
    return (Raio_orbital, Massa_do_exoplaneta, Raio_do_exoplaneta, Probabilidade_de_transito, 
            Tempo_de_transito, Luminosidade_da_estrela, Temperatura_de_equilibrio, 
            Zona_habitavel_interna, Zona_habitavel_central, Zona_habitavel_externa, 
            Insolação_do_exoplaneta, Densidade_do_exoplaneta, Baricentro)

def exibir_resultados(parametros):
    (Raio_orbital, Massa_do_exoplaneta, Raio_do_exoplaneta, Probabilidade_de_transito, 
     Tempo_de_transito, Luminosidade_da_estrela, Temperatura_de_equilibrio, 
     Zona_habitavel_interna, Zona_habitavel_central, Zona_habitavel_externa, 
     Insolação_do_exoplaneta, Densidade_do_exoplaneta, Baricentro) = parametros
    
    print('\nResultados:')
    print(f'Semi eixo maior do planeta via lei de kepler: {Raio_orbital:.10e} m')
    print(f'Semi eixo maior do planeta via lei de kepler: {Raio_orbital / UA:.10e} UA')
    print(f'\nMassa do exoplaneta: {Massa_do_exoplaneta:.10e} Kg')
    print(f'Massa em função de jupter: {Massa_do_exoplaneta / Massa_de_jupter}')
    print(f'Massa em função da terra: {Massa_do_exoplaneta / Massa_da_terra}')
    print(f'\nRaio do exoplaneta: {Raio_do_exoplaneta:.10e} m')
    print(f'Raio em função de jupter: {Raio_do_exoplaneta / Raio_de_jupter}')
    print(f'Raio em função da terra: {Raio_do_exoplaneta / Raio_da_terra}')
    print(f'\nProbabilidade de transito do exoplaneta: {Probabilidade_de_transito}')
    print(f'Tempo de Transito: {Tempo_de_transito:.10e} S')
    print(f'Tempo de Transito em horas: {Tempo_de_transito / 3600} h')
    print(f'\nGrau de insolação em função da terra: {Insolação_do_exoplaneta}')
    print(f'Temperatura de equilibrio: {Temperatura_de_equilibrio} K')
    print(f'\nZona de habitabilidade:')
    print(f'Interna: {Zona_habitavel_interna} UA')
    print(f'Central: {Zona_habitavel_central} UA')
    print(f'Externa: {Zona_habitavel_externa} UA')
    print(f'\nDensidade do exoplaneta: {Densidade_do_exoplaneta:.10e} g/cm³')
    print(f'\nDistância do semi eixo maior do baricentro até o centro da estrela: {Baricentro:.10e} m')

# Execução do programa
dados = obter_dados()
parametros = calcular_parametros(*dados)
exibir_resultados(parametros)
