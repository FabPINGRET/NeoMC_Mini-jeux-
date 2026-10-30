advancement grant @a[tag=mg.flw] only main_quest:quest_6
scoreboard players set $fla41 mg.fla 1

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute if score Inventory Honeyboost matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> Congrats, you figured it out! Alright sidekick, I'll let you help me. I've opened the way to ","color":"white"},{"text":"Sticky Hollow","color":"light_purple"},{"text":", so when you're ready, I'll meet you inside. The glory of heroicism awaits! Oh, you'll also want to think of a catchy sidekick name, like Moldly or something.","color":"white"}]

execute if score Inventory Honeyboost matches 1 unless score lord_of_valor Story matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> I think you're a fine hero in your own right. Don't worry, you'll always be my favorite sidekick. I just know our heroing paths will cross again someday...","color":"white"}]

execute if score Inventory Honeyboost matches 1 if score lord_of_valor Story matches 1 run function npc:overworld_cutscene/lord_of_valor/slimecave_0

execute positioned 10180 42 -237 run kill @n[tag=quest_marker,distance=..3]

setblock -9773 252 416 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
