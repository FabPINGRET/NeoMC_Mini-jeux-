execute at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.wither_skeleton.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Qskentic","color":"dark_aqua"},{"text":"> Your lungs, they fill and empty. Is this some trick? Do you truly live?","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
