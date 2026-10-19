# @s : plus grande prise que son record (#lfs en cm) ? Oui : record remplacé, message, plaque du Hall
scoreboard players add @s mg.lfb 0
execute unless score #lfs mg.st > @s mg.lfb run return 0
scoreboard players operation @s mg.lfb = #lfs mg.st
tellraw @s [{"text":"⭐ Nouveau record perso : ","color":"yellow"},{"score":{"name":"#lfs","objective":"mg.st"},"color":"gold","bold":true},{"text":" cm","color":"gray"}]
function mg:hall/top {obj:"mg.lfb",key:"fish",lbl:"🎣 Plus belle prise",col:"aqua",unit:" cm"}
