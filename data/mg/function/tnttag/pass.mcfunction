# Passe la bombe de @s (porteur) au joueur marqué mg.newb
function mg:tnttag/unequip
scoreboard players set @s mg.cd 30
execute as @a[tag=mg.newb] run tag @s add mg.bomb
execute as @a[tag=mg.newb] run function mg:tnttag/equip
tellraw @a [{"selector":"@s","color":"yellow"},{"text":" passe la bombe à ","color":"gray"},{"selector":"@a[tag=mg.newb]","color":"red"},{"text":" !","color":"gray"}]
tag @a remove mg.newb
