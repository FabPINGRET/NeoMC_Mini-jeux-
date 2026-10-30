execute positioned -300 34 -70 run advancement grant @a[distance=..10,tag=mg.flw] only sidequest_2:yommod_start
scoreboard players set yommod_all bool 0

execute positioned -300 34 -70 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2

execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['1']}}}}] as @e[tag=shieldbearer,tag=bird,limit=1,distance=0..] at @s run setblock ~ ~-3 ~ redstone_block
execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['1']}}}}] as @e[tag=shieldbearer,tag=bird,limit=1,distance=0..] at @s run item replace entity @s weapon.mainhand from block ~ ~-2 ~ container.0

execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['2']}}}}] as @e[tag=shieldbearer,tag=beetle,limit=1,distance=0..] at @s run setblock ~ ~-3 ~ redstone_block
execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['2']}}}}] as @e[tag=shieldbearer,tag=beetle,limit=1,distance=0..] at @s run item replace entity @s weapon.mainhand from block ~ ~-2 ~ container.0

execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['3']}}}}] as @e[tag=shieldbearer,tag=waterfall,limit=1,distance=0..] at @s run setblock ~ ~-3 ~ redstone_block
execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['3']}}}}] as @e[tag=shieldbearer,tag=waterfall,limit=1,distance=0..] at @s run item replace entity @s weapon.mainhand from block ~ ~-2 ~ container.0

execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['4']}}}}] as @e[tag=shieldbearer,tag=sun,limit=1,distance=0..] at @s run setblock ~ ~-3 ~ redstone_block
execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['4']}}}}] as @e[tag=shieldbearer,tag=sun,limit=1,distance=0..] at @s run item replace entity @s weapon.mainhand from block ~ ~-2 ~ container.0

execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['5']}}}}] as @e[tag=shieldbearer,tag=cross,limit=1,distance=0..] at @s run setblock ~ ~-3 ~ redstone_block
execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['5']}}}}] as @e[tag=shieldbearer,tag=cross,limit=1,distance=0..] at @s run item replace entity @s weapon.mainhand from block ~ ~-2 ~ container.0

execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['6']}}}}] as @e[tag=shieldbearer,tag=eye,limit=1,distance=0..] at @s run setblock ~ ~-3 ~ redstone_block
execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['6']}}}}] as @e[tag=shieldbearer,tag=eye,limit=1,distance=0..] at @s run item replace entity @s weapon.mainhand from block ~ ~-2 ~ container.0

execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['7']}}}}] as @e[tag=shieldbearer,tag=frozen,limit=1,distance=0..] at @s run setblock ~ ~-3 ~ redstone_block
execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['7']}}}}] as @e[tag=shieldbearer,tag=frozen,limit=1,distance=0..] at @s run item replace entity @s weapon.mainhand from block ~ ~-2 ~ container.0

execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['8']}}}}] as @e[tag=shieldbearer,tag=alien,limit=1,distance=0..] at @s run setblock ~ ~-3 ~ redstone_block
execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['8']}}}}] as @e[tag=shieldbearer,tag=alien,limit=1,distance=0..] at @s run item replace entity @s weapon.mainhand from block ~ ~-2 ~ container.0

execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['9']}}}}] as @e[tag=shieldbearer,tag=familiar,limit=1,distance=0..] at @s run setblock ~ ~-3 ~ redstone_block
execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['9']}}}}] as @e[tag=shieldbearer,tag=familiar,limit=1,distance=0..] at @s run item replace entity @s weapon.mainhand from block ~ ~-2 ~ container.0

execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['10']}}}}] as @e[tag=shieldbearer,tag=weird,limit=1,distance=0..] at @s run setblock ~ ~-3 ~ redstone_block
execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['10']}}}}] as @e[tag=shieldbearer,tag=weird,limit=1,distance=0..] at @s run item replace entity @s weapon.mainhand from block ~ ~-2 ~ container.0

execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['11']}}}}] as @e[tag=shieldbearer,tag=steadfast,limit=1,distance=0..] at @s run setblock ~ ~-3 ~ redstone_block
execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['11']}}}}] as @e[tag=shieldbearer,tag=steadfast,limit=1,distance=0..] at @s run item replace entity @s weapon.mainhand from block ~ ~-2 ~ container.0

execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['12']}}}}] as @e[tag=shieldbearer,tag=reptile,limit=1,distance=0..] at @s run setblock ~ ~-3 ~ redstone_block
execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['12']}}}}] as @e[tag=shieldbearer,tag=reptile,limit=1,distance=0..] at @s run item replace entity @s weapon.mainhand from block ~ ~-2 ~ container.0

execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['13']}}}}] as @e[tag=shieldbearer,tag=fungal,limit=1,distance=0..] at @s run setblock ~ ~-3 ~ redstone_block
execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['13']}}}}] as @e[tag=shieldbearer,tag=fungal,limit=1,distance=0..] at @s run item replace entity @s weapon.mainhand from block ~ ~-2 ~ container.0

execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['14']}}}}] as @e[tag=shieldbearer,tag=scratch,limit=1,distance=0..] at @s run setblock ~ ~-3 ~ redstone_block
execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['14']}}}}] as @e[tag=shieldbearer,tag=scratch,limit=1,distance=0..] at @s run item replace entity @s weapon.mainhand from block ~ ~-2 ~ container.0

execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['15']}}}}] as @e[tag=shieldbearer,tag=synthetic,limit=1,distance=0..] at @s run setblock ~ ~-3 ~ redstone_block
execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['15']}}}}] as @e[tag=shieldbearer,tag=synthetic,limit=1,distance=0..] at @s run item replace entity @s weapon.mainhand from block ~ ~-2 ~ container.0

execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['16']}}}}] as @e[tag=shieldbearer,tag=fountain,limit=1,distance=0..] at @s run setblock ~ ~-3 ~ redstone_block
execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['16']}}}}] as @e[tag=shieldbearer,tag=fountain,limit=1,distance=0..] at @s run item replace entity @s weapon.mainhand from block ~ ~-2 ~ container.0

execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['17']}}}}] as @e[tag=shieldbearer,tag=noxious,limit=1,distance=0..] at @s run setblock ~ ~-3 ~ redstone_block
execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['17']}}}}] as @e[tag=shieldbearer,tag=noxious,limit=1,distance=0..] at @s run item replace entity @s weapon.mainhand from block ~ ~-2 ~ container.0

execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['18']}}}}] as @e[tag=shieldbearer,tag=pathogen,limit=1,distance=0..] at @s run setblock ~ ~-3 ~ redstone_block
execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide",components:{"minecraft:custom_model_data":{strings:['18']}}}}] as @e[tag=shieldbearer,tag=pathogen,limit=1,distance=0..] at @s run item replace entity @s weapon.mainhand from block ~ ~-2 ~ container.0

execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide"}}] if blocks -294 30 -77 -294 30 -65 -292 30 -77 all if blocks -306 30 -77 -306 30 -65 -292 30 -77 all if block -296 30 -63 redstone_block if block -298 30 -63 redstone_block if block -302 30 -63 redstone_block if block -304 30 -63 redstone_block run scoreboard players set yommod_all bool 1

execute if block -300 30 -63 minecraft:redstone_block positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] unless entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide"}}] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Yommod","color":"dark_aqua"},{"text":"> Good day, Hero. Welcome to my shield workshop! Feel free to decorate your gear and make other Dwarves jealous. I hope you like the special ","color":"white"},{"text":"Royal Shield ","color":"blue"},{"text":"pattern I developed in your honor!","color":"white"}]
execute unless block -300 30 -63 minecraft:redstone_block positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] unless entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide"}}] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Yommod","color":"dark_aqua"},{"text":"> Good day, Hero. Welcome to my brand new shield workshop! ","color":"white"},{"text":"Shield patterns","color":"aqua"},{"text":" are a fun way to decorate your gear and make other Dwarves jealous. I want to collect them all, so if you find any, please consider donating them. If you bring me a pattern from every corner of the world, I'll give you something","color":"white"},{"text":" really, really cool","color":"dark_purple"},{"text":" I found!","color":"white"}]


execute if score yommod_all bool matches 0 positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide"}}] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Yommod","color":"dark_aqua"},{"text":"> A new shield pattern! This is great, I'll add it to my collection! I'll put it on your shield free of charge if you want.","color":"white"}]

execute if score yommod_all bool matches 1 positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide"}}] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Yommod","color":"dark_aqua"},{"text":"> That's the last shield pattern I needed! This is fantastic! Here, take the ","color":"white"},{"text":"really, really cool ","color":"dark_purple"},{"text":"thing I told you about. And finally, to cap off my collection, I'm unveiling the special ","color":"white"},{"text":"Royal Shield ","color":"blue"},{"text":"pattern I developed in your honor. Many thanks, hero!","color":"white"}]


execute if score yommod_all bool matches 0 positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide"}}] run playsound minecraft:zelda.itemget master @a[tag=mg.flw] ~ ~ ~ 1 1
execute if score yommod_all bool matches 1 positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide"}}] run playsound minecraft:zelda.secret master @a[tag=mg.flw] ~ ~ ~ 1 1
execute if score yommod_all bool matches 1 positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide"}}] run advancement grant @a[tag=mg.flw] only sidequest_2:yommod_complete
execute if score yommod_all bool matches 1 positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide"}}] run scoreboard players set $fla39 mg.fla 1
execute if score yommod_all bool matches 1 positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide"}}] as @e[tag=shieldbearer,tag=royal,limit=1,distance=0..] at @s run setblock ~ ~-3 ~ redstone_block 
execute if score yommod_all bool matches 1 positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide"}}] as @e[tag=shieldbearer,tag=royal,limit=1,distance=0..] at @s run item replace entity @s weapon.mainhand from block ~ ~-2 ~ container.0 
execute if score yommod_all bool matches 1 positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide"}}] run setblock -299 33 -70 minecraft:chest[facing=north,type=single,waterlogged=false]{Items:[{Slot:13b,components:{"minecraft:custom_model_data":{strings:["9"]},"minecraft:custom_name":{bold:1b,color:"light_purple",text:"Moon Queen's Embrace"}},count:1,id:"minecraft:flint"}],components:{}}

execute positioned -300 34 -70 as @p[gamemode=!spectator,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide"}}] run item replace entity @s weapon.mainhand with air


#execute as @p[gamemode=!spectator] if entity @s[nbt={SelectedItem:{id:"minecraft:rabbit_hide"}}] run item replace entity @s weapon.mainhand from block ~ ~-1 ~ container.0
#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
