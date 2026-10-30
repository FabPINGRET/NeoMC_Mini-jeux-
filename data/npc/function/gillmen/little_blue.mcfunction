execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 0.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Little Blue","color":"blue"},{"text":"> You want to go to the ","color":"white"},{"text":"Lake","color":"blue"},{"text":"? The button over there will open the gate, but be careful! Also, if you can't ","color":"white"},{"text":"breathe water","color":"blue"},{"text":", it would be wise to stop at the shrine in the other room before you go.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
