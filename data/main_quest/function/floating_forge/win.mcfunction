playsound minecraft:zelda.secret master @a[tag=mg.flw] 93 77 225 1 1

kill @e[tag=blade_metal,distance=0..]
kill @e[tag=blade_metal_marker,distance=0..]
kill @e[tag=blade_metal_loc,distance=0..]
kill @e[tag=blade_metal_dest,distance=0..]
setblock 87 70 216 minecraft:air

setblock 93 76 217 air

setblock 93 76 222 minecraft:trapped_chest[facing=north,type=single,waterlogged=false]{Items:[{Slot:13b,components:{"minecraft:custom_name":"Imperishable Blade","minecraft:tooltip_display":{hidden_components:["minecraft:unbreakable"]},"minecraft:unbreakable":{}},count:1,id:"minecraft:iron_sword"}]}
