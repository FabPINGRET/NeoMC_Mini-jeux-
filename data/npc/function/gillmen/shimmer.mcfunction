execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute if score bubble_lake Story matches 0..2 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Shimmer","color":"yellow"},{"text":"> You're just in time. The tide’s about to turn, but we’re stretched too thin for a full assault. The monstrous ","color":"white"},{"text":"Lake Freaks","color":"dark_green"},{"text":" keep appearing, created by their horrible ","color":"white"},{"text":"Supreme","color":"dark_green"},{"text":". ","color":"white"},{"text":"Kill all of them","color":"aqua"},{"text":", and it’ll surface. When it does, ","color":"white"},{"text":"destroy it","color":"aqua"},{"text":". Do that, and we reclaim ","color":"white"},{"text":"Bubble Lake ","color":"blue"},{"text":"for good.","color":"white"}]
execute if score bubble_lake Story matches 0..2 run setblock -108 40 173 minecraft:redstone_block

execute if score bubble_lake Story matches 3 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Shimmer","color":"yellow"},{"text":"> The ","color":"white"},{"text":"Lake Freaks","color":"dark_green"},{"text":" are dead thanks to you, but their ","color":"white"},{"text":"Supreme","color":"dark_green"},{"text":" is still out there.","color":"white"}]

execute if score bubble_lake Story matches 4 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Shimmer","color":"yellow"},{"text":"> The ","color":"white"},{"text":"Lake Freaks","color":"dark_green"},{"text":" are dead thanks to you. The worst days are behind us.","color":"white"}]


execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run kill @n[tag=quest_marker,distance=..3]

execute if score bubble_lake Story matches 1 run scoreboard players set bubble_lake Story 2

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
