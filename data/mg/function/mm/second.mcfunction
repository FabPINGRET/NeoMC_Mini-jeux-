scoreboard players set $mml mg.st 270
scoreboard players operation $mmq mg.st = $mmt mg.st
scoreboard players operation $mmq mg.st /= #20 mg.st
scoreboard players operation $mml mg.st -= $mmq mg.st
execute if score $mmt mg.st matches ..200 run title @a[tag=mg.mmm] actionbar {"text":"🔪 Ton couteau arrive dans quelques secondes…","color":"red"}
execute if score $mmt mg.st matches 201.. run title @a[tag=mg.play,tag=mg.mmm] actionbar [{"text":"🔪 Innocents restants : ","color":"red"},{"score":{"name":"$mmn","objective":"mg.st"},"color":"yellow","bold":true},{"text":" — ","color":"gray"},{"score":{"name":"$mml","objective":"mg.st"},"color":"yellow"},{"text":" s","color":"gray"}]
execute as @a[tag=mg.play,tag=!mg.mmm] run title @s actionbar [{"text":"🪙 Or : ","color":"gold"},{"score":{"name":"@s","objective":"mg.mmo"},"color":"yellow","bold":true},{"text":"/10 — ","color":"gray"},{"score":{"name":"$mml","objective":"mg.st"},"color":"yellow"},{"text":" s","color":"gray"}]
