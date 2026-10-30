bossbar set boss:dark_eebo value 6
bossbar set boss:dark_eebo color green
bossbar set boss:dark_eebo players
scoreboard players set boss:deebo BossHealth 6

kill @e[tag=smearblin,distance=0..]

scoreboard players set deebo_painting Value 0
scoreboard players set deebo_lastattack Value 0
function boss:mini/dark_eebo/reset_marker_rotation

fill -11539 187 -190 -11531 187 -176 minecraft:fire replace soul_fire strict

execute as @e[tag=deebo,distance=0..] run data modify entity @s item.components."minecraft:custom_model_data".strings[] set value "1"
setblock -11532 187 -183 minecraft:player_head[powered=false,rotation=12]{components:{},profile:{properties:[{name:"textures",value:"ewogICJ0aW1lc3RhbXAiIDogMTc2NzExNjU0NTE2MCwKICAicHJvZmlsZUlkIiA6ICJhODgyMzAzMDVkOWY0ODRiYjNjNjc2OTg1OTYxYjc2YSIsCiAgInByb2ZpbGVOYW1lIiA6ICJMb3JkRHJld3BpY3VzIiwKICAic2lnbmF0dXJlUmVxdWlyZWQiIDogdHJ1ZSwKICAidGV4dHVyZXMiIDogewogICAgIlNLSU4iIDogewogICAgICAidXJsIiA6ICJodHRwOi8vdGV4dHVyZXMubWluZWNyYWZ0Lm5ldC90ZXh0dXJlL2MwNDUzZWZiNjU0M2MxZjQyYTIxOGIwNjEwMzYxOTYyZjg0M2Y2YjY3NzJiOTJmYmI3ZTE4MDkxMjM5MzA2ZWIiCiAgICB9CiAgfQp9"}]}}
setblock -11532 187 -182 minecraft:oak_sign[rotation=4,waterlogged=false]{back_text:{color:"black",has_glowing_text:0b,messages:["","","",""]},components:{},front_text:{color:"black",has_glowing_text:0b,messages:["","Talk to the","Creature",""]},is_waxed:0b}
setblock -11533 187 -182 minecraft:stone_button[face=floor,facing=east,powered=false]
setblock -11538 187 -183 minecraft:blue_carpet
fill -11545 187 -183 -11545 188 -183 minecraft:air

tag @e[tag=deebo,distance=0..] remove active
tag @e[tag=deebo_marker,distance=0..] remove active
schedule clear floaty:sched/boss/mini/dark_eebo/pick_attack

setblock -11552 173 -169 air
setblock -11551 173 -171 air
setblock -11549 173 -173 air
setblock -11552 173 -175 air
setblock -11552 173 -179 air
setblock -11549 173 -171 black_wool
setblock -11547 173 -171 black_wool

tp @n[tag=deebo_stand,distance=0..] -11514 187 -183
