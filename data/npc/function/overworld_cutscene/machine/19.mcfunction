particle minecraft:flame 10396 172 -8 0.4 0.5 0.4 0 50
particle minecraft:totem_of_undying 10396 172 -16 0.4 0.5 0.4 0 50
particle minecraft:cherry_leaves 10392 172 -7 0.4 0.5 0.4 0 50
particle minecraft:egg_crack 10392 172 -17 0.4 0.5 0.4 0 50
particle minecraft:block{block_state:"ice"} 10388 172 -8 0.4 0.5 0.4 0 50
particle minecraft:falling_water 10388 172 -16 0.4 0.5 0.4 0 50
particle minecraft:sculk_soul 10387 172 -12 0.4 0.5 0.4 0 50

playsound minecraft:block.trial_spawner.ominous_activate master @a[tag=mg.flw] 10392 170 -12 1 0.1

scoreboard players set lord_of_valor Story 4

tag @a[tag=mg.flw] remove no_warp
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 0

kill @e[tag=lord_machine,distance=0..]
setblock 10392 171 -17 air
fill 10379 171 -11 10379 173 -13 air

#stop particles and laser
setblock 10395 80 -12 air

#Open Virion
setblock -9765 240 418 minecraft:redstone_block

scoreboard players set mainstory Story 13
