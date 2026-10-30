execute if score banana_of_temptation bool matches 0 run scoreboard players set banana_of_temptation bool 1
execute if score banana_of_temptation bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[gamemode=!spectator,tag=mg.flw] if items entity @s weapon.mainhand flint[minecraft:custom_model_data={strings:['30']}] run scoreboard players set banana_of_temptation bool 2

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[gamemode=!spectator,tag=mg.flw] if items entity @s weapon.mainhand flint[minecraft:custom_model_data={strings:['30']}] run item replace entity @s weapon.mainhand with air

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.fox.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute if score banana_of_temptation bool matches 0..1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"24k Monky","color":"yellow"},{"text":"> OOOH EEEEH EEEE AHHHH!! (I'm looking for a giant, ","color":"white"},{"text":"golden banana","color":"yellow"},{"text":" to complete my collection of treasures! It would really tie the room together, you know? If I had one, I'd be","color":"white"},{"text":" such a very happy monkey","color":"red"},{"text":"! I'd just have to be careful to always ","color":"white"},{"text":"have my back to it","color":"green"},{"text":" anytime I touched it...)","color":"white"}]

execute if score banana_of_temptation bool matches 2 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"24k Monky","color":"yellow"},{"text":"> OOO OOOOH AAHHH AHHHH AHHH!! (This is the perfect","color":"white"},{"text":" banana","color":"yellow"},{"text":", thank you! I've gotta be the ","color":"white"},{"text":"happiest monkey alive","color":"red"},{"text":" right now. Life is pointless without gold.)","color":"white"}]

execute if score banana_of_temptation bool matches 2 run clone 10132 198 1303 10132 200 1305 10132 190 1303
execute if score banana_of_temptation bool matches 2 run setblock 10131 185 1302 minecraft:stone
execute if score banana_of_temptation bool matches 2 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1.75 ~ run particle minecraft:heart ~ ~ ~ 0.3 0.3 0.3 0 10 force
execute if score banana_of_temptation bool matches 2 run setblock 10125 185 1305 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
