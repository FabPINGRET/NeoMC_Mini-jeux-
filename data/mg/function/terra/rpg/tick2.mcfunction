# Chaque tick (dimension) : butin, trésors, chiffres de dégâts
execute if score $tvq5 mg.st matches 0 as @a[tag=mg.tvw] if items entity @s container.* *[custom_data~{trloot:1}] run function mg:terra/rpg/loot
execute if score $tvq5 mg.st matches 0 as @a[tag=mg.tvw] if items entity @s container.* *[custom_data~{trloot:2}] run function mg:terra/rpg/loot
execute if score $tvq5 mg.st matches 0 run function mg:terra/rpg/tc_tick
function mg:terra/rpg/dmg_tick
