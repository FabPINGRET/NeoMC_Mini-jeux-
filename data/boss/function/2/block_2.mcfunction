clone -10112 137 -40 -10110 139 -15 -10124 153 -37
scoreboard players set @a[gamemode=!spectator,tag=mg.flw] ScreenShake 1
schedule function floaty:sched/game/screenshake_end 1s replace
kill @e[tag=closed_1,tag=ck_eye,distance=0..]
kill @e[tag=closed_2,tag=ck_eye,distance=0..]
kill @e[tag=closed_6,tag=ck_eye,distance=0..]
summon armor_stand -10119 153.78125 -19 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["ck_eye","tentacle_1"],equipment:{head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYThkODdjNWFmYWFiMTA5YmFhM2Y2MzA1OWI4ODBlODQ1ZTA0ZjU0ZTJiZGQ5NTc0YjY2NjY1NzQ4ZmNiY2E3YyJ9fX0="}]}}}}}
summon armor_stand -10118 153.78125 -38 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["ck_eye","tentacle_2"],equipment:{head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYThkODdjNWFmYWFiMTA5YmFhM2Y2MzA1OWI4ODBlODQ1ZTA0ZjU0ZTJiZGQ5NTc0YjY2NjY1NzQ4ZmNiY2E3YyJ9fX0="}]}}}}}
summon armor_stand -10135 153.78125 -43 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["ck_eye","tentacle_6"],equipment:{head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYThkODdjNWFmYWFiMTA5YmFhM2Y2MzA1OWI4ODBlODQ1ZTA0ZjU0ZTJiZGQ5NTc0YjY2NjY1NzQ4ZmNiY2E3YyJ9fX0="}]}}}}}
