execute positioned -12384 123 355 run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 4 1.2

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Valor","color":"yellow"},{"text":"> I... I can't believe it's over.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/boss/final/cutscene/death_4 5s replace

#","color":"white"},{"text":"
