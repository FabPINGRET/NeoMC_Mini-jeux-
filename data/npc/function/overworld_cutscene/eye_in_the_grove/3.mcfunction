function boss:mini/eye_in_the_grove/horse_summon
execute positioned -10060 117 328 run function summon:eye_in_the_grove
function boss:mini/eye_in_the_grove/eye_ride
bossbar set boss:eye_in_the_grove players @a[tag=mg.flw]
setblock -10044 105 327 redstone_block
particle dust_color_transition{from_color:[0.678,0.678,0.678],to_color:[1.000,0.569,0.000],scale:2} -10060 117 328 1 1 1 0 200 normal
playsound minecraft:block.trial_spawner.ominous_activate hostile @a[tag=mg.flw] -10060 117 328 2 0.7

tp @n[tag=grove_eye_cutscene,distance=0..] -10060 110 328 180 0

tag @a[tag=mg.flw] remove cutscene

setblock -10059 105 349 minecraft:redstone_block

function music:miniboss

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
