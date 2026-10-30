# @s passe le portail du foot du hub (mg:hub/enter_foot) : descend sur le terrain, devant la porte du vestiaire, face au terrain
tp @s 0.5 48 -16.5 facing 0.5 48 -22.5
execute at @s run playsound minecraft:block.portal.travel master @s ~ ~ ~ 0.2 1.8
execute at @s run particle minecraft:portal ~ ~1 ~ 0.3 0.6 0.3 0.5 30
