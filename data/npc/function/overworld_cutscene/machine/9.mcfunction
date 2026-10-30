execute positioned 10396 170 -12 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord Morbex","color":"dark_aqua","bold":true},{"text":"> While you’ve been playing hero, my machine has been siphoning a trickle of power from the ","color":"white","bold":false},{"text":"Bell","color":"gold"},{"text":" and focusing it like a needle against its own defenses.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/machine/10 11s replace

#","color":"white"},{"text":"
