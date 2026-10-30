tag @a[tag=mg.flw] remove seedfoot
setblock -9932 179 222 minecraft:stone_pressure_plate

fill -9898 197 202 -9900 197 200 minecraft:barrier replace #minecraft:shulker_boxes
fill -9954 194 200 -9956 194 202 minecraft:barrier replace #minecraft:shulker_boxes
fill -9912 192 191 -9910 192 189 minecraft:barrier replace #minecraft:shulker_boxes
fill -9947 198 223 -9945 198 221 minecraft:barrier replace #minecraft:shulker_boxes
fill -9910 194 213 -9908 194 211 minecraft:barrier replace #minecraft:shulker_boxes
fill -9940 191 204 -9938 191 206 minecraft:barrier replace #minecraft:shulker_boxes
setblock -9899 197 201 minecraft:green_shulker_box[facing=down]{components:{},lock:{components:{"minecraft:custom_name":'"Ximglie"'}}}
setblock -9955 194 201 minecraft:green_shulker_box[facing=down]{components:{},lock:{components:{"minecraft:custom_name":'"Ximglie"'}}}
setblock -9911 192 190 minecraft:green_shulker_box[facing=down]{components:{},lock:{components:{"minecraft:custom_name":'"Ximglie"'}}}
setblock -9946 198 222 minecraft:green_shulker_box[facing=down]{components:{},lock:{components:{"minecraft:custom_name":'"Ximglie"'}}}
setblock -9909 194 212 minecraft:green_shulker_box[facing=down]{components:{},lock:{components:{"minecraft:custom_name":'"Ximglie"'}}}
setblock -9939 191 205 minecraft:green_shulker_box[facing=down]{components:{},lock:{components:{"minecraft:custom_name":'"Ximglie"'}}}
setblock -9899 179 201 air
setblock -9955 179 201 air
setblock -9911 179 190 air
setblock -9946 179 222 air
setblock -9909 179 212 air
setblock -9939 179 205 air

fill -9951 178 218 -9903 178 177 minecraft:azalea_leaves[persistent=true] replace minecraft:flowering_azalea_leaves
fill -9951 179 218 -9903 180 177 air replace minecraft:flowering_azalea_leaves

execute as @a[tag=mg.flw] at @s run playsound minecraft:zelda.error master @s ~ ~ ~ 1 1 1

fill -9951 179 203 -9951 180 199 air replace minecraft:orange_stained_glass
fill -9913 179 192 -9909 180 188 air replace minecraft:yellow_stained_glass
fill -9944 180 218 -9948 179 218 air replace minecraft:lime_stained_glass
fill -9911 179 214 -9907 180 210 air replace minecraft:light_blue_stained_glass
fill -9937 179 207 -9941 180 203 air replace minecraft:purple_stained_glass
