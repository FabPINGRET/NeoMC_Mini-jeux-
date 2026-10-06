# Attribue un couloir à @s (un par joueur, 12 max puis on recommence) et le téléporte en haut
scoreboard players operation @s mg.ln = $li mg.st
scoreboard players add $li mg.st 1
execute if score $li mg.st matches 12.. run scoreboard players set $li mg.st 0
function mg:dropper/to_top
