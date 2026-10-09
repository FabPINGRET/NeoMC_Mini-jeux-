# @s : lanceur de la bombe qui vient d'exploser ($bpts points)
scoreboard players operation @s mg.bmb += $bpts mg.st
execute if score $bpts mg.st matches 1.. run title @s actionbar [{"text":"💥 +","color":"gold"},{"score":{"name":"$bpts","objective":"mg.st"},"color":"yellow","bold":true},{"text":" dégâts","color":"gold"}]
execute if score $bpts mg.st matches 0 run title @s actionbar {"text":"💨 Raté !","color":"gray"}
execute if score $bpts mg.st matches 400.. run tellraw @a[tag=mg.play] [{"text":"💥 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" : coup dévastateur, ","color":"red"},{"score":{"name":"$bpts","objective":"mg.st"},"color":"gold","bold":true},{"text":" points !","color":"red"}]
execute if score $bpts mg.st matches 1.. at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.6 0.8
