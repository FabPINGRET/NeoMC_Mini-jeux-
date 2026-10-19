# Puits des âmes : vague de la salle 1
scoreboard players set $od7 mg.st 1
function mg:ombre/dg/souls/close
execute store result score $g mg.st if entity @a[tag=mg.olw,x=-223,y=45,z=131,dx=27,dy=14,dz=89]
scoreboard players operation $g mg.st *= #2 mg.st
scoreboard players add $g mg.st 3
execute if score $g mg.st matches 10.. run scoreboard players set $g mg.st 9
function mg:ombre/dg/spawn_sw
tag @e[tag=mg.oldgn] add mg.oldg7
tag @e[tag=mg.oldgn] add mg.oldg
execute as @e[tag=mg.oldgn,tag=mg.olprov] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,distance=..30]
tag @e[tag=mg.oldgn] remove mg.oldgn
title @a[x=-223,y=45,z=131,dx=27,dy=14,dz=89] actionbar {"text":"⚔ Puits des âmes : salle 1 / 4","color":"red","bold":true}
playsound minecraft:event.raid.horn hostile @a[x=-223,y=45,z=131,dx=27,dy=14,dz=89] -209.5 46 144.5 0.6 1.4
