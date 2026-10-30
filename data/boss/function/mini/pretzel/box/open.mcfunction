setblock -10340 89 446 minecraft:barrel[facing=up,open=true]{Items:[],components:{},lock:{components:{"minecraft:custom_name":'"Ximglie"'}}}
summon item_display -10340 91.7 446 {NoGravity:1b,Silent:1b,billboard:"center",interpolation_duration:20,Tags:["pretzel_item"],brightness:{sky:15,block:15},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[3f,3f,3f]},item:{id:"minecraft:netherite_scrap",count:1}}
data modify entity @n[tag=pretzel_item,distance=0..] transformation.translation set value [0.0f, 1.2f, 0.0f]
scoreboard players set pretzel_box_tick Value 1
setblock -10355 61 459 redstone_block
particle minecraft:dust_plume -10340 90 446 0.1 0 0.1 0.1 20
playsound minecraft:block.barrel.open block @a[tag=mg.flw] -10340 89 446 1 1
