__Projeto Final da UC Fundamentos de Programação__

__Autoras:__ Leonor Figueiredo nº21902968

__Contas *GitHub*:__ Leonor9999Glitched

__*Link GitHub:*__ https://github.com/DanielaGameiro/Projeto-FP.git

# O que aconteceu durante o trabalho

Durante o projeto, chegou-se à conclusão que seria melhor dividir o programa em classes e modulos. O programa principal começa no ficheiro Menu_principal. Apartir daí, dependendo dos comando do utilizador, o programa avançará para outros modulos.

Se o utilizador escolher o botão que disse "Rules", o modulo Rules.py irá abrir e o utilizador poderá ver as regras do jogo. Para regressar ao Menu_principal, só precisa de clicar no botão "Exit".

Se o utilizador escolher o botão "Game", o modulo Game.py irá abrir e o jogo começará. O jogador poderá controlar a ovelha ou os lobos. Para sair deste do jogo, é só preciso clicar no borão Exit.

Para terminar o programa, ou o utilizador clica na cruz vermelha da janela ou clica no botão Exit no modulo Menu_principal.

No ficheiro Game.py, há três classes que ajudam a completar esta parte. A Class Board, que desenha o tabuleiro, e que verifica se não peça nenhuma no lugar para onde queremos mover a peça que seleccionamos. A Class Game que é a classe onde o jogo irá decorrer. A Class Game_functions que é onde as funções de todo programa estarão, o mover as peças, seleccionar as peças e verificar se há movimentos disponiveis. A Class Piece é responsavel por desenhar as peças, calcular onde é que cada peça vai ser colocada e onde é que começam no tabuleiro.

# Mudança de ramo

Perto do final trabalho, houve a criação de um novo ramo para testar umas ideias que tive.

Durante o processo de trabalho, eu tive a seguir um tutorial, na esperança que de que me ajudasse com o projecto porém, vim a descobrir de que o tutorial podia não estar-se a adaptar bem ao projecto e então, numa última tentativa de tentar fazer algo, criei um segundo ramo chamado Text. Era suposto ter o nome Test mas, naquela altura de desespero, escrevi mal o nome.

Usando o comando, git checkout Text, pode-se aceder a esse branch.

# Inesperado

A build foi criada a partir do que estava feito no branch main. O outro branch chamado de Text era suposto ser uma experiência portanto, não foi usado na build.

Durante o projecto, nada de muito dificil aconteceu. Até que se fez a build. Segmentation Fault foi, inicialmente, o erro que ocorreu. O programa não abre, apesar de que o código não dá suspeitas de algo estar em errado.

Após dar-se uma verificação no código e de desinstalar e instalar novamente o Python e Pygame, um novo erro surgiu. Usando o Prompt de Comando (cmd), este foi o erro que foi assinalado:

"Traceback (most recent call last):
  File "Menu_principal.py", line 112, in <module>
  File "Menu_principal.py", line 35, in Menu_principal
  File "pygame\sysfont.py", line 415, in SysFont
  File "pygame\sysfont.py", line 333, in font_constructor
TypeError: expected str, bytes or os.PathLike object, not BytesIO
[10088] Failed to execute script Menu_principal"

Examinando o texto, parece que o erro desta vez das próprias fontes (letras) do python. Parece que a build não está a reagir bem às fontes (letras) usadas no jogo.

Infelizmente, este erro não foi resolvido. Não tinha acesso a essa biblioteca interior do python.

# Referências

Para fazer este trabalho, houve uma pesquisa e algum auxilio da Internet.

Estes são os links de onde a ajuda veio:

- https://www.youtube.com/watch?v=vnd3RfeG3NM&t=461s
- https://www.youtube.com/watch?v=LSYj8GZMjWY
- https://www.youtube.com/watch?v=_kOXGzkbnps
- tps://www.pygame.org/docs/ref/key.html