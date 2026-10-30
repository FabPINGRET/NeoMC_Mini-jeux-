scoreboard players set boss:lod BossHealth 6
bossbar set boss:lod value 6
bossbar set boss:lod color green
bossbar set boss:lod players
setblock -10083 134 -215 minecraft:redstone_block
tp @e[tag=lod_boss_loc,distance=0..] -10084 159 -189
fill -10083 134 -209 -10083 134 -211 air
setblock -10090 134 -201 air
setblock -10083 134 -199 minecraft:air
fill -10085 137 -199 -10087 137 -199 air
function boss:3/stal/collapse
fill -10093 160 -204 -10123 160 -174 sand replace minecraft:target
fill -10093 160 -204 -10123 160 -174 sand replace minecraft:suspicious_sand
setblock -10083 134 -188 air
