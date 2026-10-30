clone -10112 140 -40 -10110 142 -15 -10138 153 -50
scoreboard players set @a[gamemode=!spectator,tag=mg.flw] ScreenShake 1
schedule function floaty:sched/game/screenshake_end 1s replace
kill @e[tag=closed_3,tag=ck_eye,distance=0..]
kill @e[tag=closed_4,tag=ck_eye,distance=0..]
kill @e[tag=closed_5,tag=ck_eye,distance=0..]
summon armor_stand -10130 153.78125 -26 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["ck_eye","tentacle_3"],equipment:{head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYThkODdjNWFmYWFiMTA5YmFhM2Y2MzA1OWI4ODBlODQ1ZTA0ZjU0ZTJiZGQ5NTc0YjY2NjY1NzQ4ZmNiY2E3YyJ9fX0="}]}}}}}
summon armor_stand -10126 153.78125 -36 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["ck_eye","tentacle_4"],equipment:{head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYThkODdjNWFmYWFiMTA5YmFhM2Y2MzA1OWI4ODBlODQ1ZTA0ZjU0ZTJiZGQ5NTc0YjY2NjY1NzQ4ZmNiY2E3YyJ9fX0="}]}}}}}
summon armor_stand -10136 153.78125 -17 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["ck_eye","tentacle_5"],equipment:{head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYThkODdjNWFmYWFiMTA5YmFhM2Y2MzA1OWI4ODBlODQ1ZTA0ZjU0ZTJiZGQ5NTc0YjY2NjY1NzQ4ZmNiY2E3YyJ9fX0="}]}}}}}
