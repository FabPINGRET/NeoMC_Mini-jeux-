# Flèche enchantée offerte par le minuteur (@s = joueur tiré au sort)
function mg:oitc/special_give
tellraw @a[tag=mg.play] [{"text":"✦ ","color":"light_purple"},{"selector":"@s","color":"yellow"},{"text":" reçoit une flèche enchantée !","color":"light_purple"}]
