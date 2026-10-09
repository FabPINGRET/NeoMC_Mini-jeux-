# Monde de survie régénéré (oct. 2026, structures ×3) : @s garde inventaire et XP mais repart du point de départ (macro id)
# Les anciennes positions (lieu, maison, lit) pointent sur l'ancien terrain : on les remplace.
tag @s add mg.svg2
execute in mg:survie run spreadplayers 100000 100000 0 24 false @s
execute at @s run spawnpoint @s ~ ~ ~
$data modify storage mg:survie p.k$(id).home set from entity @s Pos
$data modify storage mg:survie p.k$(id).pos set from entity @s Pos
$data modify storage mg:survie p.k$(id).dim set value "mg:survie"
$data remove storage mg:survie p.k$(id).resp
effect give @s minecraft:resistance 5 4 true
tellraw @s [{"text":"🌲 Le monde de survie a été régénéré, avec 2 à 3 fois plus de structures (villages, temples, avant-postes, ruines…). ","color":"green"},{"text":"Ton inventaire, ton coffre de l'Ender et ton XP sont conservés ; tu repars du point de départ.","color":"gray"}]
