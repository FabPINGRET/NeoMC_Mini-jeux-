bossbar set boss:prophet value 160
bossbar set boss:prophet color green
bossbar set boss:prophet players

tag @a[tag=mg.flw] remove targeted

function boss:mini/wahrog/pose/none
tp @n[tag=wahrog_stand,distance=0..] -11146 68 332 0 0
kill @n[tag=wahrog_boss,distance=0..]
kill @e[tag=c_parasite,distance=0..]

#Stop tick and particles
fill -11159 28 350 -11157 28 350 air
fill -11163 27 350 -11161 28 343 air replace minecraft:redstone_block

scoreboard players set wahrog_target Value 0
scoreboard players set wahrog_counter Value 0
