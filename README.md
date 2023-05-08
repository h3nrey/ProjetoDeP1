# Projeto de P1

## Table of Content

1. Game Story
2. Gameplay
3. Controles
4. Level Design
5. Tecnologias
6. Como Rodar
7. Organização do Projeto
8. Legenda das tiles
9. Referências

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Sumário</h2></summary>
  <ol>
    <li><a href="#game-history">História do jogo</a></li>
    <li><a href="#gameplay">Gameplay</a></li>
    <li><a href="#controles">Controles</a></li>
    <li><a href="#level-design">Level Design</a></li>
    <li><a href="#tecnologies">Tecnologias</a></li>
    <li><a href="#how-to-run">Como Rodar</a></li>
    <li><a href="#code-organization">Organização do Projeto</a></li>
    <li><a href="#tiles-labels">Legenda das tiles</a></li>
    <li><a href="#references">Referências</a></li>
  </ol>
</details>

<h2 id="game-history">
	História do jogo
</h2>
<p>
	A anja brilhante se encontra num labirinto e ela tem que encontrar a chave do portão para escapar do labirinto antes que sua energia vital acabe. Para isso a anja brilhante deve encontrar colétaveis que aumentam sua energia vital que tornando-a capaz de andar de percorrer o labirinto ou aumentar o tempo para a procura da sua escapatória. Ajude ela guiando o caminho que ela deve percorrer para escapar do labirinto. Conto com voce para essa missão...
</p>

## Gameplay

<p>
	A jogabilidade envolve uma perspectiva de topo em que o jogador tem um número limitado de movimentos para navegar através de um ambiente baseado num quadriculado. Ao longo do caminho, tem de recolher três itens - CHAVES, bem como itens opcionais TEMPO e ENERGIA - para progredir através de vários obstáculos. O jogo também inclui puzzles lógicos que o jogador tem de resolver para avançar. O desafio consiste em gerir os movimentos limitados enquanto recolhe estrategicamente os itens necessários e resolve os puzzles, com a opção de escolher se quer ou não recolher TEMPO e ENERGIA para ajudar no seu progresso.
</p>

## Controles

<p>
	R  = Pressione 'R' para reiniciar a fase se sua energia (⚡) acabou.
</p>
<p>
	↑  = Move a anjinha brilhante para cima
</p>
<p>
	↓  = Move a anjinha brilhante para baixo
</p>
<p>
	←  = Move a anjinha brilhante para esquerda
</p>
<p>
	→  = Move a anjinha brilhante para direita
</p>

## Level Design

<p>
	O design dos níveis consiste em salas, cada uma com obstáculos e desafios. Algumas salas têm caixas arrastáveis que podem ser usadas para bloquear caminhos ou activar interruptores. Os formatos geométricos das salas foram concebidos para tornar mais complexos os movimentos do jogador e o controlo dos custos de energia.

    Por exemplo, algumas salas podem ter corredores estreitos que exigem que o jogador manobre cuidadosamente para evitar o desperdício de energia, enquanto outras podem ter grandes espaços abertos que permitem um movimento mais fácil, mas exigem mais energia para atravessar. As caixas arrastáveis podem aumentar a complexidade da resolução de puzzles, uma vez que o jogador tem de as posicionar estrategicamente para ultrapassar obstáculos e conservar energia.

    No geral, o design dos níveis é cuidadosamente concebido para proporcionar uma experiência desafiante mas gratificante aos jogadores à medida que avançam no jogo.

</p>

<h2 id="tecnologies">Tecnologias</h2>

<a href="https://www.python.org">
 Python 3
</a>
<br>
<a href="https://www.pygame.org/wiki/GettingStarted">
Pygame 2
</a>
<br>
<a href="">OS</a>

<!-- ## Como rodar o jogo? -->
<h2 id="how-to-run">Como rodar o jogo?</h2>
<p>
	O jogo requer que o Python e o Pygame estejam instalados no teu sistema. Instruções sobre como instalar o Python e o Pygame podem ser encontradas nos seus respectivos sites. Abra o arquivo `main.py` e compile o código
</p>

<h2 id="code-organization">Organização do Projeto</h2>

<h3>main.py</h3>
<p>
		É o script principal do projeto, lá que o loop do jogo roda e interliga os componentes centrais do jogo
</p>

<h3>settings.py</h3> 
<p>
		É o "armazém" de dados do projeto, todos os dados estáticos, como: a estrutura das fazes, resolução do jogo, tamanho das tiles e etc..
</p>

<h3>player.py</h3>
<p>
	Tudo que o player realiza e suas interações com outros objetos são controlados nesse script.
</p>

<h3>map.py</h3>
<p>Gera as tiles das fases, lendo a estrutura crua dos mapas e decidindo qual tile usar apartir das tags, além disso seta a posição do player</p>

<h3>music.py</h3>
<p>Lida com os sons do jogo, sendo músicas ou efeitos sonoros.</p>

<h3>ui.py</h3>
<p>Cuida de toda a interface do jogo, tanto na parte de criar em si os textos e botões, como de atualizar os seus conteúdos apartir de dados no main.py
</p>

<h3>tile.py</h3>
<p>Classe abstrata das tiles do jogo</p>

<h3>button.py</h3>
<p>Classe especializada da tile que lida com as particularidades dos botões que abrem portões no jogo
</p>

<h3>box.py</h3>
<p>Classe especializada da tile que lida com as particularidades das caixas do jogo</p>

<h2 id="tiles-labels">Legenda das tiles no map</h2>
<ul>
<li>X -> tile das paredes</li>
<li>D(R,L, T, B) -> tile da porta e a rotação da porta</li>
<li>C -> tile do relógio</li>
<li>E -> tila do orb de energia</li>
<li>K -> tile da chave</li>
<li>B -> tile da caixa</li>
<li>P -> define a posição do player</li>
<li>T_coluna/linha -> tile dos botões, a coluna e linha são as posições da tile do bloco impassável</li>
</ul>

<h2 id="references">Referências</h2>
<p>
	O jogo foi inspirado em The Talos Principle, Lara Croft GO, Monument Valley
</p>
