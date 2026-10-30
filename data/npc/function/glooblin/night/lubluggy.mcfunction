execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lubluggy","color":"light_purple"},{"text":"> These eggs are our future! I watch over them at night to make sure they're ok. If you're looking for where other Glooblins go after dark, I think one goes to their ","color":"white"},{"text":"cellar","color":"light_purple"},{"text":" sometimes.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 

scoreboard players set nightblin_2 bool 1
execute if score slime_man Story matches 2 if score nightblin_1 bool matches 1 if score nightblin_2 bool matches 1 if score nightblin_3 bool matches 1 if score nightblin_4 bool matches 1 if score nightblin_5 bool matches 1 if score nightblin_6 bool matches 1 if score nightblin_7 bool matches 1 run scoreboard players set slime_man Story 3
