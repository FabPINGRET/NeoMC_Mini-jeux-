execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Wrubby","color":"light_purple"},{"text":"> The vat here is pure moldsap, tapped from the stems of mature ","color":"white"},{"text":"Moldsap Mushrooms","color":"light_purple"},{"text":". When boiled down, the it becomes a thick, pungent rotsyrup we use to sweeten our food and pour over our gummy pancakes! Oh, you just want to know where other Glooblins go at night? I'd check the ","color":"white"},{"text":"aviary","color":"light_purple"},{"text":".","color":"white"}]

scoreboard players set nightblin_7 bool 1
execute if score slime_man Story matches 2 if score nightblin_1 bool matches 1 if score nightblin_2 bool matches 1 if score nightblin_3 bool matches 1 if score nightblin_4 bool matches 1 if score nightblin_5 bool matches 1 if score nightblin_6 bool matches 1 if score nightblin_7 bool matches 1 run scoreboard players set slime_man Story 3

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
