execute positioned -12384 123 355 run particle minecraft:witch ~ ~1 ~ 1.5 0.5 1.5 2 200 force
execute positioned -12384 123 355 run particle minecraft:instant_effect ~ ~1 ~ 3 1 3 2 400 force
execute positioned -12384 123 355 run playsound minecraft:ambient.warped_forest.mood master @a[tag=mg.flw] ~ ~1 ~ 4 1
execute positioned -12384 123 355 run playsound minecraft:block.respawn_anchor.set_spawn master @a[tag=mg.flw] ~ ~1 ~ 3 0.1
execute positioned -12384 123 355 run playsound minecraft:block.respawn_anchor.ambient master @a[tag=mg.flw] ~ ~1 ~ 3 1
execute positioned -12384 123 355 run playsound minecraft:item.trident.riptide_1 master @a[tag=mg.flw] ~ ~1 ~ 4 0.7
execute positioned -12384 123 355 run playsound minecraft:entity.evoker.prepare_attack master @a[tag=mg.flw] ~ ~1 ~ 4 1.4

schedule function floaty:sched/boss/final/cutscene/18 3s replace

#","color":"white"},{"text":"
