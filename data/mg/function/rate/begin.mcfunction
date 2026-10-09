# Début de partie : clé de la carte ($rgid → storage mg:rate key.m) et du jeu (key.f, key.g) ; les notes en attente expirent. Généré.
# (épreuves d'une Mini Party : on garde la Mini Party elle-même)
execute if score $mp mg.st matches 1 unless score $game mg.st matches 59 run return 0
tag @a remove mg.rate
execute if score $rgid mg.st matches 27 run function mg:rate/fix {base:67,s:"$ttm"}
execute if score $rgid mg.st matches 4 run function mg:rate/fix {base:71,s:"$bwm"}
execute if score $rgid mg.st matches 78 run function mg:rate/fix {base:74,s:"$elm"}
execute store result storage mg:rate key.m int 1 run scoreboard players get $rgid mg.st
data modify storage mg:rate key.f set value ""
data modify storage mg:rate key.g set value 0
execute if score $game mg.st matches 1 run data modify storage mg:rate key merge value {f:"spleef",g:1}
execute if score $game mg.st matches 2 run data modify storage mg:rate key merge value {f:"tntrun",g:2}
execute if score $game mg.st matches 3 run data modify storage mg:rate key merge value {f:"pvp",g:3}
execute if score $game mg.st matches 4 run data modify storage mg:rate key merge value {f:"bedwars",g:4}
execute if score $game mg.st matches 5 run data modify storage mg:rate key merge value {f:"sheepwar",g:5}
execute if score $game mg.st matches 7 run data modify storage mg:rate key merge value {f:"sheepwar",g:5}
execute if score $game mg.st matches 6 run data modify storage mg:rate key merge value {f:"mobarena",g:6}
execute if score $game mg.st matches 20..21 run data modify storage mg:rate key merge value {f:"splegg",g:7}
execute if score $game mg.st matches 22 run data modify storage mg:rate key merge value {f:"sumo",g:8}
execute if score $game mg.st matches 23 run data modify storage mg:rate key merge value {f:"dropper",g:9}
execute if score $game mg.st matches 64..65 run data modify storage mg:rate key merge value {f:"dropper",g:9}
execute if score $game mg.st matches 26 run data modify storage mg:rate key merge value {f:"oitc",g:10}
execute if score $game mg.st matches 27 run data modify storage mg:rate key merge value {f:"tnttag",g:11}
execute if score $game mg.st matches 28 run data modify storage mg:rate key merge value {f:"blockparty",g:12}
execute if score $game mg.st matches 29 run data modify storage mg:rate key merge value {f:"anvil",g:13}
execute if score $game mg.st matches 30 run data modify storage mg:rate key merge value {f:"turf",g:14}
execute if score $game mg.st matches 31 run data modify storage mg:rate key merge value {f:"quake",g:15}
execute if score $game mg.st matches 36 run data modify storage mg:rate key merge value {f:"paintball",g:16}
execute if score $game mg.st matches 56 run data modify storage mg:rate key merge value {f:"icerace",g:17}
execute if score $game mg.st matches 57..58 run data modify storage mg:rate key merge value {f:"bb",g:18}
execute if score $game mg.st matches 59..60 run data modify storage mg:rate key merge value {f:"party",g:19}
execute if score $game mg.st matches 61..63 run data modify storage mg:rate key merge value {f:"kart",g:20}
execute if score $game mg.st matches 66 run data modify storage mg:rate key merge value {f:"elyrace",g:21}
execute if score $game mg.st matches 75 run data modify storage mg:rate key merge value {f:"elytra",g:22}
execute if score $game mg.st matches 83 run data modify storage mg:rate key merge value {f:"telephone",g:23}
execute if score $game mg.st matches 84..85 run data modify storage mg:rate key merge value {f:"tron",g:24}
execute if score $game mg.st matches 86..87 run data modify storage mg:rate key merge value {f:"koth",g:25}
execute if score $game mg.st matches 88 run data modify storage mg:rate key merge value {f:"tower",g:26}
execute if score $game mg.st matches 89..90 run data modify storage mg:rate key merge value {f:"convoy",g:27}
execute if score $game mg.st matches 93 run data modify storage mg:rate key merge value {f:"ctf",g:28}
execute if score $game mg.st matches 94 run data modify storage mg:rate key merge value {f:"uhc",g:29}
execute if score $game mg.st matches 95 run data modify storage mg:rate key merge value {f:"hg",g:30}
execute if score $game mg.st matches 96 run data modify storage mg:rate key merge value {f:"prophunt",g:31}
execute if score $game mg.st matches 97 run data modify storage mg:rate key merge value {f:"zombies",g:32}
execute if score $game mg.st matches 98 run data modify storage mg:rate key merge value {f:"infection",g:33}
execute store result score $rgf mg.st run data get storage mg:rate key.g
