# @s choisit la classe Tank : kit, puis arène
scoreboard players set @s mg.pcl 3
function mg:pvpc/equip
function mg:pvpc/to_arena
tellraw @s [{"text":"⚔ Classe ","color":"gray"},{"text":"Tank","color":"aqua","bold":true},{"text":" — bonne chance ! ","color":"gray"},{"text":"(émeraude = boutique, boussole = retour)","color":"dark_gray"}]
