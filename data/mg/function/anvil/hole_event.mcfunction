# Prochain trou : l'intervalle diminue avec le niveau d'intensité (100 ticks → 45 ticks)
scoreboard players set $hc mg.st 100
scoreboard players operation $tmp mg.st = $lv mg.st
scoreboard players operation $tmp mg.st *= $c6 mg.st
scoreboard players operation $hc mg.st -= $tmp mg.st
scoreboard players operation $hc mg.st > $hmin mg.st
function mg:anvil/hole_new
execute if score $lv mg.st matches 4.. run function mg:anvil/hole_new
execute if score $lv mg.st matches 8.. run function mg:anvil/hole_new
