setblock -10324 61 462 minecraft:redstone_block
function boss:mini/pretzel/pick_attack

bossbar set boss:pretzel players @a[tag=mg.flw]

setblock -10355 61 439 redstone_block

function music:miniboss

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
