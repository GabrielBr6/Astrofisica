from math import sqrt
G=6.67e-11
Pi=3.14159265358979
Boltz=5.67037442e-8
UA=1.496e11
Massa_do_sol=1.98892e30
Raio_do_sol=6.9634e8
Luminosidade_do_sol=3.827e26
Massa_da_terra=5.972e24
Raio_da_terra=6.3781e6
Massa_de_jupter=1.898e27
raio_de_jupter=6.9911e7
Albedo=0.367

print('')
print('Coloque os valores solicitados referentes a estrela e ao exoplaneta')
print('Todos os valores solicitados serão apenas aqueles que podem ser utilizados de acordo com as regras do trabalho')
print("Obs: Alguns valores dos resultados podem não ser muito precisos, já que os metodos/formulas utilizados são diferentes dos da NASA, então não se preocupe muito com a diferença nos valores se comaparada com as do Exo")
print('Estrela')
Massa_estrela=(float(input('Massa da estrela em Massas solares:'))*Massa_do_sol)
print('')
Raio_da_estrela=(float(input('Raio da estrela em Raios solares:'))*Raio_do_sol)
print('')
Temperatura_estrela=float(input('Temperatura da estrela em k:'))
print('')
print('Planeta')
Profundidade_de_transito=(float(input('Transit Depth[%] (Profundidade de transito):'))/(100))
print('')
Velocidade_radial=float(input('Radial Velocity Amplitude [m/s] (Velocidade radial):'))
print('')
Periodo_orbital=(float(input('Orbital Period [days] (Periodo orbital em dias):')))
print('')
Excentricidade=float(input('Excentricidade:'))
print('')
print('O Albedo sera utilizado 0.367(Mesmo da terra, de acordo com o pedido do trabalho):')
print('')
print('-'*30)
print("Massa da estrela(Kg):" "%.10e"%float(Massa_estrela))
print('-'*30)
print("Raio da estrela(m):" "%.10e"%float(Raio_da_estrela))
print('-'*30)
print("Temperatura da estrela(k):", float(Temperatura_estrela))
print('-'*30)
print("Profundidade de Transito:", float(Profundidade_de_transito))
print('-'*30)
print("Velocidade Radial(m/s):", float(Velocidade_radial))
print('-'*30)
print("Periodo orbital(s):" "%.10e"%float(Periodo_orbital*86400))
print('-'*30)
print("Excentricidade:", float(Excentricidade))
print('-'*30)

#Formulas para calcular parametros
Massa_do_exoplaneta=float(((Periodo_orbital/4380)**(1/3))*(Velocidade_radial/13)*Massa_de_jupter)
Raio_do_exoplaneta=float((10*Raio_da_estrela*sqrt(10490*Profundidade_de_transito)/1049))
Densidade_do_exoplaneta=float(((3*Massa_do_exoplaneta)/((4*Pi)*Raio_do_exoplaneta**3))/1000)
#Raio_do_exoplaneta=float(sqrt(Profundidade_de_transito)*Raio_do_sol)
Raio_orbital=float(((G*Massa_estrela*((Periodo_orbital*86400)**2))/(4*(Pi)**2))**(1/3))
Probabilidade_de_transito=float((Raio_da_estrela/(Raio_orbital*(1-Excentricidade**2))))
Tempo_de_transito=float(((sqrt(Raio_orbital*G*Massa_estrela))*(2*Raio_da_estrela))/(G*Massa_estrela))  #Valor em segundos, dividir por 3600 para horas
#Tempo_de_transito=13*((Massa_estrela/Massa_do_sol)**(-1/2))*((Raio_orbital/UA)**(1/2))*(Raio_da_estrela/Raio_do_sol) #Valor direto em horas
Temperatura_de_equilibrio=Temperatura_estrela*((1-Albedo)**(1/4))*((Raio_da_estrela/(2*Raio_orbital))**(1/2))
Luminosidade_da_estrela=float(4*Pi*(Raio_da_estrela**2)*Boltz*(Temperatura_estrela**4))
Zona_habitavel_interna=float(0.75*sqrt(Luminosidade_da_estrela/Luminosidade_do_sol))
Zona_habitavel_central=float(1*sqrt(Luminosidade_da_estrela/Luminosidade_do_sol))
Zona_habitavel_externa=float(1.77*sqrt(Luminosidade_da_estrela/Luminosidade_do_sol))
Insolação_do_exoplaneta=float((Luminosidade_da_estrela/Luminosidade_do_sol)*(UA**2/(Raio_orbital**2)))



#Exibição dos resultados
print('')
print('Resultados:')
print('Semi eixo maior do planeta via lei de kepler:' "%.10e"%float(Raio_orbital),'m')
print('Semi eixo maior do planeta via lei de kepler:', float(Raio_orbital/UA),'UA')
print('-'*30)
print('Determinacao da massa do planeta em funcao da massa de Jupiter e massa terretre:')
print('Massa do exoplaneta:' "%.10e"%float(Massa_do_exoplaneta), "Kg")
print('Massa em função de jupter:', Massa_do_exoplaneta/Massa_de_jupter)
print('Massa em função da terra:', Massa_do_exoplaneta/Massa_da_terra)
print('-'*30)
print('Determinacao do raio do planeta em funcao do raio de Jupiter e Terrestre:')
print('Raio do exoplaneta:' "%.10e"%float(Raio_do_exoplaneta), 'm')
print('Raio em função de jupter:', Raio_do_exoplaneta/raio_de_jupter)
print('Raio em função da terra:', Raio_do_exoplaneta/Raio_da_terra)
print('-'*30)
print("Probabilidade de transito do exoplaneta:", Probabilidade_de_transito)
print('-'*30)
print("Tempo de Transito:" "%.10e"%float(Tempo_de_transito), 'S')
print("Tempo de Transito em horas:", Tempo_de_transito/3600, 'h')
print('-'*30)
print('Grau de insolação em função da terra:', Insolação_do_exoplaneta)
print('-'*30)
print('Temperatura de equilibrio:', Temperatura_de_equilibrio, "K")
print('-'*30)
print("Determinacao da zona de habitabilidade da estrela, interna, central e externa")
print('Interna:', Zona_habitavel_interna, "UA")
print('Central:', Zona_habitavel_central, "UA")
print('Externa:', Zona_habitavel_externa, "UA")
print('-'*30)
print('Densidade do exoplaneta:', Densidade_do_exoplaneta, 'g/cm³')
print('-'*30)