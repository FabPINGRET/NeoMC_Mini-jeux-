execute positioned 10022 93 -99 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10022 93 -99 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:item.armor.equip_leather neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10022 93 -99 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Grlu","color":"light_purple"},{"text":"> My real name is Grlu. I've always wanted to be a hero, and when ","color":"white"},{"text":"Morbex","color":"dark_aqua"},{"text":" and his cronies showed up I took it as my chance to show the world how brave I can be.","color":"white"},{"text":" ⇒","color":"light_purple"}]

item replace entity 628a093a-fd14-4699-b4e4-4873fd4ab2fd armor.head from block 10023 90 -102 container.18
item replace entity 628a093a-fd14-4699-b4e4-4873fd4ab2fd weapon.mainhand from block 10023 90 -102 container.9


schedule function floaty:sched/npc/overworld_cutscene/lord_of_valor/3 11s replace
