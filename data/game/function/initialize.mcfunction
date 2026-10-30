attribute @a[tag=mg.flw] minecraft:fall_damage_multiplier base set 1
xp set @a[tag=mg.flw] 0 points
xp set @a[tag=mg.flw] 0 levels
execute as @a[tag=mg.flw] run attribute @s minecraft:max_health base set 20
execute as @a[tag=mg.flw] run attribute @s minecraft:armor base set 0
execute as @a[tag=mg.flw] run attribute @s minecraft:step_height base reset
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 0
function game:blue_light_off

#---DUNGEON---
scoreboard players set Inventory HeartContainers 10
scoreboard players set Inventory ThornBow 0
scoreboard players set Inventory Bonestride 0
scoreboard players set Inventory FeatherBrush 0
scoreboard players set Inventory Amulet 0
scoreboard players set Inventory TomeOfTongues 0
scoreboard players set Inventory Honeyboost 0
scoreboard players set Inventory DominionRod 0
scoreboard players set Inventory IcelightScepter 0
scoreboard players set Inventory SoaringTrident 0
scoreboard players set Inventory Smokewings 0

scoreboard players set Inventory DungeonFlag 0
scoreboard players set Inventory AntiLag 0
scoreboard players set mainstory Story -1

#---LOVEBUG---
scoreboard players set Inventory LovebugTotal 0
scoreboard players set BetterEconomy bool 0
scoreboard players set BetterGuild bool 0
scoreboard players set EndChest bool 0
scoreboard players set FeatherFall bool 0
scoreboard players set WuggyBow bool 0
scoreboard players set Ambidextrous bool 0
scoreboard players set ConnectingEverywhere bool 0
scoreboard players set FreeMagic bool 0

#---OTHER MAJOR QUEST TOTALS---
scoreboard players set Inventory BardSongTotal 0
scoreboard players set Inventory AbnormazoidTotal 0
scoreboard players set Inventory HistoryBookTotal 0

#---QUEST BOOLS---
#bools are for the gill guild to be able to know if you've completed a quest or not!

