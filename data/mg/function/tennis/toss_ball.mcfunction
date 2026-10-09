# @s : nouvelle balle (lancer du service)
tag @s remove mg.tnnew
scoreboard players operation @s mg.tnc = $tnk mg.st
tag @s add mg.tnk
tag @s add mg.tntoss
function mg:tennis/sync_in
scoreboard players set @s mg.tnvx 0
scoreboard players set @s mg.tnvz 0
scoreboard players set @s mg.tnvy 230
scoreboard players operation @s mg.tnl = $tnside mg.st
scoreboard players set @s mg.tnb 0
