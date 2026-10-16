# @s a abattu un carnotaure : 120 ₵ (+ mission de chasse), les autres chasseurs ont une part
scoreboard players set @s mg.tvkc 0
function mg:terra/rpg/k_carno
scoreboard players add @s mg.tvc 120
function mg:terra/rpg/xp {n:60}
scoreboard players set @s mg.tval 40
title @s actionbar [{"text":"+120 ₵ ","color":"gold","bold":true},{"text":"carnotaure abattu !","color":"gray"}]
execute at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.6 1.2
tellraw @a[tag=mg.tvw] [{"text":"🦖 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" a abattu le carnotaure !","color":"red","bold":true}]
execute if entity @e[tag=mg.tvhunt] run return 0
tag @s add mg.tvkill
execute if score @s mg.tvm matches 4 run function mg:terra/m4_done
execute as @a[tag=mg.tvw,tag=!mg.tvkill,scores={mg.tvm=4}] run function mg:terra/m4_share
tag @s remove mg.tvkill