scoreboard players set love_1 bool 0
scoreboard players set love_2 bool 0
scoreboard players set love_3 bool 0
scoreboard players set love_4 bool 0
scoreboard players set love_5 bool 0
scoreboard players set love_6 bool 0
scoreboard players set love_7 bool 0
scoreboard players set love_8 bool 0
scoreboard players set love_9 bool 0
scoreboard players set love_10 bool 0
scoreboard players set love_11 bool 0
scoreboard players set love_12 bool 0
scoreboard players set love_13 bool 0
scoreboard players set love_14 bool 0
scoreboard players set love_15 bool 0
scoreboard players set love_16 bool 0
scoreboard players set love_17 bool 0
scoreboard players set love_18 bool 0
scoreboard players set love_19 bool 0
scoreboard players set love_20 bool 0
scoreboard players set love_21 bool 0
scoreboard players set love_22 bool 0
scoreboard players set love_23 bool 0
scoreboard players set love_24 bool 0
scoreboard players set key_1 bool 0
scoreboard players set key_2 bool 0
scoreboard players set key_3 bool 0
scoreboard players set key_4 bool 0
scoreboard players set key_5 bool 0
scoreboard players set key_6 bool 0
scoreboard players set key_7 bool 0
scoreboard players set key_8 bool 0
scoreboard players set key_9 bool 0
scoreboard players set key_10 bool 0
scoreboard players set key_11 bool 0
scoreboard players set key_12 bool 0
scoreboard players set key_13 bool 0
scoreboard players set key_14 bool 0
scoreboard players set key_15 bool 0
scoreboard players set key_16 bool 0
scoreboard players set key_17 bool 0
scoreboard players set key_18 bool 0
scoreboard players set key_19 bool 0
scoreboard players set key_20 bool 0
scoreboard players set key_21 bool 0
scoreboard players set key_22 bool 0
scoreboard players set key_23 bool 0
scoreboard players set key_24 bool 0
scoreboard players set key_25 bool 0
scoreboard players set key_26 bool 0
scoreboard players set key_27 bool 0
scoreboard players set key_28 bool 0
scoreboard players set key_29 bool 0
scoreboard players set key_30 bool 0
scoreboard players set key_31 bool 0
scoreboard players set key_32 bool 0
scoreboard players set key_33 bool 0
scoreboard players set key_34 bool 0
scoreboard players set key_35 bool 0
scoreboard players set key_36 bool 0
scoreboard players set key_37 bool 0
scoreboard players set key_38 bool 0
scoreboard players set key_39 bool 0
scoreboard players set key_40 bool 0
scoreboard players set key_41 bool 0
scoreboard players set key_42 bool 0
scoreboard players set key_43 bool 0
scoreboard players set key_44 bool 0
scoreboard players set key_45 bool 0
scoreboard players set key_46 bool 0
scoreboard players set key_47 bool 0
scoreboard players set key_48 bool 0
scoreboard players set key_49 bool 0
scoreboard players set key_50 bool 0
scoreboard players set key_51 bool 0
scoreboard players set key_52 bool 0
scoreboard players set key_53 bool 0
scoreboard players set key_54 bool 0
scoreboard players set key_55 bool 0
scoreboard players set key_56 bool 0
scoreboard players set key_57 bool 0
scoreboard players set key_58 bool 0
scoreboard players set key_59 bool 0
scoreboard players set key_60 bool 0
scoreboard players set key_61 bool 0
scoreboard players set key_62 bool 0
scoreboard players set key_63 bool 0
scoreboard players set key_64 bool 0
scoreboard players set pattern_1 bool 0
scoreboard players set pattern_2 bool 0
scoreboard players set pattern_3 bool 0
scoreboard players set pattern_4 bool 0
scoreboard players set pattern_5 bool 0
scoreboard players set pattern_6 bool 0
scoreboard players set pattern_7 bool 0
scoreboard players set pattern_8 bool 0
scoreboard players set pattern_9 bool 0
scoreboard players set pattern_10 bool 0
scoreboard players set pattern_11 bool 0
scoreboard players set pattern_12 bool 0
scoreboard players set pattern_13 bool 0
scoreboard players set pattern_14 bool 0
scoreboard players set pattern_15 bool 0
scoreboard players set pattern_16 bool 0
scoreboard players set pattern_17 bool 0
scoreboard players set pattern_18 bool 0
scoreboard players set bard_1 bool 0
scoreboard players set bard_2 bool 0
scoreboard players set bard_3 bool 0
scoreboard players set bard_4 bool 0
scoreboard players set bard_5 bool 0
scoreboard players set bard_6 bool 0
scoreboard players set bard_7 bool 0
scoreboard players set bard_8 bool 0
scoreboard players set bard_9 bool 0
scoreboard players set bard_10 bool 0
scoreboard players set bard_11 bool 0
scoreboard players set bard_12 bool 0
scoreboard players set bard_13 bool 0
scoreboard players set bard_14 bool 0
scoreboard players set bard_15 bool 0
scoreboard players set bard_16 bool 0
scoreboard players set bard_17 bool 0
scoreboard players set abnormazoid_1 bool 0
scoreboard players set abnormazoid_2 bool 0
scoreboard players set abnormazoid_3 bool 0
scoreboard players set abnormazoid_4 bool 0
scoreboard players set abnormazoid_5 bool 0
scoreboard players set abnormazoid_6 bool 0
scoreboard players set abnormazoid_7 bool 0
scoreboard players set abnormazoid_8 bool 0
scoreboard players set abnormazoid_9 bool 0
scoreboard players set abnormazoid_10 bool 0
scoreboard players set abnormazoid_11 bool 0
scoreboard players set abnormazoid_12 bool 0
scoreboard players set abnormazoid_13 bool 0
scoreboard players set abnormazoid_14 bool 0
scoreboard players set abnormazoid_15 bool 0
scoreboard players set abnormazoid_16 bool 0
scoreboard players set abnormazoid_17 bool 0
scoreboard players set abnormazoid_18 bool 0
scoreboard players set history_1 bool 0
scoreboard players set history_2 bool 0
scoreboard players set history_3 bool 0
scoreboard players set history_4 bool 0
scoreboard players set history_5 bool 0
scoreboard players set history_6 bool 0
scoreboard players set history_7 bool 0
scoreboard players set history_8 bool 0
scoreboard players set history_9 bool 0
scoreboard players set history_10 bool 0
scoreboard players set history_11 bool 0
scoreboard players set history_12 bool 0
scoreboard players set history_13 bool 0
scoreboard players set history_14 bool 0
scoreboard players set history_15 bool 0
scoreboard players set history_16 bool 0
scoreboard players set history_17 bool 0
scoreboard players set history_18 bool 0

