scoreboard players set $phl mg.st 240
scoreboard players operation $phs2 mg.st = $pht mg.st
scoreboard players operation $phs2 mg.st /= #20 mg.st
scoreboard players operation $phl mg.st -= $phs2 mg.st
execute if score $pht mg.st matches ..600 run title @a[tag=mg.phs] actionbar [{"text":"🎭 Les cacheurs se cachent… ","color":"gray"},{"score":{"name":"$phl","objective":"mg.st"},"color":"yellow"}]
execute if score $pht mg.st matches 601.. run title @a[tag=mg.phs] actionbar [{"text":"🎭 Cacheurs restants : ","color":"red"},{"score":{"name":"$phh","objective":"mg.st"},"color":"yellow","bold":true},{"text":" — ","color":"gray"},{"score":{"name":"$phl","objective":"mg.st"},"color":"yellow"},{"text":" s","color":"gray"}]
