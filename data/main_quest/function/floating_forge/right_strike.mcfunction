fill 88 78 224 90 82 226 air
fill 88 82 223 90 80 223 air
fill 89 81 226 89 79 231 air replace minecraft:acacia_wood

fill 89 80 224 89 78 226 minecraft:netherite_block
fill 88 78 225 90 80 225 minecraft:netherite_block
fill 88 78 224 90 80 226 minecraft:polished_deepslate_wall replace air
fill 89 79 231 89 79 227 minecraft:acacia_wood[axis=z]

#playsound minecraft:item.mace.smash_ground master @a 89 77 225 2 1
playsound minecraft:entity.ravager.step master @a[tag=mg.flw] 89 77 225 1 0.5
playsound minecraft:block.note_block.basedrum master @a[tag=mg.flw] 89 77 225 2 1

schedule function floaty:sched/main_quest/floating_forge/right_raise 19t

tag @n[tag=blade_metal_marker,tag=right,tag=contact,distance=0..] add struck
execute if entity @e[tag=blade_metal_marker,tag=right,tag=struck,distance=0..] run particle minecraft:flame 89 77.5 225 0.5 0 0.5 0.05 20
execute if entity @e[tag=blade_metal_marker,tag=right,tag=struck,distance=0..] run playsound minecraft:block.anvil.place master @a[tag=mg.flw] 89 77 225 0.5 0.5
