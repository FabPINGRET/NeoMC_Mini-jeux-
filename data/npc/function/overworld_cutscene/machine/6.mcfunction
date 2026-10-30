execute positioned 10396 170 -12 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord Morbex","color":"dark_aqua","bold":true},{"text":"> Ah, so you found a new seventh Lord. This is your play, is it? I concede you’ve won the","color":"white","bold":false},{"text":" Dark Isles","color":"dark_purple"},{"text":", but not before I achieved my ultimate purpose here...","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/machine/7 11s replace

#","color":"white"},{"text":"
