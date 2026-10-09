# @s = interaction frappée : le cacheur lié prend un coup (si c'est un chercheur)
execute on attacker if entity @s[tag=mg.phs] run tag @s add mg.phatk
data remove entity @s attack
scoreboard players operation $pid mg.st = @s mg.pid
execute if entity @a[tag=mg.phatk] as @a[tag=mg.phh] if score @s mg.pid = $pid mg.st run damage @s 5 minecraft:player_attack by @a[tag=mg.phatk,limit=1]
tag @a remove mg.phatk
