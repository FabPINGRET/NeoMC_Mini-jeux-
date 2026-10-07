# Mur devant : le kart ne passe pas, rebondit un peu en arrière (@s = kart)
$execute at @s run tp @s ~ ~$(v) ~
execute on passengers if entity @s[type=minecraft:player] run function mg:kart/bumped
