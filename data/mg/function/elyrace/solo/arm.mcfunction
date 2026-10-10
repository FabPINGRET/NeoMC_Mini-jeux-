# @s = joueur en solo (mg.xso, parcours mg.xcr et place de départ mg.ri déjà posés) : phase 1 (décompte), chrono à 0, TOUT l'état de course
# remis à zéro (G.OBJECTIVES : ors mg.xu / mg.xo, classement mg.xft, arrivée mg.xf, reprise, origine du balayage, cœurs...), équipement,
# départ gelé, titres. Appelé par solo/start et par solo/retry (« Rejouer », phase 4) : ni tag, ni pause, ni annonce ici
scoreboard players set @s mg.xph 1
scoreboard players set @s mg.xst 0
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
gamemode adventure @s
effect clear @s
clear @s
function mg:elyrace/equip
execute if score @s mg.xcr matches 1 run spawnpoint @s 24 281 27000
execute if score @s mg.xcr matches 2 run spawnpoint @s 24 282 29600
function mg:elyrace/place_tp
function mg:core/freeze
effect give @s minecraft:resistance 7 255 true
title @s title [{"text":"Prépare-toi !","color":"gold"}]
title @s subtitle [{"text":"Début dans 5 secondes...","color":"gray"}]
execute at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 0.8
