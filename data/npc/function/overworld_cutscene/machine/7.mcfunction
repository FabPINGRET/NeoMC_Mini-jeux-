execute positioned 10387 170 -12 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Valor","color":"yellow"},{"text":"> What do you mean, scumlips? What have you done?","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/machine/8 6s replace

#","color":"white"},{"text":"
