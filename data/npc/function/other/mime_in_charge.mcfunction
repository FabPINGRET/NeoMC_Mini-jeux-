execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ unless entity @a[distance=9..,gamemode=!spectator,tag=mg.flw] if entity @a[distance=..9,gamemode=!spectator,tag=mg.flw] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mime in Charge","color":"white"},{"text":"> ","color":"white"},{"text":"!","bold":true,"italic":true}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ unless entity @a[distance=9..,gamemode=!spectator,tag=mg.flw] if entity @a[distance=..9,gamemode=!spectator,tag=mg.flw] run setblock -11668 149 -337 minecraft:redstone_block
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ unless entity @a[distance=9..,gamemode=!spectator,tag=mg.flw] if entity @a[distance=..9,gamemode=!spectator,tag=mg.flw] positioned -11648 165 -350 run kill @n[tag=boss_marker,distance=..3]


execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if entity @a[distance=9..,gamemode=!spectator,tag=mg.flw] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mime in Charge","color":"white"},{"text":"> ... ","color":"white"},{"text":"(He motions to you that everyone should be here)","color":"gray","italic":true}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
