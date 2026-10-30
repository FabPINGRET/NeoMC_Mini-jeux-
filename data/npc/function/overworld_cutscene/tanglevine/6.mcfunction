execute positioned 10468 60 119 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10468 60 119 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> Oh... You again? Well, this is unexpected.","color":"white"},{"text":" ⇒","color":"light_purple"}]

setblock 10470 54 120 redstone_block

schedule function floaty:sched/npc/overworld_cutscene/tanglevine/7 4s

execute as @a[tag=mg.flw] at @s run playsound minecraft:soundtrack.slime_man_fail record @s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
