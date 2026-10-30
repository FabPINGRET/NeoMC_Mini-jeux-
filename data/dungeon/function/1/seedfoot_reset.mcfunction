tag @a[tag=mg.flw] remove seedfoot
setblock -9932 191 303 minecraft:stone_pressure_plate
fill -9931 199 317 -9933 199 315 air
setblock -9932 199 316 minecraft:green_shulker_box[facing=down]{components:{},lock:{components:{"minecraft:custom_name":'"Ximglie"'}}}
setblock -9932 191 316 air
fill -9925 190 320 -9939 190 306 azalea_leaves[persistent=true] replace minecraft:flowering_azalea_leaves
fill -9939 191 306 -9925 192 320 air replace minecraft:flowering_azalea_leaves
setblock -9932 189 327 air
scoreboard players set sop_timer_1 Countdown -1
execute as @a[tag=mg.flw] at @s run playsound minecraft:zelda.error master @s ~ ~ ~ 1 1 1
