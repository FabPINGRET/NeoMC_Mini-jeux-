# 0 = RING, 1 = GROUND RING, 2 = STATIC

scoreboard players set @s Value 0
scoreboard players set wm_follow_dest bool 1
kill @e[tag=wm_grav_ref,distance=0..]

#stop slam land check
setblock -11199 -35 -105 minecraft:redstone_block
