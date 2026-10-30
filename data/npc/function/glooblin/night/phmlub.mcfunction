execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Phmlub","color":"light_purple"},{"text":"> I'm taking inventory for the night. I use this room as extra storage for my Spore Store. I know there's a Glooblin who goes to the ","color":"white"},{"text":"Sugar House ","color":"light_purple"},{"text":"around now.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 

scoreboard players set nightblin_3 bool 1
execute if score slime_man Story matches 2 if score nightblin_1 bool matches 1 if score nightblin_2 bool matches 1 if score nightblin_3 bool matches 1 if score nightblin_4 bool matches 1 if score nightblin_5 bool matches 1 if score nightblin_6 bool matches 1 if score nightblin_7 bool matches 1 run scoreboard players set slime_man Story 3
