scoreboard players set $mpbk mg.st -1
execute as @a[tag=mg.play] if score @s mg.ok > $mpbk mg.st run scoreboard players operation $mpbk mg.st = @s mg.ok
execute as @a[tag=mg.play] if score @s mg.ok = $mpbk mg.st run tag @s add mg.mpbest
execute as @a[tag=mg.mpbest,limit=1] run function mg:core/win_player
tag @a remove mg.mpbest
execute unless score $state mg.st matches 3 run function mg:core/draw
