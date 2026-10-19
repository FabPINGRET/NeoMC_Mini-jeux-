# Grotte de givre : vague de la salle 1
scoreboard players set $od2 mg.st 1
function mg:ombre/dg/ice/close
execute store result score $g mg.st if entity @a[tag=mg.olw,x=-31,y=65,z=-203,dx=89,dy=14,dz=27]
scoreboard players operation $g mg.st *= #2 mg.st
scoreboard players add $g mg.st 3
execute if score $g mg.st matches 10.. run scoreboard players set $g mg.st 9
function mg:ombre/dg/spawn_n
tag @e[tag=mg.oldgn] add mg.oldg2
tag @e[tag=mg.oldgn] add mg.oldg
execute as @e[tag=mg.oldgn,tag=mg.olprov] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,distance=..30]
tag @e[tag=mg.oldgn] remove mg.oldgn
title @a[x=-31,y=65,z=-203,dx=89,dy=14,dz=27] actionbar {"text":"⚔ Grotte de givre : salle 1 / 4","color":"red","bold":true}
playsound minecraft:event.raid.horn hostile @a[x=-31,y=65,z=-203,dx=89,dy=14,dz=27] -17.5 66 -189.5 0.6 1.4
