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
scoreboard players enable @a mg.duel
execute if score $setup mg.st matches 1 run function mg:gun/cl_tick
function mg:gta/pre_tick
function mg:terra/pre_tick
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
execute if score $setup mg.st matches 1 if entity @a[x=-12,y=40,z=-10,dx=51,dy=20,dz=45] run function mg:pvpc/tick
execute if score $setup mg.st matches 1 unless entity @a[x=-12,y=40,z=-10,dx=51,dy=20,dz=45] if entity @a[tag=mg.pvpc] run function mg:pvpc/tick
execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 if loaded 13 53 5 unless block 13 53 5 minecraft:lodestone run function mg:pvpc/build
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
execute if entity @a[tag=mg.xso] run function mg:elyrace/solo/tick
# Duel sniper : commandes, puis boucle (duellistes, ou invitations en attente)
execute as @a[scores={mg.duel=1..}] run function mg:duel/cmd
execute if entity @a[tag=mg.dl] run function mg:duel/tick
execute unless entity @a[tag=mg.dl] if entity @a[scores={mg.dlto=1..}] run function mg:duel/tick
execute unless entity @a[tag=mg.dl] unless entity @a[scores={mg.dlto=1..}] if entity @a[tag=mg.dlrq] run function mg:duel/tick

# Armurerie du lobby
execute if score $setup mg.st matches 1 run function mg:lobby/guns_tick
execute if score $setup mg.st matches 1 run function mg:lobby/armory_tick
execute if score $setup mg.st matches 1 run function mg:lobby/ev/tick
execute if score $theme mg.st matches 1.. run function mg:lobby/theme/tick
execute if score $thrs mg.st matches 1.. if entity @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] run function mg:lobby/theme/restore
execute if score $lan mg.t matches 30 unless score $theme mg.st matches 1.. unless data storage mg:lobby theme as @e[tag=mg.thmob] run function mg:lobby/theme/gone
execute if score $lan mg.t matches 30 unless score $theme mg.st matches 1.. unless data storage mg:lobby theme run kill @e[tag=mg.thnpc]
function mg:hat/tick
scoreboard players remove @a[scores={mg.fd=1..}] mg.fd 1
# Parcours d'élytra : socle de départ, joueurs en vol, objets du parcours jamais conservés
execute if score $setup mg.st matches 1 as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.ely,tag=!mg.pkr,gamemode=adventure,x=16,y=63,z=-9,dx=0.99,dy=2.5,dz=0.99] run function mg:elytra/start
execute if score $setup mg.st matches 1 as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.ely,tag=!mg.pkr,gamemode=adventure,x=32,y=63,z=-15,dx=0.99,dy=2.5,dz=0.99] run function mg:elytra/start2
execute as @a[tag=mg.ely] at @s run function mg:elytra/player
# Élytres libres : socle (une fois par passage), joueurs en vol, objets jamais conservés hors du vol libre
execute as @a[tag=mg.efp] unless entity @s[x=16,y=63,z=-21,dx=0.99,dy=2.5,dz=0.99] run tag @s remove mg.efp
execute if score $setup mg.st matches 1 as @a[tag=!mg.efp,tag=!mg.play,tag=!mg.surv,tag=!mg.ely,gamemode=adventure,x=16,y=63,z=-21,dx=0.99,dy=2.5,dz=0.99] run function mg:elytra/free_pad
execute as @a[tag=mg.elyf] at @s run function mg:elytra/free_tick
execute if score $lan mg.t matches 20 run clear @a[tag=!mg.elyf] minecraft:elytra[minecraft:custom_data~{mg_elyf:1b}]
execute if score $lan mg.t matches 20 run clear @a[tag=!mg.elyf] minecraft:firework_rocket[minecraft:custom_data~{mg_elyf:1b}]
# Tableau à droite tournant (lobby) + reconstruction des ajouts du spawn s'ils ont été effacés
execute if score $setup mg.st matches 1 if score $state mg.st matches 0 if score $sbm mg.st matches 0 run function mg:hall/board_tick
execute if score $setup mg.st matches 1 if score $lan mg.t matches 5 run function mg:sb/auto
execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block -9 64 27 minecraft:gold_block run function mg:hall/build
execute if score $setup mg.st matches 1 if score $lan mg.t matches 12 run function mg:hall/t3_tick
execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block 24 63 19 minecraft:gold_block run function mg:lobby/food_build
execute if score $setup mg.st matches 1 if entity @a[x=-75,y=55,z=-75,dx=150,dy=60,dz=150] run function mg:coaster/tick
execute if score $lan mg.t matches 15 run function mg:rank/tick
execute as @a[scores={mg.rt=1..}] run function mg:rate/submit
execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block 16 63 -9 minecraft:sea_lantern run function mg:elytra/build
execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block 32 63 -15 minecraft:sea_lantern run function mg:elytra/build
# Panneaux flottants des 3 socles d'élytra (6 text_display) : reconstruits s'il en manque un
execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 store result score $eld mg.t if entity @e[type=minecraft:text_display,tag=mg.elyd,x=14,y=66,z=-23,dx=21,dy=3,dz=17]
execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 if score $eld mg.t matches ..5 if score $thrs mg.st matches 0 run function mg:elytra/build
execute if score $lan mg.t matches 20 run clear @a[tag=!mg.ely] minecraft:elytra[minecraft:custom_data~{mg_ely:1b}]
execute if score $lan mg.t matches 20 run clear @a[tag=!mg.ely] minecraft:firework_rocket[minecraft:custom_data~{mg_ely:1b}]
execute if score $lan mg.t matches 20 run clear @a[tag=!mg.play,tag=!mg.xso] minecraft:elytra[minecraft:custom_data~{mg_elyr:1b}]
execute if score $lan mg.t matches 20 run clear @a[tag=!mg.play,tag=!mg.xso] minecraft:firework_rocket[minecraft:custom_data~{mg_elyr:1b}]
execute if score $setup mg.st matches 1 as @a[tag=!mg.play,tag=!mg.surv,gamemode=adventure,x=24,y=63,z=19,dx=0.99,dy=2.5,dz=0.99] run function mg:lobby/food_give

