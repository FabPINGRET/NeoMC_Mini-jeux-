# @s dépense $(m) mana (renvoie 0 s'il n'en a pas assez)
$execute unless score @s mg.olmp matches $(m).. run return run function mg:ombre/cl/nomana
$scoreboard players remove @s mg.olmp $(m)
function mg:ombre/mana_bar
return 1
