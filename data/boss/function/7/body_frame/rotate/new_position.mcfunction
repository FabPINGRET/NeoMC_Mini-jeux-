#tellraw @p ["Current Dir: ",{"score":{"name":"boss:st_facing_dir","objective":"Value"}}]
execute store result score boss:st_facing_target Value run random value 4..12
#tellraw @p ["Premath Target: ",{"score":{"name":"boss:st_facing_target","objective":"Value"}}]
scoreboard players operation boss:st_facing_target Value += boss:st_facing_dir Value
#tellraw @p ["Precycle Target: ",{"score":{"name":"boss:st_facing_target","objective":"Value"}}]
execute if score boss:st_facing_target Value >= 15 Value run scoreboard players operation boss:st_facing_target Value -= 15 Value
#tellraw @p ["Final Target: ",{"score":{"name":"boss:st_facing_target","objective":"Value"}}]

execute store result score boss:st_facing_dir bool run random value 0..1
execute if score boss:st_facing_dir bool matches 0 run setblock -10448 -48 -358 minecraft:redstone_block
execute if score boss:st_facing_dir bool matches 1 run setblock -10448 -48 -360 minecraft:redstone_block

playsound minecraft:block.grindstone.use hostile @a[tag=mg.flw] -10473 -21 -378 3 0.5
playsound minecraft:block.campfire.crackle hostile @a[tag=mg.flw] -10473 -21 -378 2 2
