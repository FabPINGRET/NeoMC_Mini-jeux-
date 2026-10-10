# @s choisit la classe Assassin : kit, puis arène
scoreboard players set @s mg.pcl 4
function mg:pvpc/equip
function mg:pvpc/to_arena
tellraw @s [{"text":"⚔ Classe ","color":"gray"},{"text":"Assassin","color":"dark_gray","bold":true},{"text":" — bonne chance ! ","color":"gray"},{"text":"(émeraude = boutique, boussole = retour)","color":"dark_gray"}]
