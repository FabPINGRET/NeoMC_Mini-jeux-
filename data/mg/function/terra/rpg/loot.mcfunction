# @s a ramassé du butin d'élite / des gemmes : ouverture
execute store result score $n mg.st run clear @s *[custom_data~{trloot:1}]
execute if score $n mg.st matches 1.. run function mg:terra/rpg/loot_open
execute store result score $g mg.st run clear @s *[custom_data~{trloot:2}]
execute if score $g mg.st matches 1.. run function mg:terra/rpg/loot_gem
