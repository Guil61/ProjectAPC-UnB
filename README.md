# ProjectAPC-UnB

Os indígenas da etnia Ticuna são um dos poucos que ainda preservam sua língua original dentre
todas as etnias indígenas no Brasil. A língua Ticuna é falada por mais de 40 mil pessoas, ou seja,
ela é uma língua viva. Ela é a primeira língua (L1) aprendida por muitas crianças Ticunas e é
ensinada nas escolas indígenas da região do alto Solimões (região da tríplice fronteira Brasil,
Colômbia e Peru).
A língua Ticuna é uma língua isolada, o que significa que ela não possui parentesco com
nenhuma outra língua viva atual. Mesmo considerando as línguas extintas, aparentemente ela
só tem parentesco com a língua Yuri, do qual se conhece apenas poucas palavras. Além disso,
existem poucos textos escritos em Tikuna traduzidos para o português e vice-versa. Por estas
duas causas, não existe língua parecida com ela e não existem muitas traduções, é difícil treinar
modelos pré-treinados de IA Generativa para a língua Ticuna. Os modelos pré-treinados usam
línguas indo-européias comuns. Ou seja, treinar em outra língua indo-européia fica mais fácil.
Por isso, a proposta deste projeto 1 de APC. Colaborar com a produção de um conjunto de dados
(dataset) para treinar um modelo de IA Generativa para a língua Ticuna.
O projeto consistem em escrever um programa Python para produzir como saída um texto em
que cada frase em português corresponde a uma ou mais frases em Ticuna. O texto em ticuna e
português foi extraído do Nosso Povo, que está em pdf: http://etnolinguistica.wdfiles.com/local-
-files/biblio%3Avarios-1985-toru/Varios_1985_ToruDuuugu_NossoPovo_Ticuna.pdf
Como entrada são dados dois textos extraídos do livro (copiado e colado do arquivo .pdf), um
em português e outro em ticuna. Note que os dois textos contém erros. Ao se fazer a cópia,
alguns erros foram intriduzidos. Faça um programa Python 3.x sem usar listas ou dicionários para
retirar estes erros, tanto do texto em Ticuna como do texto em Português.
