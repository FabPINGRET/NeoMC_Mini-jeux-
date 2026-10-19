# Forge écarlate : vague de la salle 2
scoreboard players set $od5 mg.st 3
execute store result score $g mg.st if entity @a[tag=mg.olw,x=209,y=51,z=125,dx=27,dy=14,dz=89]
scoreboard players operation $g mg.st *= #2 mg.st
scoreboard players add $g mg.st 4
execute if score $g mg.st matches 10.. run scoreboard players set $g mg.st 9
function mg:ombre/dg/spawn_se
tag @e[tag=mg.oldgn] add mg.oldg5
tag @e[tag=mg.oldgn] add mg.oldg
execute as @e[tag=mg.oldgn,tag=mg.olprov] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,distance=..30]
tag @e[tag=mg.oldgn] remove mg.oldgn
title @a[x=209,y=51,z=125,dx=27,dy=14,dz=89] actionbar {"text":"⚔ Forge écarlate : salle 2 / 4","color":"red","bold":true}
playsound minecraft:event.raid.horn hostile @a[x=209,y=51,z=125,dx=27,dy=14,dz=89] 222.5 52 157.5 0.6 1.4
