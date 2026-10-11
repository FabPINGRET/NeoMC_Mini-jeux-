# @s est mort dans l'arène : série perdue, équipement (et achats) perdus, retour au mini-lobby pour rechoisir une classe
scoreboard players set @s mg.deaths 0
scoreboard players set @s mg.pks 0
scoreboard players set @s mg.phc 0
function mg:pvpc/cleanup
clear @s
effect clear @s
function mg:core/attr_reset
tp @s 13.5 55 11.0 180 0
spawnpoint @s 13 55 11
function mg:core/give_menu
function mg:core/heal
title @s title {"text":"☠ Tu es mort","color":"red","bold":true}
title @s subtitle {"text":"marche sur un socle pour redescendre","color":"gray"}
