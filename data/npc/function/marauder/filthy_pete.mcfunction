execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Filthy Pete","color":"aqua"},{"text":"> We used to have a hideout on the ","color":"white"},{"text":"Isle of Ice","color":"aqua"},{"text":" some years back. We haven't lived there in a while, but some of our crew is doing a final sweep of it before we go, in case we left anything important.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
