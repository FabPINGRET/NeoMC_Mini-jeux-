# @s : chapeau de saison, la saison est finie
scoreboard players set @s mg.hat 0
function mg:hat/strip
tellraw @s [{"text":"🎩 ","color":"gold"},{"text":"La saison est finie : ton chapeau de saison est rangé jusqu'à l'an prochain.","color":"gray"}]
