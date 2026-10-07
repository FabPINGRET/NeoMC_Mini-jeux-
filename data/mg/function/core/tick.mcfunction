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
scoreboard players enable @a mg.pl
scoreboard players enable @a mg.dice
function mg:survie/tick
execute as @a[scores={mg.dice=5..10}] run function mg:party/menu_cmd
execute as @a[scores={mg.dice=3}] unless score $game mg.st matches 59 run function mg:party/menu_nomap

# Nouveaux joueurs (ou ré-init après setup)
execute if score $setup mg.st matches 1 as @a[tag=!mg.init,tag=!mg.surv] run function mg:core/join

# Joueur reconnecté → lobby (jamais dans l'arène)
execute if score $setup mg.st matches 1 as @a[scores={mg.lg=1..}] run function mg:core/reconnect

# Ouverture du menu (objet ou /trigger mg.menu)
execute as @a[scores={mg.cs=1..},tag=!mg.surv] run function mg:core/menu_use
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
scoreboard players remove @a[scores={mg.fd=1..}] mg.fd 1
# Parcours d'élytra : socle de départ, joueurs en vol, objets du parcours jamais conservés
execute if score $setup mg.st matches 1 as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.ely,gamemode=adventure,x=16,y=63,z=-9,dx=0.99,dy=2.5,dz=0.99] run function mg:elytra/start
execute as @a[tag=mg.ely] at @s run function mg:elytra/player
execute if score $lan mg.t matches 20 run clear @a[tag=!mg.ely] minecraft:elytra[minecraft:custom_data~{mg_ely:1b}]
execute if score $lan mg.t matches 20 run clear @a[tag=!mg.ely] minecraft:firework_rocket[minecraft:custom_data~{mg_ely:1b}]
execute if score $setup mg.st matches 1 as @a[tag=!mg.play,tag=!mg.surv,gamemode=adventure,x=24,y=63,z=19,dx=0.99,dy=2.5,dz=0.99] run function mg:lobby/food_give

# Kart libre du spawn
execute if score $setup mg.st matches 1 run function mg:lobkart/tick

# Parkour du lobby
execute if score $setup mg.st matches 1 run function mg:parkour/tick

# Plots des joueurs
execute as @a[scores={mg.pl=1..}] run function mg:plot/cmd
execute if score $setup mg.st matches 1 run function mg:plot/tick

# Canne ≡ MENU : refilée aux admins dès que leur inventaire est libre (toutes les 2 s ; hors partie, plot créatif, parkour, spectateur, créatif)
scoreboard players add $gmt mg.t 1
execute if score $gmt mg.t matches 40.. as @a[tag=mg.admin,tag=mg.init,tag=!mg.surv,tag=!mg.play,tag=!mg.out,tag=!mg.inplot,tag=!mg.pkr,tag=!mg.lk,tag=!mg.visit,gamemode=!spectator,gamemode=!creative] run function mg:core/give_menu_safe
execute if score $gmt mg.t matches 40.. run scoreboard players set $gmt mg.t 0

# Machine à états
execute if score $state mg.st matches 1 run function mg:core/countdown
execute if score $state mg.st matches 2 run function mg:core/game_tick
execute if score $state mg.st matches 3 run function mg:core/ending

# Hors partie : nettoyage de sécurité + rattrapage du vide
execute if score $state mg.st matches 0 run tag @a remove mg.play
execute if score $state mg.st matches 0 run tag @a remove mg.out
execute if score $state mg.st matches 0 as @a[gamemode=spectator,tag=!mg.visit,tag=!mg.surv,tag=!mg.lk] run function mg:core/back_to_lobby
execute as @a[tag=mg.init,tag=!mg.play,tag=!mg.out,tag=!mg.surv] at @s run function mg:core/void_catch

# Visiteurs de plots : confinés à la zone des plots
execute if entity @a[tag=mg.visit] run function mg:plot/visit_guard
