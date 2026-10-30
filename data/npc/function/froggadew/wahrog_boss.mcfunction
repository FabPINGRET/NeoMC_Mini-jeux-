execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7

execute positioned -9864 109 556 if entity @a[gamemode=!spectator,distance=6..,tag=mg.flw] run tellraw @a[distance=..6,tag=mg.flw] [{"text":"<"},{"text":"Wahrog the Prophet","color":"#44BBFF"},{"text":"> The space behind your eyes is unruined by crackling! Please, gather ","color":"white"},{"text":"everyone","color":"#44BBFF"},{"text":" here...","color":"white"}]

execute positioned -9864 109 556 if entity @a[gamemode=!spectator,distance=..6,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=6..,tag=mg.flw] run function npc:overworld_cutscene/wahrog/0

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