# Kart libre du spawn
execute if score $setup mg.st matches 1 run function mg:lobkart/tick
# Neo City (monde GTA) : portail du lobby et session
function mg:gta/lobby_tick
function mg:terra/lobby_tick

# Parkour du lobby
execute if score $setup mg.st matches 1 run function mg:parkour/tick

# Plots des joueurs
execute as @a[scores={mg.pl=1..}] run function mg:plot/cmd
execute if score $setup mg.st matches 1 run function mg:plot/tick

# Canne ≡ MENU : refilée aux admins dès que leur inventaire est libre (toutes les 2 s ; hors partie, plot créatif, parkour, spectateur, créatif)
scoreboard players add $gmt mg.t 1
execute if score $gmt mg.t matches 40.. as @a[tag=mg.admin,tag=mg.init,tag=!mg.surv,tag=!mg.play,tag=!mg.out,tag=!mg.inplot,tag=!mg.pkr,tag=!mg.lk,tag=!mg.visit,tag=!mg.dl,gamemode=!spectator,gamemode=!creative] run function mg:core/give_menu_safe
execute if score $gmt mg.t matches 40.. run scoreboard players set $gmt mg.t 0

# Compte à rebours : aucun tir (flèche, œuf, boule de neige, trident, perle, liste dans tags/entity_type/shot.json) ne part des joueurs gelés
# (les kits ne sont donnés qu'au GO : une flèche ou une perle tirée ici est perdue, accepté)
execute if score $state mg.st matches 1 as @a[tag=mg.play] at @s run kill @e[type=#mg:shot,distance=..8]
# Machine à états
execute if score $state mg.st matches 1 run function mg:core/countdown
execute as @a[tag=mg.frz] run function mg:core/freeze_hold
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
execute if entity @a[tag=mg.sit] run function mg:lobby/sit/tick
execute if score $lan mg.t matches 30 unless entity @a[tag=mg.sit] if entity @e[type=minecraft:item_display,tag=mg.seat,limit=1] run kill @e[type=minecraft:item_display,tag=mg.seat]
