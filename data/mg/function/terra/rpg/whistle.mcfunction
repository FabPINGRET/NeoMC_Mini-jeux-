# @s : sifflet : son raptor apparaît à côté de lui (l'ancien est renvoyé) et il monte dessus
execute if score @s mg.trmt matches ..0 run return 0
execute if score @s mg.trsc matches 1.. run return 0
scoreboard players set @s mg.trsc 40
function mg:terra/rpg/mount_gone
tag @e[tag=mg.tvlast] remove mg.tvlast
scoreboard players add $tvid mg.st 1
summon minecraft:horse ~ ~ ~ {Tags:["mg.tv","mg.tvd","mg.tvn","mg.tvlast","mg.trmount","mg.tvs_raptor"],Tame:1b,PersistenceRequired:1b,Silent:1b,SaddleItem:{id:"minecraft:saddle",count:1},equipment:{saddle:{id:"minecraft:saddle",count:1}},active_effects:[{id:"minecraft:invisibility",duration:-1,amplifier:0,show_particles:0b}],attributes:[{id:"minecraft:movement_speed",base:0.34},{id:"minecraft:jump_strength",base:0.95},{id:"minecraft:max_health",base:40},{id:"minecraft:step_height",base:1.6},{id:"minecraft:safe_fall_distance",base:12}]}
data modify entity @e[tag=mg.tvlast,limit=1] Owner set from entity @s UUID
execute if score $rp mg.st matches 1 run function mg:terra/dino/raptor_rp
execute unless score $rp mg.st matches 1 run function mg:terra/dino/raptor_bd
scoreboard players operation @e[tag=mg.tvn] mg.tvid = $tvid mg.st
scoreboard players operation @e[tag=mg.tvn] mg.tvses = $tvses mg.st
scoreboard players operation @e[tag=mg.tvlast] mg.tvo = @s mg.tvpid
scoreboard players set @e[tag=mg.tvlast] mg.tvph 0
tag @e[tag=mg.tvn] remove mg.tvn
ride @s mount @e[tag=mg.tvlast,limit=1]
execute at @s run playsound minecraft:entity.fox.screech player @a ~ ~ ~ 1 1.3
