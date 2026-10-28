# Admin : régénère le chunk maintenant
execute if score $fnok mg.st matches 1 run function mg:filon/regen
execute unless score $fnok mg.st matches 1 run scoreboard players set $fnpend mg.st 1
