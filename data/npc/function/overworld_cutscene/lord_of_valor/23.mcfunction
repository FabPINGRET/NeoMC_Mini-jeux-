function music:end
tag @a[tag=mg.flw] remove no_warp
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 0

setblock 10031 91 -101 air

execute as @n[tag=lord_of_flame,distance=0..] at @s run tp @s ~ ~ ~ -90 0
execute as @n[tag=lord_of_forest,distance=0..] at @s run tp @s ~ ~ ~ 90 0
execute as @n[tag=lord_of_spores,distance=0..] at @s run tp @s ~ ~ ~ -90 0
setblock 10029 95 -95 minecraft:player_head[powered=false,rotation=12]{components:{},profile:{id:[I;342755571,-1933686352,-1272836348,-1012528262],name:"",properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNDA1ZWU5YzY0ZDRiNjYyMTE5ZjVjNTczNTU2MjMyNzQwMDE4NTgyMjM5YjA5OTNlZTZjYTMyNTJmZmVlMWY2NyJ9fX0="}]}}
execute as @n[tag=lord_of_ice,distance=0..] at @s run tp @s ~ ~ ~ 0 0
execute as @n[tag=lord_of_water,distance=0..] at @s run tp @s ~ ~ ~ 0 0

setblock 10026 95 -100 minecraft:oak_wall_sign[facing=south,waterlogged=false]{back_text:{color:"black",has_glowing_text:0b,messages:['""','""','""','""']},components:{},front_text:{color:"cyan",has_glowing_text:1b,messages:["","Talk to the","Lord of Water",""]},is_waxed:0b}
setblock 10026 94 -100 minecraft:polished_blackstone_button[face=floor,facing=north,powered=false]
setblock 10023 95 -101 minecraft:oak_wall_sign[facing=south,waterlogged=false]{back_text:{color:"black",has_glowing_text:0b,messages:['""','""','""','""']},components:{},front_text:{color:"yellow",has_glowing_text:1b,messages:["","Talk to the","Lord of Valor",""]},is_waxed:0b}
setblock 10023 94 -101 minecraft:polished_blackstone_button[face=floor,facing=north,powered=false]
setblock 10018 95 -100 minecraft:oak_wall_sign[facing=south,waterlogged=false]{back_text:{color:"black",has_glowing_text:0b,messages:['""','""','""','""']},components:{},front_text:{color:"white",has_glowing_text:1b,messages:["","Talk to the","Lord of Ice",""]},is_waxed:0b}
setblock 10018 94 -100 minecraft:polished_blackstone_button[face=floor,facing=north,powered=false]
setblock 10017 95 -89 minecraft:oak_wall_sign[facing=east,waterlogged=false]{back_text:{color:"black",has_glowing_text:0b,messages:['""','""','""','""']},components:{},front_text:{color:"red",has_glowing_text:1b,messages:["","Talk to the","Lord of Flame",""]},is_waxed:0b}
setblock 10017 94 -89 minecraft:polished_blackstone_button[face=floor,facing=west,powered=false]
setblock 10027 95 -89 minecraft:oak_wall_sign[facing=west,waterlogged=false]{back_text:{color:"black",has_glowing_text:0b,messages:['""','""','""','""']},components:{},front_text:{color:"green",has_glowing_text:1b,messages:["","Talk to the","Lord of Forest",""]},is_waxed:0b}
setblock 10027 94 -89 minecraft:polished_blackstone_button[face=floor,facing=east,powered=false]
setblock 10016 95 -94 minecraft:oak_wall_sign[facing=east,waterlogged=false]{back_text:{color:"black",has_glowing_text:0b,messages:['""','""','""','""']},components:{},front_text:{color:"purple",has_glowing_text:1b,messages:["","Talk to the","Lord of Spores",""]},is_waxed:0b}
setblock 10016 94 -94 minecraft:polished_blackstone_button[face=floor,facing=west,powered=false]
setblock 10028 95 -94 minecraft:oak_wall_sign[facing=west,waterlogged=false]{back_text:{color:"black",has_glowing_text:0b,messages:['""','""','""','""']},components:{},front_text:{color:"light_gray",has_glowing_text:1b,messages:["","Talk to the","Lord of Stone",""]},is_waxed:0b}
setblock 10028 94 -94 minecraft:polished_blackstone_button[face=floor,facing=east,powered=false]

setblock 10022 93 -86 minecraft:ladder[facing=south,waterlogged=false]

schedule function floaty:sched/npc/overworld_cutscene/lord_of_valor/24 2t replace

# open machine
