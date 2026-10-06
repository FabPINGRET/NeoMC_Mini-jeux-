# Joueur suivant, ou fin du tour de plateau -> roulette du mini-jeu
tag @a remove mg.mpcur
scoreboard players add $mpt mg.st 1
execute if score $mpt mg.st > $mpn mg.st run return run function mg:party/round_end
scoreboard players set $mph mg.st 0
