execute as @n[tag=pretzel_boss,distance=0..] at @s run playsound minecraft:entity.evoker.cast_spell hostile @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute as @n[tag=pretzel_boss,distance=0..] at @s run particle minecraft:firework ~ ~1 ~ 0.5 0.5 0.5 0 70
tp @n[tag=pretzel_boss,distance=0..] -10340 49 446
setblock -10341 89 445 minecraft:player_head[powered=false,rotation=6]{components:{},profile:{id:[I;1893713680,2085177240,-1513123797,-1170527382],properties:[{name:"textures",value:"ewogICJ0aW1lc3RhbXAiIDogMTc2MjEzNjY4MzMzMSwKICAicHJvZmlsZUlkIiA6ICJhODgyMzAzMDVkOWY0ODRiYjNjNjc2OTg1OTYxYjc2YSIsCiAgInByb2ZpbGVOYW1lIiA6ICJMb3JkRHJld3BpY3VzIiwKICAic2lnbmF0dXJlUmVxdWlyZWQiIDogdHJ1ZSwKICAidGV4dHVyZXMiIDogewogICAgIlNLSU4iIDogewogICAgICAidXJsIiA6ICJodHRwOi8vdGV4dHVyZXMubWluZWNyYWZ0Lm5ldC90ZXh0dXJlL2UzZWEyNGVkMTY5NjYzYzg5NjE4YTM1NmZjNWJiNmNlMDFkNjg4YmMyMzNkZmVmNTVhOTJmYWRjNDUxZGRjN2IiCiAgICB9CiAgfQp9"}]}}
scoreboard players set pretzel_since_sword Value 0

function boss:mini/pretzel/schedule_attack
