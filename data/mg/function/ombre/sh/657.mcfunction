function mg:core/heal
scoreboard players operation @s mg.olmp = @s mg.olmm
function mg:ombre/mana_bar
tellraw @s {"text":"🍺 Tu te reposes un moment près du feu. Vie et mana restaurées.","color":"gold"}
