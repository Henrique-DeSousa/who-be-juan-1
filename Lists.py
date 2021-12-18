import random

import cowsay


class Responses:
    responses_flirt = ["Ohh hey girl, theres a shopping sale at my house!\nClothes are 100% off..."]

    responses_negro = ["Qual foi a última coisa que passou pela cabeça da princesa Diana?\nO rádio",
                       "Porque é que não existem medicamentos na Etiópia?\nPorque não podem ser tomados em jejum.",
                       "O sujeito vai ao médico:\n– Doutor, tenho tendências suicidas. O que faço?\n– Em primeiro lugar, pague a consulta.",
                       "Qual a diferença entre um padre e um tenista?\nAs bolas com que o tenista brinca têm pelinhos.",
                       "Qual é a parte mais dura de um vegetal?\nA cadeira de rodas.",
                       "O que faz um leproso no banho?\nNestum",
                       "Porque é que a Anne Frank não acabou o diário?\nProblemas de concentração.",
                       "Porque é que o Hitler se suicidou?\nPorque viu a conta do gás.",
                       "O que se chama a dois sem-abrigos a atirar pedras um ao outro?\nUma luta de almofadas.",
                       "Sabias que sem árabes não tinha acontecido o 11/9?\nTinha acontecido o XI/IX.",
                       "Hitler estava a caminhar num campo de concentração quando ouve “sniff, sniff…”.\nVira-se e vê uma menina a chorar enquanto mexia num cinzeiro com o dedo. Hitler aproxima-se, mete-lhe a mão por cima do ombro e pergunta:\n– Era alguém conhecido?",
                       "Qual é a diferença entre uma pizza e um judeu?\nA pizza quando vai ao forno não grita.",
                       "Um menino, com uma mão atrás, disse para uma amiguinha:\n– Adivinha o que eu tenho na minha mãozinha…\n– Um rebuçado!\n– Não, paralisia!",
                       "Mãe, na escola chamam-me mafioso!\n– Não te preocupes, filhinho, amanhã a mãe vai lá e acaba com isso.\n– Boa mãe, mas faz com que pareça um acidente.",
                       "Porque é que o bebé de 6 anos da Etiópia está a chorar?\nEstá a ter uma crise de meia idade.",
                       "O que é que os pais da criança da Etiópia deram ao filho do sexto aniversário?\nFlores para a campa",
                       "Porque é que os pretos não vão para o céu?\nPorque os andaimes não são assim tão altos.",
                       "O que é um judeu a voar?\nFumo",
                       "Quando é que sabes que a tua irmã está com o período?\nQuando a pila do teu pai sabe a sangue.",
                       "Estatística:\n9 em cada 10 pessoas curtem gang rape",
                       "- Mãe, não gosto da avó!\n- Está bem, então come só as batatas.",
                       ]

    responses = ["who be juan kanobi",
                 "gay🚫🧢",
                 "cute,",
                 "fat",
                 "ugly"]

    responses_prefix = ["dropped", "kobe"]

    responses_kill = ["mate-se, fachabor",
                      "O Tejo está à sua espera, atire-se.",
                      "Avada Kedavra!!!"]

    responses_censured = ["fds", "crlh", "puta", "merda", "caralho", "69", "fornicar", "shit", "fuck"]

    responses_cen = ["Olha a linguagem!",
                     "É com essa boca que beijas a tua mãe?",
                     "Tento na língua rapazinho!",
                     "Vê lá se queres apanhar!"
                     ]

    responses_confusion = ["explainnn",
                     "Nem ele sabe",
                     "Não inventes!",
                     "Eu e que não sei",
                     "??",
                     "Não se preocupem, a força está connosco"]

    responses_explanations = ["awn?", "como assim", "ahn?", "what?", "explica"]

    responses_shooting = ["Por razções legais isto é uma brincadeira!",
                          "Bora!",
                          "Eu fico com o Figueira!",
                          "Tenso",
                          "F.B.I. open up!",
                          "Vai tu primeiro, eu sigo-te"
                          ]

    responses_music = ["Man, shut yo ass. Imma just resume this beat",
                       "Imma just resume this, not because you told me",
                       "Bruh, stop talking trash."
                       ]




    def __init__(self, message):
        pig_enri = "```" + cowsay.get_output_string("pig", "macacos?") + "```"
        self.responses_enri = ["https://c.tenor.com/lVLSSglhk1cAAAAC/monkey-cymbals.gif",
                               "https://c.tenor.com/7Glf51FDQZQAAAAM/monkey-annoying.gif",
                               pig_enri,
                               """
                               ┈┈┈┈┈┈┈┈┈┈┈?????????????
┈┈╱▔▔▔▔▔╲┈┈┈??????????
┈╱┈┈╱▔╲╲╲▏┈┈┈?????┈
╱┈┈╱━╱▔▔▔▔▔╲━╮┈┈
▏┈▕┃▕╱▔╲╱▔╲▕╮┃┈┈
▏┈▕╰━▏▊▕▕▋▕▕━╯┈┈
╲┈┈╲╱▔╭╮▔▔┳╲╲┈┈┈
┈╲┈┈▏╭━━━━╯▕▕┈┈┈
┈┈╲┈╲▂▂▂▂▂▂╱╱┈┈┈
┈┈┈┈▏┊┈┈┈┈┊┈┈┈╲┈
┈┈┈┈▏┊┈ This ┈┊▕╲┈┈╲
┈╱▔. ┈ain't it chief ▕╱▔╲▕
┈▏┈┈┈╰┈┈┈┈╯┈┈┈▕▕
┈╲┈┈┈╲┈┈┈┈╱┈┈┈╱┈╲
┈┈╲┈┈▕▔▔▔▔▏┈┈╱╲╲╲▏
┈╱▔┈┈▕┈┈┈┈▏┈┈▔╲▔▔
┈╲▂▂▂╱┈┈┈┈╲▂▂▂╱┈

                               """]

        self.responses_olek = [f"Olha {message.author.mention} sobes ao {random.randint(0, 1000)}º andar e saltas.",
                               "Isso dá muito trabalho...",
                               "@rogue#0001 faz tu!",
                               "https://media1.tenor.com/images/5ad50b6db3dc7ed4ca10dd65d4ea84c2/tenor.gif?itemid=11811769",
                               "levas com a garrafa",
                               f"Olha {message.author.mention}... sobes e saltas",
                               "Não quero"]

        self.responses_trash = [f"Bruh,{message.author.mention} shut yo ass",
                                f"Juan, at your service Señor{message.author.mention}",
                                "Bruh, really? You can do better. Com'on",
                                "Anything else, you trash"]