execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brglop","color":"light_purple"},{"text":"> It's night, so you know what that means! Sleep time! It really feels like nobody actually sleeps though, I've only ever seen empty beds around here. I'm pretty sure there's a Glooblin at the ","color":"white"},{"text":"nursery","color":"light_purple"},{"text":" right now, can you believe it?","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 

scoreboard players set nightblin_1 bool 1
execute if score slime_man Story matches 2 if score nightblin_1 bool matches 1 if score nightblin_2 bool matches 1 if score nightblin_3 bool matches 1 if score nightblin_4 bool matches 1 if score nightblin_5 bool matches 1 if score nightblin_6 bool matches 1 if score nightblin_7 bool matches 1 run scoreboard players set slime_man Story 3
