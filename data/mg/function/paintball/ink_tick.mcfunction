# Encre et peinture sous les pieds (@s = joueur, à sa position)
# Sol : 0 neutre, 1 ma peinture, 2 peinture adverse
scoreboard players set $on mg.st 0
execute if entity @s[team=mg_red] if block ~ ~-0.2 ~ minecraft:orange_concrete run scoreboard players set $on mg.st 1
execute if entity @s[team=mg_red] if block ~ ~-0.2 ~ minecraft:blue_concrete run scoreboard players set $on mg.st 2
execute if entity @s[team=mg_blue] if block ~ ~-0.2 ~ minecraft:blue_concrete run scoreboard players set $on mg.st 1
execute if entity @s[team=mg_blue] if block ~ ~-0.2 ~ minecraft:orange_concrete run scoreboard players set $on mg.st 2
execute if score $on mg.st matches 1 run effect give @s minecraft:speed 1 1 true
execute if score $on mg.st matches 2 run effect give @s minecraft:slowness 1 1 true
# Encre : +1/tick, +3/tick sur sa propre peinture
scoreboard players add @s mg.pi 1
execute if score $on mg.st matches 1 run scoreboard players add @s mg.pi 2
execute if score @s mg.pi matches 201.. run scoreboard players set @s mg.pi 200
# Les touches se dissipent (une toutes les 3 s)
execute if score @s mg.ph matches 1.. run scoreboard players add @s mg.pt 1
execute if score @s mg.pt matches 60.. run scoreboard players remove @s mg.ph 1
execute if score @s mg.pt matches 60.. run scoreboard players set @s mg.pt 0
function mg:paintball/ink_bar
