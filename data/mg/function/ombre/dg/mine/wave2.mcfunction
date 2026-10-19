# Mines profondes : vague de la salle 3
scoreboard players set $od6 mg.st 5
execute store result score $g mg.st if entity @a[tag=mg.olw,x=-61,y=47,z=143,dx=27,dy=14,dz=89]
scoreboard players operation $g mg.st *= #2 mg.st
scoreboard players add $g mg.st 5
execute if score $g mg.st matches 10.. run scoreboard players set $g mg.st 9
function mg:ombre/dg/spawn_s
tag @e[tag=mg.oldgn] add mg.oldg6
tag @e[tag=mg.oldgn] add mg.oldg
execute as @e[tag=mg.oldgn,tag=mg.olprov] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,distance=..30]
tag @e[tag=mg.oldgn] remove mg.oldgn
title @a[x=-61,y=47,z=143,dx=27,dy=14,dz=89] actionbar {"text":"⚔ Mines profondes : salle 3 / 4","color":"red","bold":true}
playsound minecraft:event.raid.horn hostile @a[x=-61,y=47,z=143,dx=27,dy=14,dz=89] -47.5 48 195.5 0.6 1.4
