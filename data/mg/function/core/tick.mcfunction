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
scoreboard players enable @a mg.tel
scoreboard players enable @a mg.pl
scoreboard players enable @a mg.dice
scoreboard players enable @a mg.xs
function mg:survie/tick
execute as @a[scores={mg.dice=5..10}] run function mg:party/menu_cmd
execute as @a[scores={mg.dice=3}] unless score $game mg.st matches 59 run function mg:party/menu_nomap

# Nouveaux joueurs (ou ré-init après setup)
execute if score $setup mg.st matches 1 as @a[tag=!mg.init,tag=!mg.surv] run function mg:core/join

# Joueur reconnecté → lobby (jamais dans l'arène)
# Détection fiable : un joueur initialisé qui n'était pas là au tick précédent (mg.seen ≠ $tc - 1) vient de se reconnecter
# (le compteur leave_game seul ne suffisait pas : un joueur parti pendant un jeu terminé restait dans l'arène avec son équipement)
scoreboard players operation #prev mg.st = $tc mg.st
scoreboard players remove #prev mg.st 1
execute if score $setup mg.st matches 1 as @a[tag=mg.init] if score @s mg.seen matches ..2147483647 unless score @s mg.seen = #prev mg.st run scoreboard players set @s mg.lg 1
scoreboard players operation @a mg.seen = $tc mg.st
execute if score $setup mg.st matches 1 as @a[scores={mg.lg=1..}] run function mg:core/reconnect

# Ouverture du menu (objet ou /trigger mg.menu)
execute as @a[scores={mg.cs=1..},tag=!mg.surv] run function mg:core/menu_use
execute as @a[scores={mg.menu=1}] run function mg:core/menu_use
execute as @a[scores={mg.menu=2..}] run function mg:core/menu_chat_force

# Choix de classe (PvP Classes)
execute as @a[scores={mg.cls=1..}] run function mg:pvp2/choose

# Votes des joueurs
execute as @a[scores={mg.vote=1..}] run function mg:vote/cast
# Votes à la majorité : lancement automatique (une fois par seconde)
scoreboard players add $vtk mg.st 1
execute if score $vtk mg.st matches 20.. run function mg:vote/auto_tick
execute if score $vtk mg.st matches 20.. run scoreboard players set $vtk mg.st 0

# Build Battle : notes et choix du thème
execute as @a[scores={mg.bb=1..}] run function mg:bb/rate_cast
execute as @a[scores={mg.bw=1..}] run function mg:bb/word_cast
execute as @a[scores={mg.tel=1..}] run function mg:tel/cast

# Actions demandées
execute as @a[scores={mg.go=1..}] run function mg:core/go
execute as @a[scores={mg.opt=1..}] run function mg:core/opt
execute as @a[scores={mg.xs=1..}] run function mg:elyrace/solo/cmd

# Armurerie du lobby
execute if score $setup mg.st matches 1 run function mg:lobby/armory_tick
scoreboard players remove @a[scores={mg.fd=1..}] mg.fd 1
# Parcours d'élytra : socle de départ, joueurs en vol, objets du parcours jamais conservés
execute if score $setup mg.st matches 1 as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.ely,gamemode=adventure,x=16,y=63,z=-9,dx=0.99,dy=2.5,dz=0.99] run function mg:elytra/start
execute if score $setup mg.st matches 1 as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.ely,gamemode=adventure,x=32,y=63,z=-15,dx=0.99,dy=2.5,dz=0.99] run function mg:elytra/start2
execute as @a[tag=mg.ely] at @s run function mg:elytra/player
# Élytres libres : socle (une fois par passage), joueurs en vol, objets jamais conservés hors du vol libre
execute as @a[tag=mg.efp] unless entity @s[x=16,y=63,z=-21,dx=0.99,dy=2.5,dz=0.99] run tag @s remove mg.efp
execute if score $setup mg.st matches 1 as @a[tag=!mg.efp,tag=!mg.play,tag=!mg.surv,tag=!mg.ely,gamemode=adventure,x=16,y=63,z=-21,dx=0.99,dy=2.5,dz=0.99] run function mg:elytra/free_pad
execute as @a[tag=mg.elyf] at @s run function mg:elytra/free_tick
execute if score $lan mg.t matches 20 run clear @a[tag=!mg.elyf] minecraft:elytra[minecraft:custom_data~{mg_elyf:1b}]
execute if score $lan mg.t matches 20 run clear @a[tag=!mg.elyf] minecraft:firework_rocket[minecraft:custom_data~{mg_elyf:1b}]
# Tableau à droite tournant (lobby) + reconstruction des ajouts du spawn s'ils ont été effacés
execute if score $setup mg.st matches 1 if score $state mg.st matches 0 if score $sb mg.st matches 1 run function mg:hall/board_tick
execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block -16 64 25 minecraft:gold_block run function mg:hall/build
execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block 24 63 19 minecraft:gold_block run function mg:lobby/food_build
execute as @a[scores={mg.rt=1..}] run function mg:rate/submit
execute if score $setup mg.st matches 1 if entity @a[x=-200,y=40,z=-60,dx=100,dy=80,dz=70] run function mg:coaster/tick
execute if score $setup mg.st matches 1 if entity @a[x=-200,y=40,z=-60,dx=125,dy=80,dz=70] run function mg:coaster/tick
execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block 16 63 -9 minecraft:sea_lantern run function mg:elytra/build
execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block 32 63 -15 minecraft:sea_lantern run function mg:elytra/build
execute if score $lan mg.t matches 20 run clear @a[tag=!mg.ely] minecraft:elytra[minecraft:custom_data~{mg_ely:1b}]
execute if score $lan mg.t matches 20 run clear @a[tag=!mg.ely] minecraft:firework_rocket[minecraft:custom_data~{mg_ely:1b}]
execute if score $lan mg.t matches 20 run clear @a[tag=!mg.play] minecraft:elytra[minecraft:custom_data~{mg_elyr:1b}]
execute if score $lan mg.t matches 20 run clear @a[tag=!mg.play] minecraft:firework_rocket[minecraft:custom_data~{mg_elyr:1b}]
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

# Compte à rebours : aucun tir (flèche, œuf, boule de neige, trident, perle, liste dans tags/entity_type/shot.json) ne part des joueurs gelés
# (les kits ne sont donnés qu'au GO : une flèche ou une perle tirée ici est perdue, accepté)
execute if score $state mg.st matches 1 as @a[tag=mg.play] at @s run kill @e[type=#mg:shot,distance=..8]
# Machine à états
execute if score $state mg.st matches 1 run function mg:core/countdown
execute if score $state mg.st matches 2 run function mg:core/game_tick
execute if score $state mg.st matches 3 run function mg:core/ending

# Hors partie : nettoyage de sécurité + rattrapage du vide
execute if score $state mg.st matches 0 as @a[tag=mg.play,tag=!mg.surv] run function mg:core/reset_player
execute if score $state mg.st matches 0 as @a[tag=mg.out,tag=!mg.surv] run function mg:core/reset_player
execute if score $state mg.st matches 0 run tag @a remove mg.play
execute if score $state mg.st matches 0 run tag @a remove mg.out
execute if score $state mg.st matches 0 as @a[gamemode=spectator,tag=!mg.visit,tag=!mg.surv,tag=!mg.lk] run function mg:core/back_to_lobby
execute as @a[tag=mg.init,tag=!mg.play,tag=!mg.out,tag=!mg.surv] at @s run function mg:core/void_catch

# Visiteurs de plots : confinés à la zone des plots
execute if entity @a[tag=mg.visit] run function mg:plot/visit_guard
