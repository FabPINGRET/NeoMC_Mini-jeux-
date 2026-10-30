execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.vex.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1

execute if score funeral_chapel bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Folded Threnodist","color":"dark_purple"},{"text":"> ... Uh, nice try. Come back later.","color":"white","bold":false}]


execute if score funeral_chapel bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] if entity @a[distance=10..,gamemode=!spectator,tag=mg.flw] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Folded Threnodist","color":"dark_purple"},{"text":"> ... Everyone here first...","color":"white","bold":false}]

execute if score funeral_chapel bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] if entity @a[distance=..10,gamemode=!spectator,tag=mg.flw] unless entity @a[distance=10..,gamemode=!spectator,tag=mg.flw] run function npc:overworld_cutscene/threnodist/0

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
