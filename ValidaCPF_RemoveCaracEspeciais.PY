#   FUNÇÃO QUE VALIDA O CPF  
def valida_cpf(listaA):


    """
    Valida se o CPF digita é valido ou não.

    parammetros: Numeros do CPF em lista de inteiros.
    Retorno: Informa se o CPF é valido ou não.
    """
    resultadosListaUm = []
    resultadosListaDois = []
    calc = 10
    calcDois = 11

    for i in range(len(listaA)):
        if i <= 8:
            resultado = listaA[i] * calc
            resultadosListaUm.append(resultado)
            calc = calc - 1

    somaResultadosListaUm = sum(resultadosListaUm)
    resto_div_onze = somaResultadosListaUm % 11

    if resto_div_onze < 2:
        digitoUm = 0
    else:
        digitoUm = 11 - resto_div_onze

    for i in range(len(listaA)):
        if i <= 9:
            resultadoDois = listaA[i] * calcDois
            resultadosListaDois.append(resultadoDois)
            calcDois = calcDois - 1

    somaResultadoslistaDois = sum(resultadosListaDois)
    divDois = somaResultadoslistaDois % 11

    if divDois < 2:
        digitoDois = 0
    else:
        digitoDois = 11 - divDois

    verificador = [digitoUm, digitoDois]

    if listaA[9] == verificador[0] and listaA[10] == verificador[1]:
        print('CPF É VALIDO \n')
    else:
        print('CPF NÃO É VALIDO \n')

    return verificador

#   FUNÇÃO DO MENU QUE VALIDA O CPF 
def menu_cpf():
    """
    Função do menu que valida o CPF

    Parametros: string com os números do CPF
    Retorno: Informa se o CPF é valido ou não e pergunta se deseja validar mais um CPF.
    """
    
    try:
        # Coletando o dado digitado pelo usuário e inserindo os dados em uma lista de inteiros
        cpfDigitado = input('Digite o CPF (11 dígitos, somente números): ')
        cpfLista = [int(digito) for digito in cpfDigitado]

        # Validando se o CPF digitado possui os 11 caracteres
                
        if len(cpfLista) == 11 and len(set(cpfLista)) != 1:
                
            # Chamando a função que valida o CPF
            valida_cpf(cpfLista) 
            print('Deseja consultar um novo CPF?')    
            nova_consulta = input('Digite S para SIM. Ou qualquer Tecla para voltar ao MENU PRINCIPAL: \n')
            nova_consulta = nova_consulta.upper()
            if nova_consulta == 'S':
                menu_cpf()
            else:
                print('Você retornou ao MENU PRINCIPAL \n')
                    
        else:
            print('O CPF digitado NÃO É VÁLIDO. Deve conter 11 dígitos, somente números e não repetidos. Você será direcionado ao MENU PRINCIPAL! \n')
    except ValueError:
        print('Caracteres NÃO aceitos, você será direcionado ao MENU PRINCIPAL! \n')

#   FUNÇÃO QUE REMOVE OS CARACTERES ESPECIAIS
def remove_caracteres_especiais(frase):
    """
    Remove os caracteres de uma string, os espaços do final e do inicio do texto
    
    parametros: string com caractreres especiais
    retorno: string sem caracteres especiais
    """
    frase_sem_especiais = ''.join(caracter for caracter in frase if caracter.isalnum() or caracter.isspace())
    frase_sem_especiais = ' '.join(frase_sem_especiais.split())
    print('Frase sem os caracteres especiais: ', frase_sem_especiais,'\n')

    return frase_sem_especiais
remove_caracteres_especiais

#   FUNÇÃO DO MENU REMOVE CARACTERES ESPECIAIS
def menu_remove_caracteres_especiais():
    """
    Função do Menu que remove os caracteres especiais
    
    Parametros: String S para SIM ou qualquer tecla para retornar ao menu principal / String com caracteres especiais
    Retorno: String sem caracteres especiais e pergunta se deseja remover os caracteres de mais uma frase ou não.
    """

    frase = input('Digite uma frase para remover os caracteres especiais:')
    remove_caracteres_especiais(frase)

    print('Deseja remover os caracteres de uma nova frase? \n')
    consulta_nova = input('Digite S para SIM. Ou qualquer Tecla para voltar ao MENU PRINCIPAL:')
    consulta_nova = consulta_nova.upper()
    if consulta_nova == 'S':
        menu_remove_caracteres_especiais()
    else:
        print('Você retornou ao MENU PRINCIPAL \n')
        

#                                                     ********* APLICAÇÃO PRINCIPAL *********
print('Bem vindo ao BRUTUS APP! \n')
print('Valide CPFs / Remova os caracteres especiais do seu texto \n')
while True:
    try:
        print('Escolha uma opção abaixo, digitando o número correspondente: \n')
        print('1 - Validar CPF')
        print('2 - Remover caracteres especiais')
        print('0 - Sair')

        escolha = int(input('Digite aqui: '))

        if escolha == 1:
            menu_cpf()

        elif escolha == 2:
            menu_remove_caracteres_especiais()
            

        elif escolha == 0:
            print('Você saiu do sistema. \nVolte sempre!')
            break
        else:
            print('Escolha uma opção válida \n')
    except ValueError:
        print("*** ATENÇÃO *** DIGITE UM VALOR VÁLIDO CONFORME O MENU \n")

