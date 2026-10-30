execute if entity @a[tag=bossroom,tag=mg.flw] unless score boss:cob BossHealth matches 1 run function boss:2/fireball_shoot

scoreboard players add boss:cob Countdown 1

execute if score boss:cob Countdown matches 20 positioned -10116 153 -13 as @a[gamemode=!spectator,tag=mg.flw] run function summon:ossein_infantry
execute if score boss:cob Countdown matches 20 positioned -10144 153 -49 as @a[gamemode=!spectator,tag=mg.flw] run function summon:ossein_infantry
execute if score boss:cob Countdown matches 20 positioned -10116 153 -49 as @a[gamemode=!spectator,tag=mg.flw] run function summon:ossein_archer
execute if score boss:cob Countdown matches 20 positioned -10144 153 -13 as @a[gamemode=!spectator,tag=mg.flw] run function summon:ossein_archer

execute if score boss:cob Countdown matches 20 run scoreboard players set boss:cob Countdown 0

setblock -10124 138 -58 stone
