execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Benn","color":"aqua"},{"text":"> Heard somethin' about a","color":"white"},{"text":" speakeasy","color":"aqua"},{"text":" around here? Apparently the hidden entrance is supposed to keep out anyone too dumb to be a member, and I can't find it anywhere, so I don't know what that says about me.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
