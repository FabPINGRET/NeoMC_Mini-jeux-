execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Pluu","color":"light_purple"},{"text":"> I've never seen anything quite like this portal. I can almost see alien-looking trees on the other side... weird. I know one of the other Glooblins doesn't like to risk running into monsters at night, so he just ","color":"white"},{"text":"goes home","color":"light_purple"},{"text":".","color":"white"}]

scoreboard players set nightblin_4 bool 1
execute if score slime_man Story matches 2 if score nightblin_1 bool matches 1 if score nightblin_2 bool matches 1 if score nightblin_3 bool matches 1 if score nightblin_4 bool matches 1 if score nightblin_5 bool matches 1 if score nightblin_6 bool matches 1 if score nightblin_7 bool matches 1 run scoreboard players set slime_man Story 3

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