#---100% CHECKS---
#npcs
tag @a[tag=mg.flw] remove upgrade_scrimp
tag @a[tag=mg.flw] remove upgrade_darknyss
tag @a[tag=mg.flw] remove upgrade_scleemotius
tag @a[tag=mg.flw] remove vyrn
tag @a[tag=mg.flw] remove upgrade_mudtilda
tag @a[tag=mg.flw] remove upgrade_willy
tag @a[tag=mg.flw] remove upgrade_vok
tag @a[tag=mg.flw] remove upgrade_etch
tag @a[tag=mg.flw] remove upgrade_s18-6

#minibosses
scoreboard players set beat_eye_in_the_grove bool 0
scoreboard players set beat_custodian bool 0
scoreboard players set beat_pretzel bool 0
scoreboard players set beat_attestor_golem bool 0
scoreboard players set beat_icelorn_choir bool 0
scoreboard players set beat_knotfire bool 0
scoreboard players set beat_wahrog bool 0
scoreboard players set beat_threnodist bool 0

#major collect
scoreboard players set spine_sigil bool 0
scoreboard players set sweet_sigil bool 0
scoreboard players set control_sigil bool 0
scoreboard players set crash_sigil bool 0
scoreboard players set all_dragonbrews bool 0
scoreboard players set all_oaths bool 0

#other
scoreboard players set all_noparentunnels bool 0
scoreboard players set all_buhtween bool 0
scoreboard players set beat_sealed_citadel bool 0
scoreboard players set beat_game bool 0
scoreboard players set forgemuzzle_1 bool 0
scoreboard players set forgemuzzle_2 bool 0


#nacre
scoreboard players set nacre_1 bool 0
scoreboard players set nacre_2 bool 0
scoreboard players set nacre_3 bool 0
scoreboard players set nacre_4 bool 0
scoreboard players set nacre_5 bool 0
scoreboard players set nacre_6 bool 0
scoreboard players set nacre_7 bool 0
scoreboard players set nacre_8 bool 0
scoreboard players set nacre_9 bool 0
scoreboard players set nacre_10 bool 0

#---ENEMY SPAWN BOOLS--- (at night, when enemies are spawned, bool flips to 0)
scoreboard players set despawned_2 bool 1
scoreboard players set despawned_3 bool 1
scoreboard players set despawned_4 bool 1
scoreboard players set despawned_5 bool 1
scoreboard players set despawned_6 bool 1
scoreboard players set despawned_7 bool 1
scoreboard players set despawned_8 bool 1
scoreboard players set despawned_9 bool 1
scoreboard players set despawned_10 bool 1
scoreboard players set despawned_11 bool 1
scoreboard players set despawned_12 bool 1
scoreboard players set despawned_13 bool 1
scoreboard players set despawned_14 bool 1
scoreboard players set despawned_15 bool 1
scoreboard players set despawned_16 bool 1
scoreboard players set despawned_17 bool 1
scoreboard players set despawned_18 bool 1
scoreboard players set despawned_19 bool 1

