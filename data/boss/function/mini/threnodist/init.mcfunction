bossbar set boss:folded_threnodist value 180
bossbar set boss:folded_threnodist color green
bossbar set boss:folded_threnodist players

tag @a[tag=mg.flw] remove targeted

tp @n[tag=threnodist_stand,distance=0..] -11144 58 430 0 0
kill @n[tag=threnodist_boss,distance=0..]
kill @e[tag=d_hymnodist,distance=0..]

scoreboard players set thren_target Value 0
scoreboard players set thren_counter Value 0

#stop tick
fill -11131 38 416 -11129 36 416 air replace minecraft:redstone_block
fill -11131 38 426 -11129 38 426 air
setblock -11133 37 425 air
