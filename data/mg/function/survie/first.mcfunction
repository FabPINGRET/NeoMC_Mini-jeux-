# Première arrivée en survie : point de départ commun, point de réapparition posé
execute in mg:survie run spreadplayers 100000 100000 0 24 false @s
execute at @s run spawnpoint @s ~ ~ ~
$data modify storage mg:survie p.k$(id).home set from entity @s Pos
$data modify storage mg:survie p.k$(id).pos set from entity @s Pos
$data modify storage mg:survie p.k$(id).dim set value "mg:survie"
tellraw @s [{"text":"🌲 Bienvenue dans le monde de survie !","color":"green","bold":true}]
tellraw @s [{"text":"Ton inventaire, ton XP et ta position sont gardés quand tu repars aux mini-jeux. Retour : menu Échap → ≡ Menu (ou /trigger mg.sv set 2).","color":"gray"}]