#---MISC BOOLS--- (for intraquest checks, etc.)
scoreboard players set mortimer bool 0
scoreboard players set zoid_hurt bool 0
scoreboard players set mindczar Story 0
scoreboard players set whisper_1 bool 0
scoreboard players set whisper_2 bool 0
scoreboard players set whisper_3 bool 0
scoreboard players set whisper_4 bool 0
scoreboard players set whisper_5 bool 0
scoreboard players set whisper_6 bool 0
scoreboard players set whisper_7 bool 0
scoreboard players set strong_glue bool 0
scoreboard players set bskeppy Value 0
scoreboard players set moonlight_contagion bool 0
scoreboard players set golem_lycan bool 0
scoreboard players set bot_lycan bool 0
scoreboard players set cinder_concord Story 0
scoreboard players set zalvorn Story 0
scoreboard players set slime_man Story 0
scoreboard players set nightblin_1 bool 0
scoreboard players set nightblin_2 bool 0
scoreboard players set nightblin_3 bool 0
scoreboard players set nightblin_4 bool 0
scoreboard players set nightblin_5 bool 0
scoreboard players set nightblin_6 bool 0
scoreboard players set nightblin_7 bool 0
scoreboard players set bubble_lake Story 0
scoreboard players set monstervatory Value 0
scoreboard players set traded_with_1 bool 0
scoreboard players set traded_with_2 bool 0
scoreboard players set traded_with_3 bool 0
scoreboard players set traded_with_4 bool 0
scoreboard players set traded_with_5 bool 0
scoreboard players set traded_with_6 bool 0
scoreboard players set traded_with_7 bool 0
scoreboard players set traded_with_8 bool 0
scoreboard players set traded_with_9 bool 0
scoreboard players set traded_with_10 bool 0
scoreboard players set v_paladin Story 0
scoreboard players set mlc_altar Value 0
scoreboard players set memory_contagion bool 0
scoreboard players set can_planet bool 0
#scoreboard players set jagomund bool 0
#scoreboard players set melmund bool 0
#scoreboard players set frormund bool 0
#scoreboard players set xenemund bool 0
scoreboard players set mind_contagion bool 0
scoreboard players set grove_eye bool 0
scoreboard players set forge_level Value 1
scoreboard players set lord_of_valor Story 0
scoreboard players set trial_well_1_going bool 0
scoreboard players set trial_well_2_going bool 0
scoreboard players set trial_well_3_going bool 0
scoreboard players set lorax bool 0
scoreboard players set has_bundle bool 0
scoreboard players set chubcheek bool 0
scoreboard players set plodark bool 0
scoreboard players set banana_of_temptation bool 0
scoreboard players set mr_nippy bool 0
scoreboard players set ios_humor_created bool 0
scoreboard players set simpletoid_force_winner Value 0
scoreboard players set simpletoid bool 0
scoreboard players set anglero_1 bool 0
scoreboard players set anglero_2 bool 0
scoreboard players set anglero_3 bool 0
scoreboard players set funeral_chapel bool 0

#---TAG REMOVAL---
tag @a[tag=mg.flw] remove no_warp
tag @a[tag=mg.flw] remove dw
tag @a[tag=mg.flw] remove agaric_scales
tag @a[tag=mg.flw] remove rock_scales
tag @a[tag=mg.flw] remove fire_scales
tag @a[tag=mg.flw] remove water_scales
tag @a[tag=mg.flw] remove plant_scales
tag @a[tag=mg.flw] remove air_scales
tag @a[tag=mg.flw] remove light_scales
tag @a[tag=mg.flw] remove dark_scales
tag @a[tag=mg.flw] remove bottle1
tag @a[tag=mg.flw] remove bottle2
tag @a[tag=mg.flw] remove bottle3
tag @a[tag=mg.flw] remove bundle
tag @a[tag=mg.flw] remove darknyss

scoreboard players set Inventory Time 2
scoreboard players set Inventory DayNight 1

advancement revoke @a[tag=mg.flw] from main_quest:root
advancement revoke @a[tag=mg.flw] from sidequest:root
advancement revoke @a[tag=mg.flw] from sidequest_2:root
scoreboard players set $flsp mg.st 0
scoreboard players reset * mg.fla
