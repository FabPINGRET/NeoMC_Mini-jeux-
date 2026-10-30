setblock -11133 38 416 air
function boss:mini/threnodist/new_target
schedule function floaty:sched/boss/mini/threnodist/pick_attack 3s replace
bossbar set boss:folded_threnodist players @a[tag=mg.flw]

function music:miniboss

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
