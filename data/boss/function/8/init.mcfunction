scoreboard players set boss:fs BossHealth 10
bossbar set boss:fs players
bossbar set boss:fs value 10
bossbar set boss:fs color green

#Reset Start Latch
setblock -10825 67 407 air

#Stop Pickattack Schedule
setblock -10827 67 365 air

#Stop Dreadwarden Facing Particular Direction
setblock -10872 68 407 air
setblock -10873 68 407 air
kill @n[tag=ice_dreadwarden,distance=0..]

#stop crumbling particles
setblock -10870 68 407 air

function boss:8/draw/normal
function boss:8/position/off
scoreboard players set boss:fs_motor Value 1
scoreboard players set boss:fs_targeting Value 1
scoreboard players set boss:fs_return Value 0

#reset volley chance
setblock -10842 67 373 minecraft:black_wool

tellraw @a[tag=mg.flw] "Remember to destroy movement tick redstone block after off position is achieved!"

#FLOOR
fill -10829 88 398 -10868 88 366 minecraft:snow_block replace minecraft:packed_ice
fill -10829 88 398 -10868 88 366 minecraft:snow_block replace minecraft:polished_diorite
fill -10829 88 398 -10868 88 366 minecraft:snow_block replace minecraft:diorite
fill -10829 88 398 -10868 88 366 minecraft:snow_block replace minecraft:waxed_oxidized_copper_grate

function boss:8/cutscene/stop_vents

#WALL
fill -10870 97 390 -10869 114 373 minecraft:blue_ice replace minecraft:diamond_block
fill -10868 93 385 -10868 90 387 prismarine_bricks replace minecraft:diamond_block
setblock -10868 89 387 minecraft:prismarine
fill -10864 94 371 -10868 123 392 air replace minecraft:diamond_block
setblock -10867 102 393 minecraft:barrier

fill -10854 89 396 -10854 123 368 barrier

schedule clear floaty:sched/boss/8/pick_attack
kill @e[tag=frodrone,distance=0..]
kill @e[tag=frostbyte_lightning_loc,distance=0..]

tag @a[tag=mg.flw] remove bossroom
