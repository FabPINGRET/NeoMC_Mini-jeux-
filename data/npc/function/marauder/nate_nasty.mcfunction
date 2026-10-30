execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Nate Nasty","color":"aqua"},{"text":"> A little while ago, some ","color":"white"},{"text":"strangers ","color":"yellow"},{"text":"came aboard the Abscondence. They talked privately to the captain for a while, then left. I think they must have given him something.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
