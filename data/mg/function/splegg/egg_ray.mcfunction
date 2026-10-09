# Un pas du rayon (0,25 bloc, @s = l'œuf) : neige → l'œuf disparaît et le bloc casse ; autre bloc plein → fin ; air → on avance
# (arêtes frôlées ou œuf qui touche un joueur : rien de cassé, accepté)
execute if block ~ ~ ~ minecraft:snow_block run kill @s
execute if block ~ ~ ~ minecraft:snow_block run return run function mg:splegg/hit
execute unless block ~ ~ ~ #minecraft:air run return 0
scoreboard players remove $sgs mg.st 1
execute if score $sgs mg.st matches 1.. positioned ^ ^ ^0.25 run function mg:splegg/egg_ray
