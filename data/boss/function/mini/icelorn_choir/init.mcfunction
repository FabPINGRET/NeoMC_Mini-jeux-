bossbar set boss:icelorn_choir value 130
bossbar set boss:icelorn_choir color green
bossbar set boss:icelorn_choir players

kill @e[tag=icelorn_singer,distance=0..]
kill @e[tag=icelorn_organist,distance=0..]
kill @e[tag=icelorn_corpse,distance=0..]
summon armor_stand -10081 129 164 {NoGravity:1b,Silent:1b,Invulnerable:1b,ShowArms:1b,Small:1b,NoBasePlate:1b,PersistenceRequired:1b,Tags:["icelorn_organist"],attributes:[{id:"minecraft:scale",base:2}],Pose:{Head:[20f,0f,0f]},DisabledSlots:4144959,Rotation:[-45F,0F],equipment:{feet:{id:"minecraft:leather_boots",count:1,components:{dyed_color:1908001,trim:{material:"minecraft:netherite",pattern:"minecraft:rib"}}},legs:{id:"minecraft:leather_leggings",count:1,components:{dyed_color:1908001,trim:{material:"minecraft:netherite",pattern:"minecraft:rib"}}},chest:{id:"minecraft:leather_chestplate",count:1,components:{dyed_color:1908001,trim:{material:"minecraft:netherite",pattern:"minecraft:rib"}}},head:{id:"minecraft:player_head",count:1,components:{profile:{properties:[{name:"textures",value:"ewogICJ0aW1lc3RhbXAiIDogMTc1NDE0MzUyODEwOSwKICAicHJvZmlsZUlkIiA6ICJhODgyMzAzMDVkOWY0ODRiYjNjNjc2OTg1OTYxYjc2YSIsCiAgInByb2ZpbGVOYW1lIiA6ICJMb3JkRHJld3BpY3VzIiwKICAic2lnbmF0dXJlUmVxdWlyZWQiIDogdHJ1ZSwKICAidGV4dHVyZXMiIDogewogICAgIlNLSU4iIDogewogICAgICAidXJsIiA6ICJodHRwOi8vdGV4dHVyZXMubWluZWNyYWZ0Lm5ldC90ZXh0dXJlLzE4NThhNTIyNjAzYjhiMTNmYzBjMzc3ZTMwYzBmMGViZTM4MzhlMzZjOTgwNWRlMDViMDE4NTZlMTAyMTc0ZDIiCiAgICB9CiAgfQp9"}]}}}}}

function boss:mini/icelorn_choir/song/no_inst
function boss:mini/icelorn_choir/song/stop
function boss:mini/icelorn_choir/speed/3

execute as @n[tag=icelorn_pivot,distance=0..] at @s run tp @s ~ ~ ~ 0 0

#clear summons
fill -10086 105 196 -10060 105 196 air

scoreboard players set icelorn_overdrive bool 0
