execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.strider.happy neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Nozh-Xel","color":"light_purple"},{"text":"> Have you heard it? A ","color":"white"},{"text":"dark threnody","color":"dark_purple"},{"text":" from somewhere in Limbohold. No matter where we look, we cannot find its source. It's as if ","color":"white"},{"text":"dread","color":"dark_purple"},{"text":" itself sings a lament for the approaching death of its prey...","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
