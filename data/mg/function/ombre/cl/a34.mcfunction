# Météore : zone visée (40 blocs), impact 1,5 s plus tard
scoreboard players operation $d mg.st = $pw mg.st
scoreboard players operation $d mg.st *= #2 mg.st
scoreboard players add $d mg.st 30
execute store result storage mg:ombre s.d int 1 run scoreboard players get $d mg.st
scoreboard players set $olr mg.st 0
scoreboard players operation $own mg.st = @s mg.olpid
execute anchored eyes positioned ^ ^ ^0.6 run function mg:ombre/cl/meteo
playsound minecraft:entity.wither.shoot player @a ~ ~ ~ 1 0.6
function mg:ombre/cl/end
