# @s choisit la classe Archer : kit, puis arène
scoreboard players set @s mg.pcl 2
function mg:pvpc/equip
function mg:pvpc/to_arena
tellraw @s [{"text":"⚔ Classe ","color":"gray"},{"text":"Archer","color":"green","bold":true},{"text":" — bonne chance ! ","color":"gray"},{"text":"(émeraude = boutique, boussole = retour)","color":"dark_gray"}]
