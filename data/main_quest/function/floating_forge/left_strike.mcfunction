fill 96 78 224 98 82 226 air
fill 96 82 223 98 80 223 air
fill 97 81 226 97 79 231 air replace minecraft:acacia_wood

fill 97 80 224 97 78 226 minecraft:netherite_block
fill 96 78 225 98 80 225 minecraft:netherite_block
fill 96 78 224 98 80 226 minecraft:polished_deepslate_wall replace air
fill 97 79 231 97 79 227 minecraft:acacia_wood[axis=z]

#playsound minecraft:item.mace.smash_ground master @a 97 77 225 2 1
playsound minecraft:entity.ravager.step master @a[tag=mg.flw] 97 77 225 1 0.5
playsound minecraft:block.note_block.basedrum master @a[tag=mg.flw] 97 77 225 2 1

schedule function floaty:sched/main_quest/floating_forge/left_raise 19t

tag @n[tag=blade_metal_marker,tag=left,tag=contact,distance=0..] add struck
execute if entity @e[tag=blade_metal_marker,tag=left,tag=struck,distance=0..] run particle minecraft:flame 97 77.5 225 0.5 0 0.5 0.05 20
execute if entity @e[tag=blade_metal_marker,tag=left,tag=struck,distance=0..] run playsound minecraft:block.anvil.place master @a[tag=mg.flw] 97 77 225 0.5 0.5
