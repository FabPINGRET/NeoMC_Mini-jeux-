execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Wrlop","color":"light_purple"},{"text":"> These birds are endangered! The ","color":"white"},{"text":"Lord of Spores","color":"light_purple"},{"text":" built this aviary to keep them safe and let us admire them; a reminder that all life in these woods is precious and worth preserving. Just before I got here, I think I saw another Glooblin standing on a ","color":"white"},{"text":"small island","color":"light_purple"},{"text":" near the other side of the village.","color":"white"}]

scoreboard players set nightblin_6 bool 1
execute if score slime_man Story matches 2 if score nightblin_1 bool matches 1 if score nightblin_2 bool matches 1 if score nightblin_3 bool matches 1 if score nightblin_4 bool matches 1 if score nightblin_5 bool matches 1 if score nightblin_6 bool matches 1 if score nightblin_7 bool matches 1 run scoreboard players set slime_man Story 3

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
