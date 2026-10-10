# @s = chien : disparaît si son maître n'est plus dans l'arène
scoreboard players operation $p mg.st = @s mg.pvid
scoreboard players set $f mg.st 0
execute as @a[tag=mg.pvpc] if score @s mg.pvid = $p mg.st run scoreboard players set $f mg.st 1
execute if score $f mg.st matches 0 run tp @s ~ -300 ~
