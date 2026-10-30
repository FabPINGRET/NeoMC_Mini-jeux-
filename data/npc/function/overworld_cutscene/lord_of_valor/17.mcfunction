particle minecraft:sculk_soul 10022 96 -102 0.3 0.7 0.3 0.3 400
particle minecraft:dust_pillar{block_state:"gold_block"} 10022 95 -102 0.4 0.7 0.4 0.5 300
playsound minecraft:entity.lightning_bolt.thunder master @a[tag=mg.flw] 10022 94 -102 3 1
playsound minecraft:item.mace.smash_ground_heavy master @a[tag=mg.flw] 10022 94 -102 3 1

item replace entity 628a093a-fd14-4699-b4e4-4873fd4ab2fd armor.head from block 10023 90 -102 container.0
item replace entity 628a093a-fd14-4699-b4e4-4873fd4ab2fd armor.chest from block 10023 90 -102 container.1
item replace entity 628a093a-fd14-4699-b4e4-4873fd4ab2fd armor.legs from block 10023 90 -102 container.2
item replace entity 628a093a-fd14-4699-b4e4-4873fd4ab2fd armor.feet from block 10023 90 -102 container.3

function music:slime_man_action

schedule function floaty:sched/npc/overworld_cutscene/lord_of_valor/18 5s replace
