# Un tir d'enclumes (1 à 3 selon l'intensité)
scoreboard players operation $ac mg.st = $ai mg.st
function mg:anvil/drop
execute if score $ai mg.st matches ..10 run function mg:anvil/drop
execute if score $ai mg.st matches ..6 run function mg:anvil/drop
