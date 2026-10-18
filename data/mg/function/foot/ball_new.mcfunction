# Balle (sulfur_cube, bloc de test en corps : ballon du resource pack ; archétype mg:football) au centre ; jamais mg.lby / mg.mob / mg.npc : les nettoyages du lobby la tueraient
summon minecraft:sulfur_cube 2.5 48 -30.5 {Tags:["mg.ball"],equipment:{body:{id:"minecraft:test_block",count:1}},drop_chances:{body:0f},Invulnerable:1b,PersistenceRequired:1b}
scoreboard players set $fti mg.ft 0
