tp @n[tag=custodian_stand,distance=0..] -10441 67 439
setblock -10451 68 423 air
setblock -10449 67 423 minecraft:redstone_block
function boss:mini/custodian/appear
bossbar set boss:custodian players @a[tag=mg.flw]

setblock -10439 67 423 redstone_block

function music:miniboss

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
