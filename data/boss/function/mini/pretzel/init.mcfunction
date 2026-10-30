bossbar set boss:pretzel value 100
bossbar set boss:pretzel color green
bossbar set boss:pretzel players

setblock -10341 89 445 minecraft:player_head[powered=false,rotation=6]{components:{},profile:{id:[I;1893713680,2085177240,-1513123797,-1170527382],properties:[{name:"textures",value:"ewogICJ0aW1lc3RhbXAiIDogMTc2MjEzNjY4MzMzMSwKICAicHJvZmlsZUlkIiA6ICJhODgyMzAzMDVkOWY0ODRiYjNjNjc2OTg1OTYxYjc2YSIsCiAgInByb2ZpbGVOYW1lIiA6ICJMb3JkRHJld3BpY3VzIiwKICAic2lnbmF0dXJlUmVxdWlyZWQiIDogdHJ1ZSwKICAidGV4dHVyZXMiIDogewogICAgIlNLSU4iIDogewogICAgICAidXJsIiA6ICJodHRwOi8vdGV4dHVyZXMubWluZWNyYWZ0Lm5ldC90ZXh0dXJlL2UzZWEyNGVkMTY5NjYzYzg5NjE4YTM1NmZjNWJiNmNlMDFkNjg4YmMyMzNkZmVmNTVhOTJmYWRjNDUxZGRjN2IiCiAgICB9CiAgfQp9"}]}}

kill @n[tag=pretzel_boss,distance=0..]

scoreboard players set pretzel_box_tick Value 0
scoreboard players set pretzel_since_sword Value 0
scoreboard players set pretzel_lastattack Value 0

#Stop tick
fill -10327 62 458 -10324 61 462 air replace minecraft:redstone_block
