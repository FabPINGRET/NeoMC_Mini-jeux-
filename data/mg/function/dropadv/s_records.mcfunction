# Rappel des records (serveur pour tous, personnel pour chacun)
execute if score #srv mg.dsb matches 1.. run tellraw @a[tag=mg.play] [{"text":"🏆 Record du serveur : ","color":"gold"},{"score":{"name":"#srv","objective":"mg.dsb"},"color":"yellow","bold":true},{"text":" essais","color":"yellow"},{"text":" (","color":"gray"},{"nbt":"rec","storage":"mg:dropadv","interpret":true},{"text":")","color":"gray"}]
execute unless score #srv mg.dsb matches 1.. run tellraw @a[tag=mg.play] [{"text":"🏆 Pas encore de record du serveur : à toi de le poser !","color":"gold"}]
execute as @a[tag=mg.play] if score @s mg.dsb matches 1.. run tellraw @s [{"text":"★ Ton record : ","color":"aqua"},{"score":{"name":"@s","objective":"mg.dsb"},"color":"white","bold":true},{"text":" essais","color":"white"}]
