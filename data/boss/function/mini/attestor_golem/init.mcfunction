bossbar set boss:attestor value 1000
bossbar set boss:attestor color green
bossbar set boss:attestor players
scoreboard players set boss:attestor BossHealth 1000

kill @e[tag=a_golem,distance=0..]

#Replace statue
fill -10721 109 -263 -10719 119 -257 air
clone -10689 107 -265 -10686 117 -259 -10722 109 -263

fill -10708 108 -259 -10710 108 -261 minecraft:dripstone_block
setblock -10709 108 -260 minecraft:mud_bricks
setblock -10709 109 -260 minecraft:polished_blackstone_button[face=floor,facing=west,powered=false]

# END TICK
setblock -10686 124 -269 air
setblock -10686 124 -271 air

# RESET WIN LINE
setblock -10688 123 -269 air
