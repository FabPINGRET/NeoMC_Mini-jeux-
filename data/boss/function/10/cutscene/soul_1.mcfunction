summon armor_stand -11830 217 330 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["npc","ta_soul_display","ta_soul_display_final"],DisabledSlots:4144959,equipment:{head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{"properties":[{"name":"textures","value":"ewogICJ0aW1lc3RhbXAiIDogMTc2MzMwNTc4NDAwOSwKICAicHJvZmlsZUlkIiA6ICJhODgyMzAzMDVkOWY0ODRiYjNjNjc2OTg1OTYxYjc2YSIsCiAgInByb2ZpbGVOYW1lIiA6ICJMb3JkRHJld3BpY3VzIiwKICAic2lnbmF0dXJlUmVxdWlyZWQiIDogdHJ1ZSwKICAidGV4dHVyZXMiIDogewogICAgIlNLSU4iIDogewogICAgICAidXJsIiA6ICJodHRwOi8vdGV4dHVyZXMubWluZWNyYWZ0Lm5ldC90ZXh0dXJlL2E3ZjNiMWUxODdkMmY4YzYyNzljMWY3MTIyYzRlNDI3NDFlMDdlZTU2MTQ4MjkxMTMyNWQxMjc2YWE2YzZhOWIiCiAgICB9CiAgfQp9"}]}}}}}

particle minecraft:white_smoke -11830 218 330 0.5 0.5 0.5 0 100
playsound minecraft:entity.enderman.teleport master @a[tag=mg.flw] -11830 218 330 2 1

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/10/cutscene/soul_2 3s
