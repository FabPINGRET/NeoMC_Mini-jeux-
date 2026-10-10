# @s est mort dans l'arène : série perdue, réapparaît dans l'arène protégé 3 s, kit de classe rendu
scoreboard players set @s mg.deaths 0
scoreboard players set @s mg.pks 0
scoreboard players set @s mg.phc 0
function mg:pvpc/equip
effect give @s minecraft:resistance 3 4 true
