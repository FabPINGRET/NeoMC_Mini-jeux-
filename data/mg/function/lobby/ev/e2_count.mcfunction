execute store result score @s mg.evc run clear @s minecraft:gold_nugget[minecraft:custom_data~{mg_ev:1b}] 0
execute store result score #evi mg.st run clear @s minecraft:gold_ingot[minecraft:custom_data~{mg_ev:1b}] 0
scoreboard players operation #evi mg.st *= #ev5 mg.st
scoreboard players operation @s mg.evc += #evi mg.st
execute unless score $theme mg.st matches 1..2 run title @s actionbar [{"text":"💰 ","color":"gold"},{"score":{"name":"@s","objective":"mg.evc"},"color":"yellow","bold":true},{"text":" pièces","color":"gold"}]
execute if score $theme mg.st matches 1 run title @s actionbar [{"text":"🍬 ","color":"gold"},{"score":{"name":"@s","objective":"mg.evc"},"color":"yellow","bold":true},{"text":" bonbons","color":"gold"}]
execute if score $theme mg.st matches 2 run title @s actionbar [{"text":"🎁 ","color":"gold"},{"score":{"name":"@s","objective":"mg.evc"},"color":"yellow","bold":true},{"text":" cadeaux","color":"gold"}]
