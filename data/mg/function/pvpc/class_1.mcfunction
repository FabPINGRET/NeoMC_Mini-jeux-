# @s choisit la classe Guerrier : kit, puis arène
scoreboard players set @s mg.pcl 1
function mg:pvpc/equip
function mg:pvpc/to_arena
tellraw @s [{"text":"⚔ Classe ","color":"gray"},{"text":"Guerrier","color":"white","bold":true},{"text":" — bonne chance ! ","color":"gray"},{"text":"(émeraude = boutique, boussole = retour)","color":"dark_gray"}]
