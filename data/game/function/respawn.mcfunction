execute if score Inventory HeartContainers matches 11 run attribute @a[scores={DeathFlag=1},limit=1,tag=mg.flw] minecraft:max_health base set 22
execute if score Inventory HeartContainers matches 12 run attribute @a[scores={DeathFlag=1},limit=1,tag=mg.flw] minecraft:max_health base set 24
execute if score Inventory HeartContainers matches 13 run attribute @a[scores={DeathFlag=1},limit=1,tag=mg.flw] minecraft:max_health base set 26
execute if score Inventory HeartContainers matches 14 run attribute @a[scores={DeathFlag=1},limit=1,tag=mg.flw] minecraft:max_health base set 28
execute if score Inventory HeartContainers matches 15 run attribute @a[scores={DeathFlag=1},limit=1,tag=mg.flw] minecraft:max_health base set 30
execute if score Inventory HeartContainers matches 16 run attribute @a[scores={DeathFlag=1},limit=1,tag=mg.flw] minecraft:max_health base set 32
execute if score Inventory HeartContainers matches 17 run attribute @a[scores={DeathFlag=1},limit=1,tag=mg.flw] minecraft:max_health base set 34
execute if score Inventory HeartContainers matches 18 run attribute @a[scores={DeathFlag=1},limit=1,tag=mg.flw] minecraft:max_health base set 36
execute if score Inventory HeartContainers matches 19 run attribute @a[scores={DeathFlag=1},limit=1,tag=mg.flw] minecraft:max_health base set 38
execute if score Inventory HeartContainers matches 20 run attribute @a[scores={DeathFlag=1},limit=1,tag=mg.flw] minecraft:max_health base set 40

effect give @a[scores={DeathFlag=1},tag=mg.flw] minecraft:regeneration 3 100 true

execute as @a[scores={DeathFlag=1},tag=mlc_tag,tag=mg.flw] run function main_quest:mlc/die_lose

execute as @a[scores={DeathFlag=1},tag=mg.flw] if score @s DeathCount matches 1 run tellraw @a[tag=mg.flw] [{"selector":"@s"}," has died for the first time"]
execute as @a[scores={DeathFlag=1},tag=mg.flw] if score @s DeathCount matches 2..68 run tellraw @a[tag=mg.flw] [{"selector":"@s"}," has died ",{"score":{"name":"@s","objective":"DeathCount"}}," times"]
execute as @a[scores={DeathFlag=1},tag=mg.flw] if score @s DeathCount matches 69 run tellraw @a[tag=mg.flw] [{"selector":"@s"}," has died ",{"score":{"name":"@s","objective":"DeathCount"}}," times. Haha!"]
execute as @a[scores={DeathFlag=1},tag=mg.flw] if score @s DeathCount matches 70..99 run tellraw @a[tag=mg.flw] [{"selector":"@s"}," has died ",{"score":{"name":"@s","objective":"DeathCount"}}," times"]

execute as @a[scores={DeathFlag=1},tag=mg.flw] if score @s DeathCount matches 100..999 run tellraw @a[tag=mg.flw] [{"selector":"@s"}," has died ",{"bold":true,"color":"dark_aqua","score":{"name":"@s","objective":"DeathCount"}}," times"]
execute as @a[scores={DeathFlag=1},tag=mg.flw] if score @s DeathCount matches 1000.. run tellraw @a[tag=mg.flw] [{"selector":"@s"}," has died ",{"bold":true,"underlined":true,"color":"dark_red","score":{"name":"@s","objective":"DeathCount"}}," times... God bless them"]

execute if entity @a[tag=trial_well,tag=mg.flw] as @a[scores={DeathFlag=1},tag=mg.flw] run function game:trial_well_respawn

return 1
