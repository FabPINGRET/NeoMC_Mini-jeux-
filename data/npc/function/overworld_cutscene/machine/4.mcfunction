execute positioned 10395 170 -8 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.ravager.stunned neutral @a[tag=mg.flw] ~ ~ ~ 1 1.4

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Flame","color":"red"},{"text":"> Morbex, your tyranny over this realm is at an end.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/machine/5 6s replace

#","color":"white"},{"text":"
