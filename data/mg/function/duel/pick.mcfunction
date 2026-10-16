# Arène libre au hasard -> $dli (1 Canyon, 2 Ville, 3 Glacier ; 0 = aucune ou pas encore construites)
scoreboard players set $dli mg.st 0
execute unless data storage mg:duel {built:1b} run return 0
execute store result score #dlm mg.st run random value 1..3
execute if score #dlm mg.st matches 1 if score $dli mg.st matches 0 unless entity @a[tag=mg.dl,scores={mg.dli=1}] run scoreboard players set $dli mg.st 1
execute if score #dlm mg.st matches 1 if score $dli mg.st matches 0 unless entity @a[tag=mg.dl,scores={mg.dli=2}] run scoreboard players set $dli mg.st 2
execute if score #dlm mg.st matches 1 if score $dli mg.st matches 0 unless entity @a[tag=mg.dl,scores={mg.dli=3}] run scoreboard players set $dli mg.st 3
execute if score #dlm mg.st matches 2 if score $dli mg.st matches 0 unless entity @a[tag=mg.dl,scores={mg.dli=2}] run scoreboard players set $dli mg.st 2
execute if score #dlm mg.st matches 2 if score $dli mg.st matches 0 unless entity @a[tag=mg.dl,scores={mg.dli=3}] run scoreboard players set $dli mg.st 3
execute if score #dlm mg.st matches 2 if score $dli mg.st matches 0 unless entity @a[tag=mg.dl,scores={mg.dli=1}] run scoreboard players set $dli mg.st 1
execute if score #dlm mg.st matches 3 if score $dli mg.st matches 0 unless entity @a[tag=mg.dl,scores={mg.dli=3}] run scoreboard players set $dli mg.st 3
execute if score #dlm mg.st matches 3 if score $dli mg.st matches 0 unless entity @a[tag=mg.dl,scores={mg.dli=1}] run scoreboard players set $dli mg.st 1
execute if score #dlm mg.st matches 3 if score $dli mg.st matches 0 unless entity @a[tag=mg.dl,scores={mg.dli=2}] run scoreboard players set $dli mg.st 2
