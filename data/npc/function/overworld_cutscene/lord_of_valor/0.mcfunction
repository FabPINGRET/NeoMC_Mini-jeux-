#execute positioned 10180 40 -237 at @e[sort=nearest,limit=1,tag=npc] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a ~ ~ ~ 1 1.2
execute positioned 10027 94 -101 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Water","color":"blue"},{"text":"> Who are you who comes before us, friend of the ","color":"white"},{"text":"Hero of the Floaty Isles","color":"gold"},{"text":"?","color":"white"},{"text":" ⇒","color":"light_purple"}]

function music:end
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
tag @a[tag=mg.flw] add no_warp

execute as @n[tag=lord_of_flame,distance=0..] at @s facing entity @n[tag=lord_of_valor,distance=0..] eyes run tp @s ~ ~ ~ ~ ~
execute as @n[tag=lord_of_forest,distance=0..] at @s facing entity @n[tag=lord_of_valor,distance=0..] eyes run tp @s ~ ~ ~ ~ ~
execute as @n[tag=lord_of_spores,distance=0..] at @s facing entity @n[tag=lord_of_valor,distance=0..] eyes run tp @s ~ ~ ~ ~ ~
execute as @n[tag=lord_of_ice,distance=0..] at @s facing entity @n[tag=lord_of_valor,distance=0..] eyes run tp @s ~ ~ ~ ~ ~
execute as @n[tag=lord_of_water,distance=0..] at @s facing entity @n[tag=lord_of_valor,distance=0..] eyes run tp @s ~ ~ ~ ~ ~
setblock 10029 95 -95 minecraft:player_head[powered=false,rotation=13]{components:{},profile:{id:[I;342755571,-1933686352,-1272836348,-1012528262],name:"",properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNDA1ZWU5YzY0ZDRiNjYyMTE5ZjVjNTczNTU2MjMyNzQwMDE4NTgyMjM5YjA5OTNlZTZjYTMyNTJmZmVlMWY2NyJ9fX0="}]}}

setblock 10017 94 -89 minecraft:deepslate_brick_slab[type=bottom,waterlogged=false]
setblock 10016 94 -94 minecraft:deepslate_brick_slab[type=bottom,waterlogged=false]
setblock 10018 94 -100 minecraft:deepslate_brick_slab[type=bottom,waterlogged=false]
setblock 10026 94 -100 minecraft:deepslate_brick_slab[type=bottom,waterlogged=false]
setblock 10028 94 -94 minecraft:deepslate_brick_slab[type=bottom,waterlogged=false]
setblock 10027 94 -89 minecraft:deepslate_brick_slab[type=bottom,waterlogged=false]
fill 10015 95 -89 10028 95 -101 air replace minecraft:oak_wall_sign
setblock 10022 93 -86 deepslate_bricks

scoreboard players set lord_of_valor Story 3

schedule function floaty:sched/npc/overworld_cutscene/lord_of_valor/1 9s replace
