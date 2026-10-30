playsound minecraft:entity.vex.ambient neutral @a[tag=mg.flw] -11830 216 330 3 0.7
playsound minecraft:entity.vex.charge neutral @a[tag=mg.flw] -11830 216 330 3 0.1
playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] -11830 216 330 3 0.1
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Smoke","color":"yellow"},{"text":"> But you reopened the Allgrave, didn’t you? And now, before I kill him, I’m going to kill you."},{"text":" ⇒","color":"light_purple"}]

scoreboard players set boss_ta_cutscene_soul_pivot_pitch Value 0

summon marker -11830 213 330 {NoGravity:1b,Silent:1b,Rotation:[0F,0F],Tags:["boss_ta_cutscene_soul_pivot"]}

summon armor_stand -11830 100 330 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_ta_cutscene_soul_display","cackling"],DisabledSlots:4144959,equipment:{head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{"properties":[{"name":"textures","value":"ewogICJ0aW1lc3RhbXAiIDogMTc2MzMwNTY2Mzc3NywKICAicHJvZmlsZUlkIiA6ICJhODgyMzAzMDVkOWY0ODRiYjNjNjc2OTg1OTYxYjc2YSIsCiAgInByb2ZpbGVOYW1lIiA6ICJMb3JkRHJld3BpY3VzIiwKICAic2lnbmF0dXJlUmVxdWlyZWQiIDogdHJ1ZSwKICAidGV4dHVyZXMiIDogewogICAgIlNLSU4iIDogewogICAgICAidXJsIiA6ICJodHRwOi8vdGV4dHVyZXMubWluZWNyYWZ0Lm5ldC90ZXh0dXJlLzczMjE3ZjZhZTE4YzVkOTlmMmI1NmNkNzMxZmFkNmNiMjZmZTExODgyNDhjNjk2M2E3YWEwY2QzODhjODkxNjEiCiAgICB9CiAgfQp9"}]}}}}}

summon armor_stand -11830 100 330 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_ta_cutscene_soul_display","rictus"],DisabledSlots:4144959,equipment:{head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{"properties":[{"name":"textures","value":"ewogICJ0aW1lc3RhbXAiIDogMTc2MzMwNTM3NTM0OSwKICAicHJvZmlsZUlkIiA6ICJhODgyMzAzMDVkOWY0ODRiYjNjNjc2OTg1OTYxYjc2YSIsCiAgInByb2ZpbGVOYW1lIiA6ICJMb3JkRHJld3BpY3VzIiwKICAic2lnbmF0dXJlUmVxdWlyZWQiIDogdHJ1ZSwKICAidGV4dHVyZXMiIDogewogICAgIlNLSU4iIDogewogICAgICAidXJsIiA6ICJodHRwOi8vdGV4dHVyZXMubWluZWNyYWZ0Lm5ldC90ZXh0dXJlLzFiOWQwNjQxNGJhMzdmYTAwYTczMTdjYWVmNWUxOTM1Yzk5Mzg3NTAwZGJiNzFmODI5N2Y5MGM5NzNmMmE5YTciCiAgICB9CiAgfQp9"}]}}}}}

summon armor_stand -11830 100 330 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_ta_cutscene_soul_display","scornful"],DisabledSlots:4144959,equipment:{head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{"properties":[{"name":"textures","value":"ewogICJ0aW1lc3RhbXAiIDogMTc2MzMwNTU4MzQ5NiwKICAicHJvZmlsZUlkIiA6ICJhODgyMzAzMDVkOWY0ODRiYjNjNjc2OTg1OTYxYjc2YSIsCiAgInByb2ZpbGVOYW1lIiA6ICJMb3JkRHJld3BpY3VzIiwKICAic2lnbmF0dXJlUmVxdWlyZWQiIDogdHJ1ZSwKICAidGV4dHVyZXMiIDogewogICAgIlNLSU4iIDogewogICAgICAidXJsIiA6ICJodHRwOi8vdGV4dHVyZXMubWluZWNyYWZ0Lm5ldC90ZXh0dXJlLzJkMTA5YzhjMzkwYWIxZTA5M2EyZWZiNWQwZmU1OTQ5MjllZjQxNDU0NjcyOWIwNmYxZWQwYzA0NjVhZWE1MzYiCiAgICB9CiAgfQp9"}]}}}}}

summon armor_stand -11830 100 330 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_ta_cutscene_soul_display","wailing"],DisabledSlots:4144959,equipment:{head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{"properties":[{"name":"textures","value":"ewogICJ0aW1lc3RhbXAiIDogMTc2MzMwNTUwNDA4MSwKICAicHJvZmlsZUlkIiA6ICJhODgyMzAzMDVkOWY0ODRiYjNjNjc2OTg1OTYxYjc2YSIsCiAgInByb2ZpbGVOYW1lIiA6ICJMb3JkRHJld3BpY3VzIiwKICAic2lnbmF0dXJlUmVxdWlyZWQiIDogdHJ1ZSwKICAidGV4dHVyZXMiIDogewogICAgIlNLSU4iIDogewogICAgICAidXJsIiA6ICJodHRwOi8vdGV4dHVyZXMubWluZWNyYWZ0Lm5ldC90ZXh0dXJlLzMwODJhYWJhNjJkYTJiYzFkYmJlOTVkN2E2YzJlNDRhMzc4Y2M1NWRkNGVjZTEyNzU2YjU4OTMxOTYzYjAxNmQiCiAgICB9CiAgfQp9"}]}}}}}

setblock -11799 202 358 redstone_block

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/10/cutscene/12 10s

#","color":"white"},{"text":"
