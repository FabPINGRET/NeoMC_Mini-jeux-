execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lissy","color":"aqua"},{"text":"> 'Ave you found any magic spells? Oi've 'eard that ","color":"white"},{"text":"casting a spell makes you really 'ungry","color":"green"},{"text":"! Always 'elps to 'ave somethin' to eat.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
