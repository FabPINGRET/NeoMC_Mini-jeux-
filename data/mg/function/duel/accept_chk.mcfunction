# Dernières vérifications puis départ (@s = invité ; le défieur porte mg.dlca)
execute unless entity @a[tag=mg.dlca] run return run function mg:duel/fail_gone
function mg:duel/busy
execute if score $dlb mg.st matches 1 run return run function mg:duel/fail_busy
execute if entity @s[tag=mg.dlrq] run return run function mg:duel/fail_busy
execute as @a[tag=mg.dlca] run function mg:duel/busy
execute if score $dlb mg.st matches 1 run return run function mg:duel/fail_gone
function mg:duel/pick
execute if score $dli mg.st matches 0 run return run function mg:duel/fail_map
function mg:duel/start
