# Admin (@s) : coupe / rétablit la pêche à l'étang ($lfoff mg.st = 1 : coupée, absent : active)
execute store success score #lfw mg.st if score $lfoff mg.st matches 1
execute if score #lfw mg.st matches 1 run scoreboard players reset $lfoff mg.st
execute if score #lfw mg.st matches 1 run function mg:lobby/fish/build
execute if score #lfw mg.st matches 1 run return run tellraw @s {"text":"🎣 Pêche à l'étang : activée (socle reposé).","color":"green"}
scoreboard players set $lfoff mg.st 1
kill @e[tag=mg.lfs]
kill @e[type=minecraft:marker,tag=mg.lfm]
tag @a remove mg.lfc
setblock 36 64 -27 minecraft:air
clear @a *[minecraft:custom_data~{mg_rod:1b}]
execute as @e[type=minecraft:item] if items entity @s contents *[minecraft:custom_data~{mg_rod:1b}] run kill @s
function mg:lobby/fish/purge
tellraw @s {"text":"🎣 Pêche à l'étang : désactivée (socle et cannes retirés).","color":"red"}
