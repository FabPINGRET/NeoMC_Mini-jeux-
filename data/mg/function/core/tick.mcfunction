# Boucle principale (chaque tick)
scoreboard players add $tc mg.st 1

# Triggers utilisables par tous
scoreboard players enable @a mg.menu
scoreboard players enable @a mg.go
scoreboard players enable @a mg.opt
scoreboard players enable @a mg.cls
scoreboard players enable @a mg.vote
scoreboard players enable @a mg.bb
scoreboard players enable @a mg.bw

# Nouveaux joueurs (ou ré-init après setup)
execute if score $setup mg.st matches 1 as @a[tag=!mg.init] run function mg:core/join

# Joueur reconnecté → lobby (jamais dans l'arène)
execute if score $setup mg.st matches 1 as @a[scores={mg.lg=1..}] run function mg:core/reconnect

# Ouverture du menu (objet ou /trigger mg.menu)
execute as @a[scores={mg.cs=1..}] run function mg:core/menu_use
execute as @a[scores={mg.menu=1}] run function mg:core/menu_use
execute as @a[scores={mg.menu=2..}] run function mg:core/menu_chat_force

# Choix de classe (PvP Classes)
execute as @a[scores={mg.cls=1..}] run function mg:pvp2/choose

# Votes des joueurs
execute as @a[scores={mg.vote=1..}] run function mg:vote/cast

# Build Battle : notes et choix du thème
execute as @a[scores={mg.bb=1..}] run function mg:bb/rate_cast
execute as @a[scores={mg.bw=1..}] run function mg:bb/word_cast

# Actions demandées
execute as @a[scores={mg.go=1..}] run function mg:core/go
execute as @a[scores={mg.opt=1..}] run function mg:core/opt

# Armurerie du lobby
execute if score $setup mg.st matches 1 run function mg:lobby/armory_tick

# Parkour du lobby
execute if score $setup mg.st matches 1 run function mg:parkour/tick

# Machine à états
execute if score $state mg.st matches 1 run function mg:core/countdown
execute if score $state mg.st matches 2 run function mg:core/game_tick
execute if score $state mg.st matches 3 run function mg:core/ending

# Hors partie : nettoyage de sécurité + rattrapage du vide
execute if score $state mg.st matches 0 run tag @a remove mg.play
execute if score $state mg.st matches 0 run tag @a remove mg.out
execute if score $state mg.st matches 0 as @a[gamemode=spectator] run function mg:core/back_to_lobby
execute as @a[tag=mg.init,tag=!mg.play,tag=!mg.out] at @s run function mg:core/void_catch
