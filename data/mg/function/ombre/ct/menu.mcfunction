# @s : contrat de la guilde (prendre, suivre, rendre)
execute if score @s mg.olct matches 1.. if score @s mg.olcp >= @s mg.olcn run return run function mg:ombre/ct/done
execute if score @s mg.olct matches 1.. run return run function mg:ombre/ct/status
function mg:ombre/ct/new
