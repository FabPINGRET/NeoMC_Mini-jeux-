execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Grandpa the Wise","color":"yellow"},{"text":"> You solved my naked riddle! Teehee! If you want, you can take one of my ","color":"white"},{"text":"scales","color":"blue"},{"text":" as a special reward. Grandpa the Wise is proud of you.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
