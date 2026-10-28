# PvP actif ? 3 min après une régénération (faite avec des joueurs), ou la phase au hasard du cycle
scoreboard players set #pv mg.st 0
execute if score $fnrp mg.st matches 1 if score $fnt mg.st matches ..179 run scoreboard players set #pv mg.st 1
scoreboard players operation #pe mg.st = $fnpr mg.st
scoreboard players add #pe mg.st 180
execute if score $fnt mg.st >= $fnpr mg.st if score $fnt mg.st < #pe mg.st run scoreboard players set #pv mg.st 1
execute if score #pv mg.st matches 1 unless score $fnpvp mg.st matches 1 run tellraw @a[tag=mg.fnw] {"text":"⚔ PvP OUVERT dans la mine (3 min) ! En surface, tu ne crains rien.","color":"red","bold":true}
execute if score #pv mg.st matches 1 unless score $fnpvp mg.st matches 1 as @a[tag=mg.fnw] at @s run playsound minecraft:event.raid.horn master @s ~ ~ ~ 0.6 1.2
execute if score #pv mg.st matches 0 if score $fnpvp mg.st matches 1 run tellraw @a[tag=mg.fnw] {"text":"🕊 Fin du PvP : la mine redevient paisible.","color":"green"}
execute if score #pv mg.st matches 0 if score $fnpvp mg.st matches 1 run team join mg_fn @a[tag=mg.fnw]
scoreboard players operation $fnpvp mg.st = #pv mg.st
execute if score $fnt mg.st matches 180.. run scoreboard players set $fnrp mg.st 0
