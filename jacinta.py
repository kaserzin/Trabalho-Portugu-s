import random
import time
ne = "\033[1m"
nu = "\033[0m"
while True:
    time.sleep(0.5)
    select = int(input(f'''{ne}Escolha alguma das opções abaixo.{nu}
    {ne}1{nu} - Sorteador de alunos.
    {ne}2{nu} - Questão 1
    {ne}3{nu} - Questão 2
    {ne}4{nu} - Questão 3
    {ne}5{nu} - Finalizar Apresentação
    {ne}Selecione alguma opção:{nu} '''))    
    lista_aluno = ["Giovane Abrantes Ferreira",
               "Carlos Adriano Dias Limeira",
               "Maria Aurelice Moreira Cavalcanti",
               " Ana Beatriz Delfino dos Santos",
               "Isaque Carolino de Sousa Abreu",
               " Yara Cipriano Bezerra",
               "Albevania da Silva Juvenal",
               "Guilherme da Silva Mariano",
               "Lucas das Chagas de Souza",
               "Mirela de Aquino Vieira", 
               "Gabrielly de Carvalho Francilino",
               "Francisco Everton Maciel Rodrigues",
               "Lourena Feitosa Barbosa",
               "Gabrielle Feitosa de Sousa",
               "Camila Feitosa Pereira",
               "João Henrique de Oliveira Saturnino",
               "Francisco Jaime de Araújo Mendes",
               "Lauro José Varandas Nogueira Filho",
               "Kayo Kennedy da Silva",
               "Brenda Letícia Ferreira da Silva",
               "Dateline Linhares dos Santos", 
               "Bianca Lira Salvador",
               "Maria Livya Lima da Silva", 
               "Samira Maria da Silva",
               "Israel Nóbrega Temoteo",
               "Camila Pereira Braga",
               "Nataly Pereira da Silva",
               "Iohana Soares Albuquerque",
               "Arianne Vieira Rodrigues",
               "Karla Pedrina Duarte Pivetta",
               "Marcos Vinicius Pereira Dias"]
    if select == 1:
        time.sleep(0.3)
        print(f'Os alunos escolhidos foram:\033[{random.randint(31, 36)}m {random.choice(lista_aluno)}\033[0m\n',)
        time.sleep(0.3)
    elif select == 2:
        print('''Pergunta nº1
(URCA) “Até agora não pudemos saber se há ouro ou prata nela, ou outra coisa de metal, ou ferro; nem lha vimos. Contudo a terra em si é de muito bons ares frescos e temperados como os de Entre-Douro-e-Minho, porque neste tempo d'agora assim os achávamos como os de lá. Águas são muitas; infinitas. Em tal maneira é graciosa que, querendo-a aproveitar, dar-se-á nela tudo; por causa das águas que tem!”
Este é um trecho da Carta de Pero Vaz de Caminha sobre o “achamento” das terras do Brasil. Das alternativas abaixo sobre a Carta só é CORRETO afirmar:''')
        time.sleep(0.4)
        res = str(input(f'''{ne}A){nu} Cronologicamente a Carta de Pero Vaz de Caminha insere-se no Barroco brasileiro.
{ne}B){nu} O estilo ufanista e emotivo prenuncia características do Romantismo brasileiro.
{ne}C){nu} Entre outros textos do século XVI em forma de diários, tratados e crônicas, a Carta de Pero Vaz de Caminha é tida como literatura de informação.
{ne}D){nu} Escrita em versos, a Carta de Pero Vaz de Caminha é considerada o primeiro poema épico da literatura brasileira.
{ne}E){nu} Não se pode dizer que foi por cumprimento do dever do cargo de escrivão que Pero Vaz de Caminha escreveu a Carta.
{ne}Resposta:{nu} '''))
        if res == "a" or res == 'A':
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.5)
            print('Resposta ERRADA! ')
            print('')
        elif res == 'b' or res == 'B':
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.5)
            print('Resposta ERRADA! ')
            print('')
        elif res == 'c' or res == 'C':
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.5)
            print('Resposta CERTA!')
            print('')
        elif res == 'd' or res == 'D':
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.5)
            print('Resposta ERRADA!')
            print('')
        elif res == 'e' or res == 'E':
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.5)
            print('Resposta ERRADA! ')
            print('')
        else:
            print('Algo deu errado tente novamnete! ')
            print('')    
    elif select == 3:
        time.sleep(0.5)
        print('(UFSM) Sobre a literatura produzida no primeiro século da vida colonial brasileira, é correto afirmar que:')
        time.sleep(0.5)
        res = str(input(f'''{ne}A){nu} É formada principalmente de poemas narrativos e textos dramáticos que visavam à catequese.
{ne}B){nu} Inicia com Prosopopeia, de Bento Teixeira.
{ne}C){nu} É constituída por documentos que informam acerca da terra brasileira e pela literatura jesuítica.
{ne}D){nu} Os textos que a constituem apresentam evidente preocupação artística e pedagógica.
{ne}E){nu} Descreve com fidelidade e sem idealizações a terra e o homem, ao relatar as condições encontradas no Novo Mundo.
{ne}Resposta:{nu} '''))
        if res == "a" or res == 'A':
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.5)
            print('Resposta ERRADA! ')
            print('')
        elif res == 'b' or res == 'B':
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.5)
            print('Resposta ERRADA! ')
            print('')
        elif res == 'c' or res == 'C':
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.5)
            print('Resposta CERTA!')
            print('')
        elif res == 'd' or res == 'D':
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.5)
            print('Resposta ERRADA!')
            print('')
        elif res == 'e' or res == 'E':
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.5)
            print('Resposta ERRADA! ')
            print('')
        else:
            print('Algo deu errado tente novamnete! ')
            print('')
    elif select == 4:
        time.sleep(0.5)
        print('''PUC-Campinas) Napoleão Bonaparte e Adolf Hitler, entre outros, sonharam com a pan-Europa que, com a inclusão de mais dez países, se tornou uma realidade irreversível. Os antecedentes da União Europeia são assim, alguns mais respeitáveis do que outros. Durante muito tempo depois da tentativa de Carlos Magno de substituir o império romano pelo seu, uma identidade europeia se definia mais pelo que não era do que pelo que era: cristã e não muçulmana, civilizada em vez de bárbara (e, portanto, com o direito de subjugar e europeizar os bárbaros − isto é, o resto do mundo).
Num processo de colonização, o colonizador vê o nativo como um elemento a ser não apenas fisicamente dominado, mas também como alguém a quem deve impor ideias e convicções. Exemplo disso ocorreu, entre nós, com''')  
        time.sleep(0.5)
        res = str(input(f'''{ne}A){nu} A utilização didática do teatro, pelo Padre Anchieta, com a finalidade de conversão do gentio.
{ne}B){nu} O empenho com que o poeta Gregório de Matos satirizava os costumes populares da cidade da Bahia.
{ne}C){nu} A influência exercida pelos poetas clássicos sobre os nossos escritores arcádicos.
{ne}D){nu} Os romances de José de Alencar, inteiramente tributários da tradição literária portuguesa.
{ne}E){nu} A poesia de Castro Alves, cujo vigor. se deveu aos modelos literários dos iluministas franceses.
{ne}Resposta:{nu} '''))
        if res == "a" or res == 'A':
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.5)
            print('Resposta CERTA! ')
            print('')
        elif res == 'b' or res == 'B':
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.5)
            print('Resposta ERRADA! ')
            print('')
        elif res == 'c' or res == 'C':
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.5)
            print('Resposta ERRADA!')
            print('')
        elif res == 'd' or res == 'D':
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.5)
            print('Resposta ERRADA!')
            print('')
        elif res == 'e' or res == 'E':
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('.')
            time.sleep(0.5)
            print('Resposta ERRADA! ')
            print('')
        else:
            print('Algo deu errado tente novamnete! ')
            print('')
    elif select == 5:
        time.sleep(0.5)
        print(f'\033[41m{ne}Fim da apresentação{nu}')
        print(f'{ne}Obrigado pela atenção{nu}')
        print('''                                        code by: @pedro.kaser
                                                ! 01' Kaser#4807''')
        break 