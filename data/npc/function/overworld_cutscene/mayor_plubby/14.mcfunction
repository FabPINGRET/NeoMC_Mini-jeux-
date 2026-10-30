execute as @n[tag=mayor_plubby,distance=0..] at @s run tp @s ~ ~ ~ 0 0

execute positioned 10383 59 -222 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2

execute positioned 10383 59 -222 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mayor Plubby","color":"light_purple"},{"text":"> Wow, how exciting! You might get to be his sidekick! Feel free to ask the Glooblins if they've seen where any of their neighbors go at night. I'm sure you'll be able to figure it out. Good luck!","color":"white"}]

scoreboard players set slime_man Story 2
tag @a[tag=mg.flw] remove cutscene
tag @a[tag=mg.flw] remove no_warp

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
