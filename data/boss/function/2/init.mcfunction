scoreboard players set boss:cob BossHealth 10
bossbar set boss:cob value 10
bossbar set boss:cob color green
bossbar set boss:cob players
fill -10134 138 -15 -10155 138 -31 glass replace stone
fill -10147 152 -50 -10117 158 -12 air replace minecraft:bone_block
fill -10147 152 -50 -10117 158 -12 air replace minecraft:barrier
kill @e[tag=ck_eye,distance=0..]
setblock -10114 138 -68 air
tag @a[tag=mg.flw] remove bossroom
scoreboard players set boss:cob Countdown 9
setblock -10132 138 -60 air
fill -10137 141 -60 -10134 141 -60 air
setblock -10126 138 -57 stone
setblock -10151 138 -15 air
fill -10154 157 -34 -10154 156 -28 air replace minecraft:blue_stained_glass
