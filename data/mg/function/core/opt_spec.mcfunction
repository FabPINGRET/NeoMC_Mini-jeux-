# Bascule pause (@s = joueur ; tag mg.spectate : le joueur reste où il est quand une partie est lancée)
execute store success score @s mg.t if entity @s[tag=mg.spectate]

# Était en pause → redevient joueur
execute if score @s mg.t matches 1 run tag @s remove mg.spectate
# (Mini Party en cours sans lui : il ne la rejoint pas)
execute if score @s mg.t matches 1 if score $mp mg.st matches 1 unless entity @s[tag=mg.mpp] run tellraw @s [{"text":"▶ Pause désactivée : la Mini Party continue sans toi ; tu seras téléporté aux parties suivantes.","color":"green"}]
execute if score @s mg.t matches 1 if score $mp mg.st matches 1 unless entity @s[tag=mg.mpp] run scoreboard players set @s mg.t 2
execute if score @s mg.t matches 1 run tellraw @s [{"text":"▶ Pause désactivée : tu seras téléporté aux prochaines parties.","color":"green"}]

# Passe en pause
execute if score @s mg.t matches 0 run tag @s add mg.spectate
execute if score @s mg.t matches 0 if entity @s[tag=mg.play] run tellraw @s [{"text":"⏸ Pause : tu quittes la partie en cours (spectateur tant que tu es en pause).","color":"gray"}]
execute if score @s mg.t matches 0 unless entity @s[tag=mg.play] run tellraw @s [{"text":"⏸ Pause activée : tu restes où tu es quand une partie est lancée (re-clique pour reprendre).","color":"gray"}]

# Son vote éventuel ne compte plus (lobby : en partie, les votes sont déjà effacés)
execute if score @s mg.t matches 0 if score $state mg.st matches 0 run scoreboard players reset @s mg.vc
execute if score @s mg.t matches 0 if score $state mg.st matches 0 run function mg:vote/refresh

# S'il était en pleine partie → abandon
execute if score @s mg.t matches 0 if entity @s[tag=mg.play] run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" abandonne la partie.","color":"gray"}]
execute if score @s mg.t matches 0 if entity @s[tag=mg.play] run function mg:core/eliminate
