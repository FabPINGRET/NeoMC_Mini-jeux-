execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Slrblap","color":"light_purple"},{"text":"> I stand here sometimes to watch the Orcs. They grunt and snarl and burp and yell, but I think they're really quite sophisticated if you take the time to pay attention to them. Speaking of paying attention, one of my neighbors likes looking at the ","color":"white"},{"text":"Worldgate","color":"yellow"},{"text":" at night.","color":"white"}]

scoreboard players set nightblin_5 bool 1
execute if score slime_man Story matches 2 if score nightblin_1 bool matches 1 if score nightblin_2 bool matches 1 if score nightblin_3 bool matches 1 if score nightblin_4 bool matches 1 if score nightblin_5 bool matches 1 if score nightblin_6 bool matches 1 if score nightblin_7 bool matches 1 run scoreboard players set slime_man Story 3

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
