execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Keriv","color":"aqua"},{"text":"> I fish up random garbage all the time. If you lose any key items,","color":"white"},{"text":" specifically items that you find in dungeons","color":"green"},{"text":", chances are I'll fish them up somewhere and I'll put them in my root cellar for ya.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
