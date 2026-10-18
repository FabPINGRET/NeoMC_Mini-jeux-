# Prise : un poisson doré (gold, poids 30 sur 1000) ; @s = joueur, effets au marqueur mg.lfx
scoreboard players add $catch mg.lfn 1
scoreboard players add $gold mg.lfn 1
execute store result score #lfs mg.st run random value 80..120
title @s subtitle [{"text":"un poisson doré","color":"gold","bold":true},{"text":" de ","color":"gray"},{"score":{"name":"#lfs","objective":"mg.st"},"color":"yellow"},{"text":" cm","color":"gray"}]
title @s title {"text":"✨ POISSON DORÉ ✨","color":"gold","bold":true}
tellraw @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] [{"text":"✨ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a sorti ","color":"gray"},{"text":"un poisson doré","color":"gold","bold":true},{"text":" de ","color":"gray"},{"score":{"name":"#lfs","objective":"mg.st"},"color":"yellow"},{"text":" cm","color":"gray"},{"text":" !","color":"gray"}]
execute at @e[type=minecraft:marker,tag=mg.lfx,limit=1] run playsound minecraft:entity.firework_rocket.twinkle player @a[distance=..16] ~ ~ ~ 1 1
execute at @e[type=minecraft:marker,tag=mg.lfx,limit=1] run particle minecraft:firework ~ ~0.3 ~ 0.3 0.5 0.3 0.12 24 normal @a[distance=..16]
function mg:lobby/fish/pb
