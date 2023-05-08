# Projeto de P1

## Table of Content

1. Game Story
2. Gameplay
3. Controls
4. Level Design
5. Code Organization
6. How to Run
7. Labels
8. References

## Game Story
<h4>English</h4>
<p>
	The bright angel is in a labyrinth and she has to find the gate key to escape the labyrinth before her life energy runs out. For this, the bright angel must find collectibles that increase her vital energy, making her able to walk through the labyrinth or increase the time for the search for her escape. Help her by guiding her along the way to escape the labyrinth. I count on you for this mission...
</p>
<h4>Português</h4>
<p>
	A anja brilhante se encontra num labirinto e ela tem que encontrar a chave do portão para escapar do labirinto antes que sua energia vital acabe. Para isso a anja brilhante deve encontrar colétaveis que aumentam sua energia vital que tornando-a capaz de andar de percorrer o labirinto ou aumentar o tempo para a procura da sua escapatória. Ajude ela guiando o caminho que ela deve percorrer para escapar do labirinto. Conto com voce para essa missão...
</p>

## Gameplay
<h4>English</h4>
<p>
	The gameplay involves a topview perspective where the player has a limited number of moves to navigate through a grid-based environment. Along the way, they must collect three items - KEYS, as well as optiona\l items TIME and ENERGY - to progress through various obstacles. The game also features logic puzzles that the player must solve to advance. The challenge lies in managing the limited moves while strategically collecting the necessary items and solving the puzzles, with the option to choose whether or not to collect TIME and ENERGY to aid in their progress.
</p>
<h4>Português</h4>
<p>
	A jogabilidade envolve uma perspectiva de topo em que o jogador tem um número limitado de movimentos para navegar através de um ambiente baseado num quadriculado. Ao longo do caminho, tem de recolher três itens - CHAVES, bem como itens opcionais TEMPO e ENERGIA - para progredir através de vários obstáculos. O jogo também inclui puzzles lógicos que o jogador tem de resolver para avançar. O desafio consiste em gerir os movimentos limitados enquanto recolhe estrategicamente os itens necessários e resolve os puzzles, com a opção de escolher se quer ou não recolher TEMPO e ENERGIA para ajudar no seu progresso.
</p>

## Controls
<p>
	R  = Press 'R' to restart the stage if your energy (E) is empty.
</p>
<p>
	↑  = Move the Brigth Angel up
</p>
<p>
	↓  = Move the Brigth Angel down
</p>
<p>
	←  = Move the Brigth Angel left
</p>
<p>
	→  = Move the Brigth Angel right
</p>

## Level Design
<h4>English</h4>
<p>
	The level design consists of rooms, each with obstacles and challenges. Some rooms feature draggable boxes that can be used to block paths or activate switches. The geometric formats of the rooms are designed to add complexity to the player's movement and control of energy costs.

	For example, some rooms may have narrow corridors that require the player to maneuver carefully to avoid wasting energy, while others may have large open spaces that allow for easier movement but require more energy to traverse. The draggable boxes can add further complexity to the puzzle-solving, as the player must strategically position them to overcome obstacles and conserve energy.

	Overall, the level design is carefully crafted to provide a challenging yet rewarding experience for players as they progress through the game.
</p>
<h4>Português</h4>
<p>
	O design dos níveis consiste em salas, cada uma com obstáculos e desafios. Algumas salas têm caixas arrastáveis que podem ser usadas para bloquear caminhos ou activar interruptores. Os formatos geométricos das salas foram concebidos para tornar mais complexos os movimentos do jogador e o controlo dos custos de energia.

	Por exemplo, algumas salas podem ter corredores estreitos que exigem que o jogador manobre cuidadosamente para evitar o desperdício de energia, enquanto outras podem ter grandes espaços abertos que permitem um movimento mais fácil, mas exigem mais energia para atravessar. As caixas arrastáveis podem aumentar a complexidade da resolução de puzzles, uma vez que o jogador tem de as posicionar estrategicamente para ultrapassar obstáculos e conservar energia.

	No geral, o design dos níveis é cuidadosamente concebido para proporcionar uma experiência desafiante mas gratificante aos jogadores à medida que avançam no jogo.
</p>

## Code Organization:

<h3>main.py</h3>
<p>
    It's the game controlller, is there that the game loop and the core of the game will be
</p>

<h3>settings.py</h3> 
<p>
    stores all the constant variables of the project, there you'll find things like: the resolution of the game, and stats of the player
</p>

## how to run the game?
<h4>English</h4>
<p>
	The game requires Python and Pygame to be installed on your system. Instructions on how to install Python and Pygame can be found on their respective websites. Open the `main.py` and compile the code
</p>
<h4>Português</h4>
<p>
	O jogo requer que o Python e o Pygame estejam instalados no teu sistema. Instruções sobre como instalar o Python e o Pygame podem ser encontradas nos seus respectivos sites. Abra o arquivo `main.py` e compile o código
</p>

## Label of the cell letters in the map

<ul>
<li>X -> a block that the player cant pass through</li>
<li>D -> a door</li>
<li>C -> a clock</li>
<li>E -> an energy orb</li>
<li>K -> a key</li>
<li>B -> a draggable box</li>

</ul>

## References

<h4>English</h4>
<p>
	The game was inspired by The Talos Principle, Lara Croft GO, Monument Valley
</p>
<h4>Português</h4>
<p>
	O jogo foi inspirado em The Talos Principle, Lara Croft GO, Monument Valley
</p>
