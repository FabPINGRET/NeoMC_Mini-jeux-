# @s = joueur qui lance un contre-la-montre solo (#xv = 10 : parcours au hasard, 10 + NUM : parcours NUM). Le lancement minimal de core/request :
# ni vote effacé, ni objets retirés aux autres, ni annonce de jeu ; seul @s est participant
execute unless score #xv mg.st matches 10..12 run return 0
execute unless score $setup mg.st matches 1 run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Installation manquante : un OP doit d'abord lancer /function mg:setup.","color":"red"}]
execute unless entity @s[tag=mg.init] run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Pas encore prêt : réessaie dans un instant.","color":"red"}]
execute if entity @s[tag=mg.surv] run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Impossible depuis la survie : reviens d'abord au lobby (/trigger mg.sv set 2).","color":"red"}]
execute if entity @s[tag=mg.spectate] run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Impossible en pause : désactive la pause (/trigger mg.opt set 1).","color":"red"}]
execute if entity @s[tag=mg.ely] run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Termine d'abord ton activité en cours (parcours d'élytra, élytres libres, kart libre ou parkour).","color":"red"}]
execute if entity @s[tag=mg.elyf] run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Termine d'abord ton activité en cours (parcours d'élytra, élytres libres, kart libre ou parkour).","color":"red"}]
execute if entity @s[tag=mg.lk] run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Termine d'abord ton activité en cours (parcours d'élytra, élytres libres, kart libre ou parkour).","color":"red"}]
execute if entity @s[tag=mg.pkr] run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Termine d'abord ton activité en cours (parcours d'élytra, élytres libres, kart libre ou parkour).","color":"red"}]
execute unless score $state mg.st matches 0 run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Une partie est déjà en cours : attends sa fin.","color":"red"}]
execute if score $mp mg.st matches 1 run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"La Mini Party est en cours.","color":"red"}]
execute if score $vat mg.st matches 1.. run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Un vote est sur le point de lancer un jeu : attends-le.","color":"red"}]
# délai depuis la fin du dernier solo ($xse, en ticks de $tc) : #xd = ticks écoulés (600 = pas d'attente) ; les admins en sont exemptés
scoreboard players set #xd mg.st 600
execute if score $xse mg.st matches 1.. run scoreboard players operation #xd mg.st = $tc mg.st
execute if score $xse mg.st matches 1.. run scoreboard players operation #xd mg.st -= $xse mg.st
scoreboard players set #xr mg.st 600
scoreboard players operation #xr mg.st -= #xd mg.st
scoreboard players operation #xr mg.st /= #k20 mg.st
scoreboard players add #xr mg.st 1
execute unless entity @s[tag=mg.admin] if score #xd mg.st matches 0..599 run return run tellraw @s [{"text":"⚠ Attends encore ","color":"red"},{"score":{"name":"#xr","objective":"mg.st"},"color":"red"},{"text":" s avant un nouveau solo.","color":"red"}]
# parcours : #xv = 10 (au hasard, tiré parmi les construits par pick) ou 10 + NUM ; refusé s'il n'est pas construit
scoreboard players set $xc mg.st 0
execute if score #xv mg.st matches 11.. run scoreboard players operation $xc mg.st = #xv mg.st
execute if score #xv mg.st matches 11.. run scoreboard players remove $xc mg.st 10
execute if score $xc mg.st matches 0 run function mg:elyrace/pick
execute if score $xc mg.st matches 0 run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Aucun parcours n'est construit pour le moment : réessaie plus tard.","color":"red"}]
execute if score $xc mg.st matches 1 unless data storage mg:elyrace v2 run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Le parcours 1 (Canyon du Couchant) n'est pas encore construit : réessaie plus tard.","color":"red"}]
execute if score $xc mg.st matches 2 unless data storage mg:elyrace c2v2 run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Le parcours 2 (Pic Blanc) n'est pas encore construit : réessaie plus tard.","color":"red"}]
# lancement : $xs avant $state (les gardes de end, timeout, draw, finish et cleanup lisent $xs)
scoreboard players set $xs mg.st 1
scoreboard players set $game mg.st 66
scoreboard players set $ar mg.st 0
tag @s add mg.play
tag @a remove mg.out
tag @a remove mg.win
scoreboard players set $n0 mg.st 1
execute if entity @s[tag=mg.inplot] run function mg:plot/leave_game
execute if entity @s[tag=mg.visit] run function mg:plot/leave_game
scoreboard players set $state mg.st 1
scoreboard players set $timer mg.st 100
scoreboard players set @s mg.deaths 0
scoreboard players reset @s mg.qs
scoreboard players reset @s mg.fw
scoreboard players reset @s mg.wc
scoreboard players reset @s mg.wd
scoreboard players reset @s mg.us
function mg:elyrace/solo/announce
function mg:elyrace/prepare
# prepare a annulé (parcours pas construit : CANCEL → elyrace/draw → solo/end) : pas de gel ni de titre
execute if score $state mg.st matches 3 run return 0
function mg:core/freeze
effect give @s minecraft:resistance 7 255 true
title @s title [{"text":"Prépare-toi !","color":"gold"}]
title @s subtitle [{"text":"Début dans 5 secondes...","color":"gray"}]
execute at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 0.8
