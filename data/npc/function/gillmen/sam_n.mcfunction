execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Sam N.","color":"yellow"},{"text":"> Everyone has their own problems happening in their own lands, so people don't really want to help each other right now. It's sad.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
