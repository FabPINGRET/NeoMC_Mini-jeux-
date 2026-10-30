scoreboard players set 100_percent bool 1

execute unless entity @s[tag=upgrade_scrimp] run scoreboard players set 100_percent bool 0
execute unless entity @s[tag=upgrade_darknyss] run scoreboard players set 100_percent bool 0
execute unless entity @s[tag=upgrade_scleemotius] run scoreboard players set 100_percent bool 0
execute unless entity @s[tag=vyrn] run scoreboard players set 100_percent bool 0
execute unless entity @s[tag=upgrade_mudtilda] run scoreboard players set 100_percent bool 0
execute unless entity @s[tag=upgrade_willy] run scoreboard players set 100_percent bool 0
execute unless entity @s[tag=upgrade_vok] run scoreboard players set 100_percent bool 0
execute unless entity @s[tag=upgrade_etch] run scoreboard players set 100_percent bool 0
execute unless entity @s[tag=upgrade_s18-6] run scoreboard players set 100_percent bool 0

execute unless entity @s[tag=air_scales] run scoreboard players set 100_percent bool 0
execute unless entity @s[tag=agaric_scales] run scoreboard players set 100_percent bool 0
execute unless entity @s[tag=fire_scales] run scoreboard players set 100_percent bool 0
execute unless entity @s[tag=water_scales] run scoreboard players set 100_percent bool 0
execute unless entity @s[tag=rock_scales] run scoreboard players set 100_percent bool 0
execute unless entity @s[tag=plant_scales] run scoreboard players set 100_percent bool 0
execute unless entity @s[tag=light_scales] run scoreboard players set 100_percent bool 0
execute unless entity @s[tag=dark_scales] run scoreboard players set 100_percent bool 0

execute unless entity @s[tag=bottle1] run scoreboard players set 100_percent bool 0
execute unless entity @s[tag=bottle2] run scoreboard players set 100_percent bool 0
execute unless entity @s[tag=bottle3] run scoreboard players set 100_percent bool 0

execute if score beat_eye_in_the_grove bool matches 0 run scoreboard players set 100_percent bool 0
execute if score beat_custodian bool matches 0 run scoreboard players set 100_percent bool 0
execute if score beat_pretzel bool matches 0 run scoreboard players set 100_percent bool 0
execute if score beat_attestor_golem bool matches 0 run scoreboard players set 100_percent bool 0
execute if score beat_icelorn_choir bool matches 0 run scoreboard players set 100_percent bool 0
execute if score beat_knotfire bool matches 0 run scoreboard players set 100_percent bool 0
execute if score beat_wahrog bool matches 0 run scoreboard players set 100_percent bool 0
execute if score beat_threnodist bool matches 0 run scoreboard players set 100_percent bool 0

execute if score spine_sigil bool matches 0 run scoreboard players set 100_percent bool 0
execute if score sweet_sigil bool matches 0 run scoreboard players set 100_percent bool 0
execute if score control_sigil bool matches 0 run scoreboard players set 100_percent bool 0
execute if score crash_sigil bool matches 0 run scoreboard players set 100_percent bool 0

execute if score all_dragonbrews bool matches 0 run scoreboard players set 100_percent bool 0
execute if score all_oaths bool matches 0 run scoreboard players set 100_percent bool 0

execute if score all_noparentunnels bool matches 0 run scoreboard players set 100_percent bool 0
execute if score all_buhtween bool matches 0 run scoreboard players set 100_percent bool 0
execute if score beat_sealed_citadel bool matches 0 run scoreboard players set 100_percent bool 0
execute if score beat_game bool matches 0 run scoreboard players set 100_percent bool 0
execute if score FreeMagic bool matches 0 run scoreboard players set 100_percent bool 0

execute unless score forge_level Value matches 3 run scoreboard players set 100_percent bool 0

execute if score 100_percent bool matches 1 run advancement grant @s only main_quest:100
