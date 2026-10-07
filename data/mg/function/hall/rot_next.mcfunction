# Tableau suivant ayant au moins un score (sinon victoires)
scoreboard players add $rot mg.st 1
execute unless score $rot mg.st matches 1..23 run scoreboard players set $rot mg.st 1
scoreboard players add $rtry mg.st 1
execute if score $rtry mg.st matches 24.. run return run scoreboard objectives setdisplay sidebar mg.wins
execute if score $rot mg.st matches 1 if score #any mg.wins matches 1.. run return run scoreboard objectives setdisplay sidebar mg.wins
execute if score $rot mg.st matches 2 if score #any mg.stp matches 1.. run return run scoreboard objectives setdisplay sidebar mg.stp
execute if score $rot mg.st matches 3 if score #any mg.stk matches 1.. run return run scoreboard objectives setdisplay sidebar mg.stk
execute if score $rot mg.st matches 4 if score #any mg.wg_spleef matches 1.. run return run scoreboard objectives setdisplay sidebar mg.wg_spleef
execute if score $rot mg.st matches 5 if score #any mg.wg_tntrun matches 1.. run return run scoreboard objectives setdisplay sidebar mg.wg_tntrun
execute if score $rot mg.st matches 6 if score #any mg.wg_pvp matches 1.. run return run scoreboard objectives setdisplay sidebar mg.wg_pvp
execute if score $rot mg.st matches 7 if score #any mg.wg_bedwars matches 1.. run return run scoreboard objectives setdisplay sidebar mg.wg_bedwars
execute if score $rot mg.st matches 8 if score #any mg.wg_sheepwar matches 1.. run return run scoreboard objectives setdisplay sidebar mg.wg_sheepwar
execute if score $rot mg.st matches 9 if score #any mg.wg_mobarena matches 1.. run return run scoreboard objectives setdisplay sidebar mg.wg_mobarena
execute if score $rot mg.st matches 10 if score #any mg.wg_splegg matches 1.. run return run scoreboard objectives setdisplay sidebar mg.wg_splegg
execute if score $rot mg.st matches 11 if score #any mg.wg_sumo matches 1.. run return run scoreboard objectives setdisplay sidebar mg.wg_sumo
execute if score $rot mg.st matches 12 if score #any mg.wg_dropper matches 1.. run return run scoreboard objectives setdisplay sidebar mg.wg_dropper
execute if score $rot mg.st matches 13 if score #any mg.wg_oitc matches 1.. run return run scoreboard objectives setdisplay sidebar mg.wg_oitc
execute if score $rot mg.st matches 14 if score #any mg.wg_tnttag matches 1.. run return run scoreboard objectives setdisplay sidebar mg.wg_tnttag
execute if score $rot mg.st matches 15 if score #any mg.wg_blockparty matches 1.. run return run scoreboard objectives setdisplay sidebar mg.wg_blockparty
execute if score $rot mg.st matches 16 if score #any mg.wg_anvil matches 1.. run return run scoreboard objectives setdisplay sidebar mg.wg_anvil
execute if score $rot mg.st matches 17 if score #any mg.wg_turf matches 1.. run return run scoreboard objectives setdisplay sidebar mg.wg_turf
execute if score $rot mg.st matches 18 if score #any mg.wg_quake matches 1.. run return run scoreboard objectives setdisplay sidebar mg.wg_quake
execute if score $rot mg.st matches 19 if score #any mg.wg_paintball matches 1.. run return run scoreboard objectives setdisplay sidebar mg.wg_paintball
execute if score $rot mg.st matches 20 if score #any mg.wg_icerace matches 1.. run return run scoreboard objectives setdisplay sidebar mg.wg_icerace
execute if score $rot mg.st matches 21 if score #any mg.wg_bb matches 1.. run return run scoreboard objectives setdisplay sidebar mg.wg_bb
execute if score $rot mg.st matches 22 if score #any mg.wg_party matches 1.. run return run scoreboard objectives setdisplay sidebar mg.wg_party
execute if score $rot mg.st matches 23 if score #any mg.wg_kart matches 1.. run return run scoreboard objectives setdisplay sidebar mg.wg_kart
function mg:hall/rot_next
