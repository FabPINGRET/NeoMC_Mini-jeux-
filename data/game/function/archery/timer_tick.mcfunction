scoreboard players operation archery_timer_second Value = archery_timer_tick Value
scoreboard players operation archery_timer_second Value /= 20 Value

scoreboard players remove archery_timer_tick Value 1

execute positioned 113 39 164 unless entity @a[gamemode=!spectator,distance=..10,tag=mg.flw] run setblock 114 34 165 air

data merge entity @n[tag=archery_scoreboard,distance=0..] {text:{"score":{"name":"archery_timer_second","objective":"Value"}}}
execute if score archery_timer_tick Value matches ..0 run setblock 114 34 165 air
