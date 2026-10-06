# Bascule mode spectateur (@s = joueur)
execute store success score @s mg.t if entity @s[tag=mg.spectate]

# Était spectateur → redevient joueur
execute if score @s mg.t matches 1 run tag @s remove mg.spectate
execute if score @s mg.t matches 1 run tellraw @s [{"text":"✔ Tu participeras aux prochaines parties.","color":"green"}]

# Devient spectateur
execute if score @s mg.t matches 0 run tag @s add mg.spectate
execute if score @s mg.t matches 0 run tellraw @s [{"text":"◉ Tu ne participeras plus aux parties (re-clique pour annuler).","color":"gray"}]

# S'il était en pleine partie → abandon
execute if score @s mg.t matches 0 if entity @s[tag=mg.play] run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" abandonne la partie.","color":"gray"}]
execute if score @s mg.t matches 0 if entity @s[tag=mg.play] run function mg:core/eliminate
