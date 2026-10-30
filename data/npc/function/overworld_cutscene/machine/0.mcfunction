#execute positioned 10392 171 -12 at @e[sort=nearest,limit=1,tag=npc] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a ~ ~ ~ 1 1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord Morbex","color":"dark_aqua","bold":true},{"text":"> Bold of you to approach me here, defender of the ","color":"white","bold":false},{"text":"Bell","color":"gold"},{"text":".","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/machine/1 7s replace

fill 10395 171 -11 10396 171 -11 air
fill 10379 171 -11 10379 173 -13 minecraft:cyan_stained_glass

tag @a[tag=mg.flw] add no_warp
function music:end
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1

function music:morbex

#stop laser
fill 10392 154 -12 10392 82 -12 air

#","color":"white"},{"text":"
