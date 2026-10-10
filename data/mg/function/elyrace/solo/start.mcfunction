# @s = joueur qui lance un contre-la-montre solo (#xv = 10 : parcours au hasard, 10 + NUM : parcours NUM). Rien de global : ni $state, ni vote effacé,
# ni objets retirés aux autres, ni annonce de jeu ; le joueur est mis en pause (mg.spectate), seul son état change
execute unless score #xv mg.st matches 10..12 run return 0
execute unless score $setup mg.st matches 1 run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Installation manquante : un OP doit d'abord lancer /function mg:setup.","color":"red"}]
execute unless entity @s[tag=mg.init] run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Pas encore prêt : réessaie dans un instant.","color":"red"}]
execute if entity @s[tag=mg.play] run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Impossible pendant que tu participes à une partie.","color":"red"}]
execute if entity @s[tag=mg.out] run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Impossible : tu regardes la partie en cours en spectateur.","color":"red"}]
execute if entity @s[tag=mg.xso] run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Tu es déjà en contre-la-montre solo.","color":"red"}]
execute if entity @s[gamemode=spectator] run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Impossible en mode spectateur.","color":"red"}]
execute if entity @s[tag=mg.ely] run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Termine d'abord ton activité en cours (parcours d'élytra, élytres libres, kart libre ou parkour).","color":"red"}]
execute if entity @s[tag=mg.elyf] run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Termine d'abord ton activité en cours (parcours d'élytra, élytres libres, kart libre ou parkour).","color":"red"}]
execute if entity @s[tag=mg.lk] run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Termine d'abord ton activité en cours (parcours d'élytra, élytres libres, kart libre ou parkour).","color":"red"}]
execute if entity @s[tag=mg.pkr] run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Termine d'abord ton activité en cours (parcours d'élytra, élytres libres, kart libre ou parkour).","color":"red"}]
execute if entity @s[tag=mg.surv] run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Impossible depuis la survie : reviens d'abord au lobby (/trigger mg.sv set 2).","color":"red"}]
execute if entity @s[tag=mg.inplot] run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Impossible depuis un plot : reviens d'abord au lobby.","color":"red"}]
execute if entity @s[tag=mg.visit] run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Impossible depuis un plot : reviens d'abord au lobby.","color":"red"}]
execute if score $mp mg.st matches 1 if entity @s[tag=mg.mpp] run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Tu participes à la Mini Party : attends sa fin.","color":"red"}]
execute if score $game mg.st matches 66 if score $state mg.st matches 1..3 run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Une course d'élytres de groupe est en cours : attends sa fin.","color":"red"}]
execute store result score #xn mg.st if entity @a[tag=mg.xso]
execute if score #xn mg.st matches 4.. run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Déjà 4 contre-la-montre solo en cours : attends qu'un se termine.","color":"red"}]
# délai depuis la fin du dernier solo du joueur (@s mg.xse, en ticks de $tc) : #xd = ticks écoulés (600 = pas d'attente) ; les admins en sont exemptés
scoreboard players set #xd mg.st 600
execute if score @s mg.xse matches 1.. run scoreboard players operation #xd mg.st = $tc mg.st
execute if score @s mg.xse matches 1.. run scoreboard players operation #xd mg.st -= @s mg.xse
scoreboard players set #xr mg.st 600
scoreboard players operation #xr mg.st -= #xd mg.st
scoreboard players operation #xr mg.st /= #k20 mg.st
scoreboard players add #xr mg.st 1
execute unless entity @s[tag=mg.admin] if score #xd mg.st matches 0..599 run return run tellraw @s [{"text":"⚠ Attends encore ","color":"red"},{"score":{"name":"#xr","objective":"mg.st"},"color":"red"},{"text":" s avant un nouveau solo.","color":"red"}]
# parcours : #xv = 10 (au hasard, tiré parmi les construits par pick) ou 10 + NUM ; refusé s'il n'est pas construit
# ($xc sert de brouillon à pick : jamais lu pendant un solo ; remis à 0 par le refus « pas construit » ci-dessous, ou au lancement ; un lancement de groupe le repose lui-même)
scoreboard players set $xc mg.st 0
execute if score #xv mg.st matches 11.. run scoreboard players operation $xc mg.st = #xv mg.st
execute if score #xv mg.st matches 11.. run scoreboard players remove $xc mg.st 10
execute if score $xc mg.st matches 0 run function mg:elyrace/pick
execute if score $xc mg.st matches 0 run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Aucun parcours n'est construit pour le moment : réessaie plus tard.","color":"red"}]
execute if score $xc mg.st matches 1 unless data storage mg:elyrace v3 run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Le parcours 1 (Canyon du Couchant) n'est pas encore construit : réessaie plus tard.","color":"red"}]
execute if score $xc mg.st matches 1 unless data storage mg:elyrace v3 run return run scoreboard players set $xc mg.st 0
execute if score $xc mg.st matches 2 unless data storage mg:elyrace c2v3 run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Le parcours 2 (Pic Blanc) n'est pas encore construit : réessaie plus tard.","color":"red"}]
execute if score $xc mg.st matches 2 unless data storage mg:elyrace c2v3 run return run scoreboard players set $xc mg.st 0
# lancement (plus aucun refus après ce point). La pause d'avant est mémorisée, puis le joueur passe en pause SANS opt_spec (il bascule,
# affiche des messages trompeurs et élimine un participant) ; son vote éventuel ne compte plus
execute if entity @s[tag=mg.spectate] run tag @s add mg.xsp0
tag @s add mg.spectate
scoreboard players reset @s mg.vc
execute if score $state mg.st matches 0 run function mg:vote/refresh
tag @s add mg.xso
scoreboard players operation @s mg.xcr = $xc mg.st
scoreboard players set $xc mg.st 0
# état du solo : phase 1 (décompte), chrono à 0 ; mg.xsl = tick précédent (le tick de ce lancement compte comme « vu »)
scoreboard players set @s mg.xph 1
scoreboard players set @s mg.xst 0
scoreboard players operation @s mg.xsl = $tc mg.st
scoreboard players remove @s mg.xsl 1
scoreboard players set @s mg.deaths 0
scoreboard players set @s mg.xa 0
scoreboard players set @s mg.xo 0
scoreboard players set @s mg.xc 0
scoreboard players set @s mg.xh 3
scoreboard players set @s mg.xp 0
scoreboard players set @s mg.xx 0
scoreboard players set @s mg.xg 0
scoreboard players set @s mg.xn 0
scoreboard players set @s mg.xl 0
scoreboard players set @s mg.xk 0
scoreboard players set @s mg.xf 0
scoreboard players set @s mg.xb1 0
scoreboard players set @s mg.xb2 0
scoreboard players set @s mg.xb3 0
scoreboard players set @s mg.xq1 0
scoreboard players set @s mg.xq2 0
scoreboard players set @s mg.xq3 0
scoreboard players set @s mg.xu 0
scoreboard players set @s mg.xft 0
scoreboard players reset @s mg.qs
scoreboard players reset @s mg.fw
scoreboard players reset @s mg.wc
scoreboard players reset @s mg.wd
scoreboard players reset @s mg.us
# place de départ libre : la plus petite que les autres solos n'occupent pas (au plus 4 solos : il y en a toujours une)
scoreboard players set @s mg.ri 0
execute if score @s mg.ri matches 0 unless entity @a[tag=mg.xso,scores={mg.ri=1}] run scoreboard players set @s mg.ri 1
execute if score @s mg.ri matches 0 unless entity @a[tag=mg.xso,scores={mg.ri=2}] run scoreboard players set @s mg.ri 2
execute if score @s mg.ri matches 0 unless entity @a[tag=mg.xso,scores={mg.ri=3}] run scoreboard players set @s mg.ri 3
execute if score @s mg.ri matches 0 unless entity @a[tag=mg.xso,scores={mg.ri=4}] run scoreboard players set @s mg.ri 4
gamemode adventure @s
effect clear @s
clear @s
function mg:elyrace/equip
execute if score @s mg.xcr matches 1 run spawnpoint @s 24 281 27000
execute if score @s mg.xcr matches 2 run spawnpoint @s 24 282 29600
function mg:elyrace/place_tp
function mg:core/freeze
effect give @s minecraft:resistance 7 255 true
function mg:elyrace/solo/announce
title @s title [{"text":"Prépare-toi !","color":"gold"}]
title @s subtitle [{"text":"Début dans 5 secondes...","color":"gray"}]
execute at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 0.8
