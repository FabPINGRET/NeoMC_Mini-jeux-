execute positioned -10720 109 -260 run function summon:attestor_golem

fill -10721 109 -263 -10719 119 -257 air
fill -10720 109 -260 -10720 117 -260 light[level=15]

fill -10710 108 -259 -10708 108 -261 stone
setblock -10709 109 -260 air

scoreboard players set trial_well_3_going bool 1

particle block{block_state:"mud_bricks"} -10720 114 -260 2 5 2 0 500
playsound minecraft:item.mace.smash_ground_heavy master @a[tag=mg.flw] -10720 109 -260 3 0.1

# START TICK
setblock -10686 124 -269 minecraft:redstone_block

# SETUP BOSSBAR
setblock -10686 123 -267 minecraft:redstone_block

# START ATTACKS
setblock -10686 123 -273 minecraft:redstone_block

function music:miniboss

scoreboard players set a_golem_breath_timer Value 200
