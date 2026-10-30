scoreboard players set boss:skt_ectobeam shortray 0
execute positioned -10222 98 434 facing entity @r[gamemode=!spectator,tag=bossroom,tag=mg.flw] eyes run function boss:5/ectobeam/ray

schedule function floaty:sched/boss/5/ectobeam/slime_position 1t
schedule function floaty:sched/boss/5/ectobeam/detonate 2s replace
