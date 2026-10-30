execute positioned -11146 68 332 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 3 0.7

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Wahrog the Prophet","color":"#44BBFF"},{"text":"> A great prophet I shall once more be!","color":"white"}]

setblock -11161 28 350 air
function boss:mini/wahrog/target/pivot
function boss:mini/wahrog/new_target
tp @n[tag=wahrog_stand,distance=0..] -11146 71 332
schedule function floaty:sched/boss/mini/wahrog/pick_attack 4s
bossbar set boss:prophet players @a[tag=mg.flw]

setblock -11157 27 342 minecraft:redstone_block

function music:miniboss

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
