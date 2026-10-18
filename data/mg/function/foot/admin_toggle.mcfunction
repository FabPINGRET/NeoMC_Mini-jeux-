# Admin (@s) : coupe / rétablit le terrain de foot ($ftoff mg.st = 1 : coupé, absent : actif)
execute store success score #ftw mg.st if score $ftoff mg.st matches 1
execute if score #ftw mg.st matches 1 run scoreboard players reset $ftoff mg.st
execute if score #ftw mg.st matches 1 run function mg:foot/entry_open
execute if score #ftw mg.st matches 1 run return run tellraw @s {"text":"⚽ Terrain de foot : activé (tapis rallumé).","color":"green"}
scoreboard players set $ftoff mg.st 1
kill @e[type=minecraft:sulfur_cube,tag=mg.ball]
execute as @a[x=-17,y=46,z=-41,dx=38,dy=8,dz=27] run function mg:foot/leave
execute as @a run function mg:foot/cleanup
execute as @a[tag=mg.ftin] run scoreboard players reset @s mg.ft
tag @a remove mg.ftin
tag @a remove mg.ftlt
function mg:foot/entry_close
tellraw @s {"text":"⚽ Terrain de foot : désactivé (joueurs renvoyés au spawn, tapis éteint).","color":"red"}
