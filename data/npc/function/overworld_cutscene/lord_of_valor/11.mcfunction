execute positioned 10022 93 -99 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:item.armor.equip_leather neutral @a[tag=mg.flw] ~ ~ ~ 1 1

item replace entity 628a093a-fd14-4699-b4e4-4873fd4ab2fd armor.head from block 10023 90 -102 container.9
item replace entity 628a093a-fd14-4699-b4e4-4873fd4ab2fd weapon.mainhand with air

schedule function floaty:sched/npc/overworld_cutscene/lord_of_valor/12 2s replace
