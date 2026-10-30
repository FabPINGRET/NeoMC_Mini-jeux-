setblock -12346 43 336 air
setblock -12346 43 334 minecraft:redstone_block
function boss:final/morbex/attack/do_sunray
bossbar set boss:final_morbex players @a[tag=mg.flw]
scoreboard players set final_morbex_target_mode Value 1
#Start death check
setblock -12354 42 383 redstone_block
function music:dark_boss
