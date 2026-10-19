# ⚽ Terrain de foot : entretien toutes les 2 s (core/tick : $lan mg.t = 30, chunks chargés)
# terrain coupé par un admin : plus de balle
execute if score $ftoff mg.st matches 1 run kill @e[type=minecraft:sulfur_cube,tag=mg.ball]
execute if score $ftoff mg.st matches 1 run return 0
# joueurs d'équipe (ou comptés à l'entrée) qui ne sont plus sur le terrain
execute as @a[tag=mg.ftr] run function mg:foot/away
execute as @a[tag=mg.ftb] run function mg:foot/away
execute as @a[tag=mg.ftin] run function mg:foot/away
# balle : une seule, tagguée (les autres sulfur_cube de la zone disparaissent ; deux balles : on repart de zéro)
kill @e[type=minecraft:sulfur_cube,tag=!mg.ball,x=-17,y=46,z=-41,dx=38,dy=8,dz=27]
# balle d'une ancienne forme (bloc d'oak_planks) : tuée, ball_new en fait une nouvelle
execute as @e[type=minecraft:sulfur_cube,tag=mg.ball] unless entity @s[nbt={equipment:{body:{id:"minecraft:test_block"}}}] run kill @s
execute store result score $ftk mg.ft if entity @e[type=minecraft:sulfur_cube,tag=mg.ball]
execute if score $ftk mg.ft matches 2.. run kill @e[type=minecraft:sulfur_cube,tag=mg.ball]
execute unless score $ftk mg.ft matches 1 run function mg:foot/ball_new
execute as @e[type=minecraft:sulfur_cube,tag=mg.ball,limit=1] unless entity @s[x=-16,y=47,z=-40,dx=36,dy=6,dz=18] run function mg:foot/ball_home
function mg:foot/ball_idle
# sur le terrain : pas de PvP (la chute ne fait déjà rien au lobby : core/attr_reset), score, remise à zéro du score quand il est vide
effect give @a[x=-17,y=46,z=-41,dx=38,dy=8,dz=27] minecraft:resistance 3 4 true
scoreboard players add @a[x=-17,y=46,z=-41,dx=38,dy=8,dz=27] mg.ft 0
title @a[x=-17,y=46,z=-41,dx=38,dy=8,dz=27] actionbar [{"text":"⚽ ","color":"white"},{"text":"🔴 ","color":"red"},{"score":{"name":"$ftr","objective":"mg.ft"},"color":"red","bold":true},{"text":" – ","color":"gray"},{"score":{"name":"$ftb","objective":"mg.ft"},"color":"blue","bold":true},{"text":" 🔵","color":"blue"},{"text":" · tes buts libres ","color":"gray"},{"score":{"name":"*","objective":"mg.ft"},"color":"yellow"}]
execute if entity @a[x=-17,y=46,z=-41,dx=38,dy=8,dz=27] run scoreboard players set $fte mg.ft 0
execute unless entity @a[x=-17,y=46,z=-41,dx=38,dy=8,dz=27] run scoreboard players add $fte mg.ft 1
execute if score $fte mg.ft matches 15.. run function mg:foot/score_reset
