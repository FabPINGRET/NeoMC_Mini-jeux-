execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:item.armor.equip_leather neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute if score mr_nippy bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Scarecrow","color":"gold"},{"text":"> ","color":"white"},{"text":"...\nMy fate is to be a scarecrow. Is my scariness too offensive that I might never befriend a crow instead?\n\n... I can only hope it isn't so. Go and be grateful for your kind face.","color":"gray","italic":true}]

execute if score mr_nippy bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Scarecrow","color":"gold"},{"text":"> ","color":"white"},{"text":"...\nA place? Where I could meet... friends? Say no more.","color":"gray","italic":true}]
execute if score mr_nippy bool matches 1 run setblock 7 52 -136 redstone_block


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
