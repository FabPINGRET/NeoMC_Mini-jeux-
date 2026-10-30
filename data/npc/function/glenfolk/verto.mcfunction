execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute if block 157 58 23 barrier at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Verto","color":"aqua"},{"text":"> The Armor Dexter went out to pick flowers a long time ago and hasn't been back since. I'm getting a bit worried about him to be honest. I heard something about there being a cave by blue flowers which has an entrance that only appears at","color":"white"},{"text":" night","color":"aqua"},{"text":".","color":"white"}]

execute unless block 157 58 23 barrier at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Verto","color":"aqua"},{"text":"> The Dexter is back open now, glad he's safe.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
