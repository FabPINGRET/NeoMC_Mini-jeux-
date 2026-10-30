# Installation de l'état de la carte Scourge (généré par tools/floaty/gen_floaty.py : ne pas éditer) — une seule fois
execute if data storage mg:floaty installed run return 0
data modify storage mg:floaty installed set value 1b
scoreboard objectives add AbnormazoidTotal dummy "AbnormazoidTotal"
scoreboard objectives add Amulet dummy "Amulet"
scoreboard objectives add AntiLag dummy "AntiLag"
scoreboard objectives add BardSongTotal dummy "BardSongTotal"
scoreboard objectives add BellRung minecraft.custom:minecraft.bell_ring "BellRung"
scoreboard objectives add Bonestride dummy "Bonestride"
scoreboard objectives add BossHealth dummy "BossHealth"
scoreboard objectives add CarrotStick minecraft.used:minecraft.carrot_on_a_stick "CarrotStick"
scoreboard objectives add Countdown dummy "Countdown"
scoreboard objectives add DayNight dummy "DayNight"
scoreboard objectives add DeathCount deathCount {"color":"dark_aqua","extra":[{"color":"aqua","text":" Deaths ","bold":true},{"color":"dark_aqua","text":"☠"}],"text":"☠"}
scoreboard objectives add DeathFlag deathCount "DeathFlag"
scoreboard objectives add DominionRod dummy "DominionRod"
scoreboard objectives add DungeonFlag dummy "DungeonFlag"
scoreboard objectives add ElderGuardianKills minecraft.killed:minecraft.guardian "ElderGuardianKills"
scoreboard objectives add FeatherBrush dummy "FeatherBrush"
scoreboard objectives add GuardianKills minecraft.killed:minecraft.guardian "GuardianKills"
scoreboard objectives add HBDeflectCD dummy "HBDeflectCD"
scoreboard objectives add HBWard dummy "HBWard"
scoreboard objectives add HeartContainers dummy "HeartContainers"
scoreboard objectives add HistoryBookTotal dummy "HistoryBookTotal"
scoreboard objectives add Honeyboost dummy "Honeyboost"
scoreboard objectives add IcelightScepter dummy "IcelightScepter"
scoreboard objectives add KillMoment deathCount "KillMoment"
scoreboard objectives add LeaveGame minecraft.custom:minecraft.leave_game "LeaveGame"
scoreboard objectives add LovebugTotal dummy "LovebugTotal"
scoreboard objectives add MobKills minecraft.custom:minecraft.mob_kills "MobKills"
scoreboard objectives add ScreenShake dummy "ScreenShake"
scoreboard objectives add Slept minecraft.custom:minecraft.sleep_in_bed "Slept"
scoreboard objectives add Smokewings dummy "Smokewings"
scoreboard objectives add SoaringTrident dummy "SoaringTrident"
scoreboard objectives add SoundtrackOverride dummy "SoundtrackOverride"
scoreboard objectives add Story dummy "Story"
scoreboard objectives add ThornBow dummy "ThornBow"
scoreboard objectives add Time dummy "Time"
scoreboard objectives add TomeOfTongues dummy "TomeOfTongues"
scoreboard objectives add Value dummy "Value"
scoreboard objectives add arrow_dir dummy "arrow_dir"
scoreboard objectives add bool dummy "bool"
scoreboard objectives add flying dummy "flying"
scoreboard objectives add grow_timer dummy "grow_timer"
scoreboard objectives add horn_blow minecraft.used:minecraft.goat_horn "horn_blow"
scoreboard objectives add jump_flag minecraft.custom:minecraft.jump "jump_flag"
scoreboard objectives add jump_flag_buffer dummy "jump_flag_buffer"
scoreboard objectives add jump_total minecraft.custom:minecraft.jump "jump_total"
scoreboard objectives add longray dummy "longray"
scoreboard objectives add push_mode dummy "push_mode"
scoreboard objectives add shield_block minecraft.custom:minecraft.damage_blocked_by_shield "shield_block"
scoreboard objectives add shortray dummy "shortray"
scoreboard objectives add shrink_timer dummy "shrink_timer"
scoreboard objectives add sneak_last dummy "sneak_last"
scoreboard objectives add sneak_speed_timer dummy "sneak_speed_timer"
scoreboard objectives add sneak_time minecraft.custom:minecraft.sneak_time "sneak_time"
scoreboard objectives add stealth_caught_timer dummy "stealth_caught_timer"
scoreboard objectives add twister_timer dummy "twister_timer"
scoreboard objectives add use_trident minecraft.used:minecraft.trident "use_trident"
scoreboard objectives add y_velocity dummy "y_velocity"
team add NoCollide "NoCollide"
team modify NoCollide color green
team modify NoCollide collisionRule never
team add NoCollideRed "NoCollideRed"
team modify NoCollideRed color red
team modify NoCollideRed collisionRule never
team add NoCollideZoid "NoCollideZoid"
team modify NoCollideZoid color aqua
team modify NoCollideZoid collisionRule never
team add enemy "enemy"
team add hero "Hero"
team modify hero friendlyFire false
team modify hero seeFriendlyInvisibles false
team modify hero color white
scoreboard players set Inventory AbnormazoidTotal 0
scoreboard players set Inventory Amulet 0
scoreboard players set Inventory AntiLag 0
scoreboard players set Inventory BardSongTotal 0
scoreboard players set Inventory Bonestride 0
scoreboard players set boss:attestor BossHealth 0
scoreboard players set boss:attestor_half BossHealth 100
scoreboard players set boss:attestor_quarter BossHealth 50
scoreboard players set boss:attestor_third BossHealth 66
scoreboard players set boss:attestor_two_thirds BossHealth 132
scoreboard players set boss:cob BossHealth 10
scoreboard players set boss:deebo BossHealth 6
scoreboard players set boss:ed BossHealth 6
scoreboard players set boss:final BossHealth 658
scoreboard players set boss:final_morbex BossHealth 200
scoreboard players set boss:fs BossHealth 10
scoreboard players set boss:lod BossHealth 6
scoreboard players set boss:secret BossHealth 6
scoreboard players set boss:sh BossHealth 10
scoreboard players set boss:skt BossHealth 6
scoreboard players set boss:sop BossHealth 10
scoreboard players set boss:st BossHealth 6
scoreboard players set boss:ta BossHealth 6
scoreboard players set boss:wm BossHealth 6
scoreboard players set PityManna Countdown 27
scoreboard players set Timer Countdown 121
scoreboard players set boss:cob Countdown 9
scoreboard players set boss_music Countdown -1
scoreboard players set boss_music_2 Countdown -1
scoreboard players set cob_music Countdown -1
scoreboard players set cob_timer_1 Countdown 3
scoreboard players set cob_timer_2 Countdown 4
scoreboard players set ed_music Countdown -1
scoreboard players set ed_timer_1 Countdown 18
scoreboard players set ed_timer_2 Countdown 70
scoreboard players set ed_timer_3 Countdown 60
scoreboard players set ed_timer_4 Countdown 48
scoreboard players set fs_music Countdown -1
scoreboard players set lod_music Countdown -1
scoreboard players set miniboss_music Countdown -1
scoreboard players set sc_music Countdown -1
scoreboard players set sc_ride_free_1 Countdown 0
scoreboard players set sc_ride_free_2 Countdown 0
scoreboard players set sc_ride_free_3 Countdown 0
scoreboard players set sh_music Countdown -1
scoreboard players set sh_timer_1 Countdown 6
scoreboard players set skt_blue_snake Countdown 1
scoreboard players set skt_green_snake Countdown 1
scoreboard players set skt_music Countdown -1
scoreboard players set skt_red_snake Countdown 1
scoreboard players set skt_ride_free Countdown 0
scoreboard players set slime_man_fail_music Countdown -1
scoreboard players set slime_man_theme_music Countdown -1
scoreboard players set sop_music Countdown -1
scoreboard players set sop_timer_1 Countdown -54191
scoreboard players set st_music Countdown -1
scoreboard players set ta_music Countdown -1
scoreboard players set virion_music Countdown -1
scoreboard players set virus_music Countdown -1
scoreboard players set wm_music Countdown -1
scoreboard players set Inventory DayNight 1
scoreboard players set Inventory DominionRod 0
scoreboard players set Inventory DungeonFlag 0
scoreboard players set Inventory FeatherBrush 0
scoreboard players set Inventory HeartContainers 10
scoreboard players set Inventory HistoryBookTotal 0
scoreboard players set Inventory Honeyboost 0
scoreboard players set Inventory IcelightScepter 0
scoreboard players set Inventory LovebugTotal 0
scoreboard players set Inventory Smokewings 0
scoreboard players set Inventory SoaringTrident 0
scoreboard players set Inventory Story 0
scoreboard players set bubble_lake Story 0
scoreboard players set cinder_concord Story 0
scoreboard players set lord_of_valor Story 0
scoreboard players set mainstory Story -1
scoreboard players set mindczar Story 0
scoreboard players set slime_man Story 0
scoreboard players set tective Story 0
scoreboard players set v_paladin Story 0
scoreboard players set zalvorn Story 0
scoreboard players set Inventory ThornBow 0
scoreboard players set Inventory Time 2
scoreboard players set stealth_cycle Time 2
scoreboard players set Inventory TomeOfTongues 0
scoreboard players set #playerR Value 17164675
scoreboard players set #playerX Value -12465929
scoreboard players set #playerY Value 189200
scoreboard players set #playerZ Value -167758
scoreboard players set #targetX Value -837
scoreboard players set #targetY Value 3911
scoreboard players set #targetZ Value -501
scoreboard players set #tmp_x Value 1355
scoreboard players set #tmp_y Value -32
scoreboard players set #tmp_z Value 702
scoreboard players set -1 Value -1
scoreboard players set -90 Value -90
scoreboard players set 0 Value 0
scoreboard players set 1 Value 1
scoreboard players set 10 Value 10
scoreboard players set 11 Value 11
scoreboard players set 12 Value 12
scoreboard players set 13 Value 13
scoreboard players set 14 Value 14
scoreboard players set 15 Value 15
scoreboard players set 180 Value 180
scoreboard players set 2 Value 2
scoreboard players set 20 Value 20
scoreboard players set 3 Value 3
scoreboard players set 360 Value 360
scoreboard players set 4 Value 4
scoreboard players set 5 Value 5
scoreboard players set 6 Value 6
scoreboard players set 60 Value 60
scoreboard players set 6000 Value 6000
scoreboard players set 67 Value 67
scoreboard players set 7 Value 7
scoreboard players set 8 Value 8
scoreboard players set 9 Value 9
scoreboard players set 90 Value 90
scoreboard players set Time Value 6000
scoreboard players set archery_frame Value 12
scoreboard players set archery_points Value 43
scoreboard players set archery_timer_second Value 0
scoreboard players set archery_timer_tick Value 0
scoreboard players set blade_metal_speed Value 0
scoreboard players set boss:fs_bicep_pitch Value 80
scoreboard players set boss:fs_bicep_pitch_delta Value 1
scoreboard players set boss:fs_bicep_pitch_goal Value 80
scoreboard players set boss:fs_bicep_pitch_speed Value 1
scoreboard players set boss:fs_bicep_pitch_storage Value -999
scoreboard players set boss:fs_bicep_yaw Value 0
scoreboard players set boss:fs_bicep_yaw_delta Value 1
scoreboard players set boss:fs_bicep_yaw_goal Value 0
scoreboard players set boss:fs_bicep_yaw_speed Value 1
scoreboard players set boss:fs_bicep_yaw_storage Value -999
scoreboard players set boss:fs_forearm_pitch Value 85
scoreboard players set boss:fs_forearm_pitch_delta Value 1
scoreboard players set boss:fs_forearm_pitch_goal Value 85
scoreboard players set boss:fs_forearm_pitch_speed Value 1
scoreboard players set boss:fs_forearm_pitch_storage Value -999
scoreboard players set boss:fs_head_pitch Value 80
scoreboard players set boss:fs_head_pitch_delta Value 1
scoreboard players set boss:fs_head_pitch_goal Value 80
scoreboard players set boss:fs_head_pitch_speed Value 1
scoreboard players set boss:fs_head_pitch_storage Value -999
scoreboard players set boss:fs_jitter Value -1
scoreboard players set boss:fs_lastattack Value 1
scoreboard players set boss:fs_motor Value 1
scoreboard players set boss:fs_motor_storage Value -999
scoreboard players set boss:fs_return Value 0
scoreboard players set boss:fs_targeting Value 1
scoreboard players set boss:sh_lastattack Value 0
scoreboard players set boss:sh_state Value 0
scoreboard players set boss:skt_lastattack Value 0
scoreboard players set boss:st_facing_dir Value 0
scoreboard players set boss:st_facing_target Value 2
scoreboard players set boss:st_lastattack Value 5
scoreboard players set boss:st_prism_color Value 12
scoreboard players set boss:ta_lastattack Value 0
scoreboard players set boss:wm_lastattack Value 1
scoreboard players set boss_fs_bicep_pitch Value 0
scoreboard players set boss_fs_bicep_pitch_goal Value 0
scoreboard players set boss_mind_mouth_angle Value 0
scoreboard players set boss_ta_active_face Value 0
scoreboard players set boss_ta_cutscene_soul_pivot_pitch Value 0
scoreboard players set boss_ta_last_face Value 0
scoreboard players set boss_ta_light_pivot_pitch Value 116
scoreboard players set boss_ta_move_mode Value 1
scoreboard players set boss_ta_scorn_angle Value -10
scoreboard players set bskeppy Value 0
scoreboard players set cactus_bomb_burst_chance Value 3
scoreboard players set custodian_health Value 0
scoreboard players set custodian_midnight_moon_angle Value 9000
scoreboard players set custodian_midnight_moon_angle_1 Value 9000
scoreboard players set custodian_midnight_moon_angle_2 Value 9000
scoreboard players set custodian_midnight_moon_angle_3 Value 9000
scoreboard players set custodian_phase Value 1
scoreboard players set custodian_sunrise_angle Value 9060
scoreboard players set custodian_sunset_moon_angle Value -40
scoreboard players set custodian_sunset_moon_delta Value -30
scoreboard players set custodian_sunset_reps Value 0
scoreboard players set dark_mysterious Value 2
scoreboard players set deebo_lastattack Value 0
scoreboard players set deebo_painting Value 0
scoreboard players set doing_quiz Value 0
scoreboard players set final_morbex_health Value 0
scoreboard players set final_morbex_target_mode Value 0
scoreboard players set firelight_scene Value 0
scoreboard players set firelight_script Value -1
scoreboard players set firelight_set Value 0
scoreboard players set forge_level Value 1
scoreboard players set fs_fanswitch Value 3
scoreboard players set fs_puzzle3_level Value 3
scoreboard players set grove_eye_health Value 0
scoreboard players set grove_eye_horse_mode Value 0
scoreboard players set grubsong_1 Value 1
scoreboard players set grubsong_10 Value 3
scoreboard players set grubsong_11 Value 2
scoreboard players set grubsong_12 Value 4
scoreboard players set grubsong_13 Value 3
scoreboard players set grubsong_14 Value 5
scoreboard players set grubsong_2 Value 2
scoreboard players set grubsong_3 Value 3
scoreboard players set grubsong_4 Value 4
scoreboard players set grubsong_5 Value 1
scoreboard players set grubsong_6 Value 2
scoreboard players set grubsong_7 Value 4
scoreboard players set grubsong_8 Value 2
scoreboard players set grubsong_9 Value 1
scoreboard players set icelight_chain Value 0
scoreboard players set icelorn_beat Value 50
scoreboard players set keygod_counter Value 80
scoreboard players set keygod_lastattack Value 1
scoreboard players set knotfire_health Value 0
scoreboard players set knotfire_lastattack Value 3
scoreboard players set memory_health Value 0
scoreboard players set memory_lasthealth Value 0
scoreboard players set mime_health Value 0
scoreboard players set mind_boss_tentacle_angle Value 385
scoreboard players set mind_contagion_health Value 0
scoreboard players set mlc_altar Value 0
scoreboard players set mlc_alter Value 0
scoreboard players set monstervatory Value 0
scoreboard players set moon_phase Value 2
scoreboard players set morbex_health Value 0
scoreboard players set morbex_lastattack Value 6
scoreboard players set morbex_repo_timer Value 100
scoreboard players set morbex_spinning_sword_angle Value 9000
scoreboard players set morbex_spinning_sword_dir Value 3
scoreboard players set morbex_trident_dir Value 1
scoreboard players set morbex_trident_timer Value 0
scoreboard players set naptime_health Value 0
scoreboard players set npt_mobile_1 Value 4
scoreboard players set npt_mobile_2 Value 4
scoreboard players set npt_mobile_3 Value 4
scoreboard players set player_count Value 1
scoreboard players set pretzel_box_tick Value 0
scoreboard players set pretzel_emerald_angle Value -13
scoreboard players set pretzel_emerald_clock Value 11
scoreboard players set pretzel_emerald_delta Value 18
scoreboard players set pretzel_health Value 0
scoreboard players set pretzel_item Value 1
scoreboard players set pretzel_lastattack Value 0
scoreboard players set pretzel_letter Value 4
scoreboard players set pretzel_opening_remark Value 8
scoreboard players set pretzel_rabbit_name Value 4
scoreboard players set pretzel_retreat_remark Value 7
scoreboard players set pretzel_selected Value 3
scoreboard players set pretzel_since_sword Value 0
scoreboard players set quiz_answer_1 Value 0
scoreboard players set quiz_answer_2 Value 0
scoreboard players set quiz_answer_3 Value 0
scoreboard players set quiz_answer_4 Value 0
scoreboard players set quiz_answer_5 Value 0
scoreboard players set quiz_question Value 0
scoreboard players set sc_boss_countdown Value 0
scoreboard players set sc_pose Value 0
scoreboard players set sc_targeting_mode Value 0
scoreboard players set simpletoid_bet Value 0
scoreboard players set simpletoid_force_winner Value 0
scoreboard players set simpletoid_respeed Value 10
scoreboard players set simpletoid_winner Value 0
scoreboard players set sphere_cave_final_neck_angle Value -90
scoreboard players set sphere_cave_neck_angle Value -90
scoreboard players set sphere_cave_neck_step_1 Value 0
scoreboard players set sphere_cave_neck_step_2 Value 0
scoreboard players set sphere_cave_time Value 6000
scoreboard players set state Value -88
scoreboard players set ta_lab_a_results Value 5
scoreboard players set ta_lab_b_results Value 2
scoreboard players set ta_lab_fluid_a_injects Value 0
scoreboard players set ta_lab_kablasts Value 0
scoreboard players set ta_lab_pumps Value 0
scoreboard players set ta_lab_safe_next_fluid Value 0
scoreboard players set ta_lab_step Value 0
scoreboard players set temp Value 1
scoreboard players set thren_arrow_xspeed Value 0
scoreboard players set thren_arrow_zspeed Value 30
scoreboard players set thren_counter Value 0
scoreboard players set thren_fountain_freq Value 5000
scoreboard players set thren_fountain_timer Value 4968
scoreboard players set thren_lastattack Value 7
scoreboard players set thren_target Value 0
scoreboard players set threnodist_health Value 0
scoreboard players set v_paladin_health Value 0
scoreboard players set venna_timer Value 82
scoreboard players set wahrog_counter Value 0
scoreboard players set wahrog_forking_x_delta Value -20
scoreboard players set wahrog_forking_x_rotation Value 117
scoreboard players set wahrog_forking_y_delta Value -12
scoreboard players set wahrog_forking_y_rotation Value -14
scoreboard players set wahrog_health Value 0
scoreboard players set wahrog_lastattack Value 2
scoreboard players set wahrog_shortray Value 0
scoreboard players set wahrog_shortray_1 Value 0
scoreboard players set wahrog_shortray_1a Value 0
scoreboard players set wahrog_shortray_1b Value 0
scoreboard players set wahrog_shortray_2 Value 0
scoreboard players set wahrog_shortray_2a Value 0
scoreboard players set wahrog_shortray_2b Value 0
scoreboard players set wahrog_shortray_3 Value 18
scoreboard players set wahrog_shortray_3a Value 0
scoreboard players set wahrog_target Value 0
scoreboard players set wm_drone_count Value 1
scoreboard players set wm_drone_pivot_1 Value 0
scoreboard players set wm_drone_pivot_2 Value 0
scoreboard players set wm_drone_pivot_3 Value 0
scoreboard players set wm_flower_stage Value 1
scoreboard players set wm_kitchen Value 0
scoreboard players set wm_roof Value 0
scoreboard players set world_virus_shell Value 31
scoreboard players set world_virus_shell_1 Value 24
scoreboard players set world_virus_shell_2 Value 7
scoreboard players set wv_center_eye_xdelta Value 0
scoreboard players set wv_center_eye_ydelta Value 0
scoreboard players set wv_center_xrotation Value 682
scoreboard players set wv_center_yrotation Value -30
scoreboard players set wv_eye_speed Value 1
scoreboard players set wv_eye_xrotation Value 682
scoreboard players set wv_eye_yrotation Value -30
scoreboard players set wv_lastattack Value 6
scoreboard players set wv_lord_timer Value -1
scoreboard players set wv_pose Value 0
scoreboard players set wv_skull_timer Value 1
scoreboard players set wv_target_mode Value 0
scoreboard players set wv_wrist_speed Value 2
scoreboard players set zalvorn_health Value 0
scoreboard players set 100_percent bool 0
scoreboard players set Ambidextrous bool 0
scoreboard players set BetterEconomy bool 0
scoreboard players set BetterGuild bool 0
scoreboard players set ConnectingEverywhere bool 0
scoreboard players set EndChest bool 0
scoreboard players set FeatherFall bool 0
scoreboard players set FreeMagic bool 0
scoreboard players set WuggyBow bool 0
scoreboard players set abnormazoid_1 bool 0
scoreboard players set abnormazoid_10 bool 0
scoreboard players set abnormazoid_11 bool 0
scoreboard players set abnormazoid_12 bool 0
scoreboard players set abnormazoid_13 bool 0
scoreboard players set abnormazoid_14 bool 0
scoreboard players set abnormazoid_15 bool 0
scoreboard players set abnormazoid_16 bool 0
scoreboard players set abnormazoid_17 bool 0
scoreboard players set abnormazoid_18 bool 0
scoreboard players set abnormazoid_2 bool 0
scoreboard players set abnormazoid_3 bool 0
scoreboard players set abnormazoid_4 bool 0
scoreboard players set abnormazoid_5 bool 0
scoreboard players set abnormazoid_6 bool 0
scoreboard players set abnormazoid_7 bool 0
scoreboard players set abnormazoid_8 bool 0
scoreboard players set abnormazoid_9 bool 0
scoreboard players set all_buhtween bool 0
scoreboard players set all_dragonbrews bool 0
scoreboard players set all_noparentunnels bool 0
scoreboard players set all_oaths bool 0
scoreboard players set anglero_1 bool 0
scoreboard players set anglero_2 bool 0
scoreboard players set anglero_3 bool 0
scoreboard players set anglero_giving bool 0
scoreboard players set archery_going bool 0
scoreboard players set banana_of_temptation bool 0
scoreboard players set bard_1 bool 0
scoreboard players set bard_10 bool 0
scoreboard players set bard_11 bool 0
scoreboard players set bard_12 bool 0
scoreboard players set bard_13 bool 0
scoreboard players set bard_14 bool 0
scoreboard players set bard_15 bool 0
scoreboard players set bard_16 bool 0
scoreboard players set bard_17 bool 0
scoreboard players set bard_2 bool 0
scoreboard players set bard_3 bool 0
scoreboard players set bard_4 bool 0
scoreboard players set bard_5 bool 0
scoreboard players set bard_6 bool 0
scoreboard players set bard_7 bool 0
scoreboard players set bard_8 bool 0
scoreboard players set bard_9 bool 0
scoreboard players set beat_attestor_golem bool 0
scoreboard players set beat_custodian bool 0
scoreboard players set beat_eye_in_the_grove bool 0
scoreboard players set beat_game bool 0
scoreboard players set beat_icelorn_choir bool 0
scoreboard players set beat_knotfire bool 0
scoreboard players set beat_pretzel bool 0
scoreboard players set beat_sealed_citadel bool 0
scoreboard players set beat_threnodist bool 0
scoreboard players set beat_wahrog bool 0
scoreboard players set boss:sh_ceiling bool 0
scoreboard players set boss:sh_protected bool 0
scoreboard players set boss:st_facing_dir bool 0
scoreboard players set boss:st_glass bool 1
scoreboard players set boss:st_shatter_glass bool 0
scoreboard players set boss:st_summon_chance bool 1
scoreboard players set boss:st_turn_chance bool 2
scoreboard players set bot_lycan bool 0
scoreboard players set can_planet bool 0
scoreboard players set chubcheek bool 0
scoreboard players set control_sigil bool 0
scoreboard players set crash_sigil bool 0
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
scoreboard players set despawned_2 bool 1
scoreboard players set despawned_3 bool 1
scoreboard players set despawned_4 bool 1
scoreboard players set despawned_5 bool 1
scoreboard players set despawned_6 bool 1
scoreboard players set despawned_7 bool 1
scoreboard players set despawned_8 bool 1
scoreboard players set despawned_9 bool 1
scoreboard players set forgemuzzle_1 bool 0
scoreboard players set forgemuzzle_2 bool 0
scoreboard players set funeral_chapel bool 0
scoreboard players set golem_lycan bool 0
scoreboard players set grove_eye bool 0
scoreboard players set has_bundle bool 0
scoreboard players set history_1 bool 0
scoreboard players set history_10 bool 0
scoreboard players set history_11 bool 0
scoreboard players set history_12 bool 0
scoreboard players set history_13 bool 0
scoreboard players set history_14 bool 0
scoreboard players set history_15 bool 0
scoreboard players set history_16 bool 0
scoreboard players set history_17 bool 0
scoreboard players set history_18 bool 0
scoreboard players set history_19 bool 0
scoreboard players set history_2 bool 0
scoreboard players set history_3 bool 0
scoreboard players set history_4 bool 0
scoreboard players set history_43 bool 1
scoreboard players set history_5 bool 0
scoreboard players set history_6 bool 0
scoreboard players set history_7 bool 0
scoreboard players set history_8 bool 0
scoreboard players set history_9 bool 0
scoreboard players set icelorn_inst_bass bool 0
scoreboard players set icelorn_inst_chime bool 0
scoreboard players set icelorn_inst_flute bool 0
scoreboard players set icelorn_inst_guitar bool 0
scoreboard players set icelorn_inst_harp bool 0
scoreboard players set icelorn_inst_hat bool 0
scoreboard players set icelorn_inst_iron_xylophone bool 0
scoreboard players set icelorn_inst_kick bool 0
scoreboard players set icelorn_inst_pling bool 0
scoreboard players set icelorn_inst_snare bool 0
scoreboard players set icelorn_overdrive bool 0
scoreboard players set ios_humor bool 0
scoreboard players set ios_humor_created bool 0
scoreboard players set key_1 bool 0
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
scoreboard players set key_2 bool 0
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
scoreboard players set key_3 bool 0
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
scoreboard players set key_4 bool 0
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
scoreboard players set key_5 bool 0
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
scoreboard players set key_6 bool 0
scoreboard players set key_60 bool 0
scoreboard players set key_61 bool 0
scoreboard players set key_62 bool 0
scoreboard players set key_63 bool 0
scoreboard players set key_64 bool 0
scoreboard players set key_7 bool 0
scoreboard players set key_8 bool 0
scoreboard players set key_9 bool 0
scoreboard players set library_giving bool 0
scoreboard players set lorax bool 0
scoreboard players set lordsword_mode bool 0
scoreboard players set love_1 bool 0
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
scoreboard players set love_2 bool 0
scoreboard players set love_20 bool 0
scoreboard players set love_21 bool 0
scoreboard players set love_22 bool 0
scoreboard players set love_23 bool 0
scoreboard players set love_24 bool 0
scoreboard players set love_3 bool 0
scoreboard players set love_4 bool 0
scoreboard players set love_5 bool 0
scoreboard players set love_6 bool 0
scoreboard players set love_7 bool 0
scoreboard players set love_8 bool 0
scoreboard players set love_9 bool 0
scoreboard players set memory_contagion bool 0
scoreboard players set mind_contagion bool 0
scoreboard players set moonlight_contagion bool 0
scoreboard players set morbex_hurtable bool 0
scoreboard players set mortimer bool 0
scoreboard players set mr_nippy bool 0
scoreboard players set nacre_1 bool 0
scoreboard players set nacre_10 bool 0
scoreboard players set nacre_2 bool 0
scoreboard players set nacre_3 bool 0
scoreboard players set nacre_4 bool 0
scoreboard players set nacre_5 bool 0
scoreboard players set nacre_6 bool 0
scoreboard players set nacre_7 bool 0
scoreboard players set nacre_8 bool 0
scoreboard players set nacre_9 bool 0
scoreboard players set nightblin_1 bool 0
scoreboard players set nightblin_2 bool 0
scoreboard players set nightblin_3 bool 0
scoreboard players set nightblin_4 bool 0
scoreboard players set nightblin_5 bool 0
scoreboard players set nightblin_6 bool 0
scoreboard players set nightblin_7 bool 0
scoreboard players set pattern_1 bool 0
scoreboard players set pattern_10 bool 0
scoreboard players set pattern_11 bool 0
scoreboard players set pattern_12 bool 0
scoreboard players set pattern_13 bool 0
scoreboard players set pattern_14 bool 0
scoreboard players set pattern_15 bool 0
scoreboard players set pattern_16 bool 0
scoreboard players set pattern_17 bool 0
scoreboard players set pattern_18 bool 0
scoreboard players set pattern_2 bool 0
scoreboard players set pattern_3 bool 0
scoreboard players set pattern_4 bool 0
scoreboard players set pattern_5 bool 0
scoreboard players set pattern_6 bool 0
scoreboard players set pattern_7 bool 0
scoreboard players set pattern_8 bool 0
scoreboard players set pattern_9 bool 0
scoreboard players set plodark bool 0
scoreboard players set pretzel_shotgun_tracking bool 0
scoreboard players set quiz_1 bool 0
scoreboard players set quiz_2 bool 0
scoreboard players set quiz_3 bool 0
scoreboard players set s_t_locator_1 bool 0
scoreboard players set s_t_locator_2 bool 0
scoreboard players set s_t_locator_3 bool 0
scoreboard players set s_t_locator_4 bool 0
scoreboard players set s_t_locator_5 bool 0
scoreboard players set s_t_locator_6 bool 0
scoreboard players set sc_boss_color bool 1
scoreboard players set sc_boss_damaged bool 1
scoreboard players set sc_boss_toggle bool 1
scoreboard players set sc_color bool 1
scoreboard players set sc_toggle bool 0
scoreboard players set simpletoid bool 0
scoreboard players set spine_sigil bool 0
scoreboard players set state bool 0
scoreboard players set stealth_cycle bool 0
scoreboard players set strong_glue bool 0
scoreboard players set sweet_sigil bool 0
scoreboard players set ta_cackling bool 0
scoreboard players set ta_rictus bool 0
scoreboard players set ta_scornful bool 0
scoreboard players set ta_wailing bool 0
scoreboard players set thren_big_dir bool 0
scoreboard players set traded_with_1 bool 0
scoreboard players set traded_with_10 bool 0
scoreboard players set traded_with_2 bool 0
scoreboard players set traded_with_3 bool 0
scoreboard players set traded_with_4 bool 0
scoreboard players set traded_with_5 bool 0
scoreboard players set traded_with_6 bool 0
scoreboard players set traded_with_7 bool 0
scoreboard players set traded_with_8 bool 0
scoreboard players set traded_with_9 bool 0
scoreboard players set trial_well_1_going bool 0
scoreboard players set trial_well_2_going bool 0
scoreboard players set trial_well_3_going bool 0
scoreboard players set vyrn_machine bool 0
scoreboard players set whisper_1 bool 0
scoreboard players set whisper_2 bool 0
scoreboard players set whisper_3 bool 0
scoreboard players set whisper_4 bool 0
scoreboard players set whisper_5 bool 0
scoreboard players set whisper_6 bool 0
scoreboard players set whisper_7 bool 0
scoreboard players set whisper_quest_2 bool 0
scoreboard players set wm_follow_dest bool 1
scoreboard players set wm_match_black bool 0
scoreboard players set wm_match_blue bool 0
scoreboard players set wm_match_brown bool 0
scoreboard players set wm_match_correctflag bool 0
scoreboard players set wm_match_cyan bool 0
scoreboard players set wm_match_lime bool 0
scoreboard players set wm_match_magenta bool 0
scoreboard players set wm_match_orange bool 0
scoreboard players set wm_match_purple bool 0
scoreboard players set wm_match_red bool 0
scoreboard players set wm_match_state bool 1
scoreboard players set wm_match_white bool 0
scoreboard players set wm_match_yellow bool 0
scoreboard players set wm_memory1 bool 0
scoreboard players set wm_memory2 bool 0
scoreboard players set wm_memory3 bool 0
scoreboard players set wm_memory4 bool 0
scoreboard players set wv_alive bool 1
scoreboard players set wv_chop_check bool 0
scoreboard players set wv_fire_color bool 0
scoreboard players set wv_focused bool 0
scoreboard players set wv_one_left bool 0
scoreboard players set yommod_all bool 0
scoreboard players set zoid_hurt bool 0
scoreboard players set boss:skt shortray 0
scoreboard players set boss:skt_ectobeam shortray 309
bossbar add boss:attestor {"color":"gold","text":"Attestor Golem","italic":true}
bossbar set boss:attestor color red
bossbar set boss:attestor max 200
bossbar set boss:attestor visible true
bossbar add boss:cob {"color":"gray","text":"Calcified Kraken","bold":true}
bossbar set boss:cob color green
bossbar set boss:cob style notched_10
bossbar set boss:cob max 10
bossbar set boss:cob value 10
bossbar set boss:cob visible true
bossbar add boss:custodian {"color":"dark_purple","text":"Custodian of the Spheres","italic":true}
bossbar set boss:custodian color green
bossbar set boss:custodian value 100
bossbar set boss:custodian visible true
bossbar add boss:dark_eebo {"color":"blue","text":"Dark Eebo","italic":true}
bossbar set boss:dark_eebo color green
bossbar set boss:dark_eebo style notched_6
bossbar set boss:dark_eebo max 6
bossbar set boss:dark_eebo value 6
bossbar set boss:dark_eebo visible true
bossbar add boss:ed {"color":"red","text":"Magmorph","bold":true}
bossbar set boss:ed color green
bossbar set boss:ed style notched_6
bossbar set boss:ed max 6
bossbar set boss:ed value 6
bossbar set boss:ed visible true
bossbar add boss:eye_in_the_grove {"color":"gold","text":"The Eye in the Grove","italic":true}
bossbar set boss:eye_in_the_grove color green
bossbar set boss:eye_in_the_grove max 60
bossbar set boss:eye_in_the_grove value 60
bossbar set boss:eye_in_the_grove visible true
bossbar add boss:final {"color":"aqua","extra":[{"color":"dark_aqua","text":" ᴡᴏʀʟᴅ ᴠɪʀᴜꜱ ","bold":true,"obfuscated":false},{"color":"aqua","text":"xxx","bold":false,"obfuscated":true}],"text":"xxx","obfuscated":true}
bossbar set boss:final color purple
bossbar set boss:final max 658
bossbar set boss:final value 658
bossbar set boss:final visible true
bossbar add boss:final_morbex {"color":"dark_aqua","text":"Scourgelord Morbex","bold":true}
bossbar set boss:final_morbex color green
bossbar set boss:final_morbex max 200
bossbar set boss:final_morbex value 200
bossbar set boss:final_morbex visible true
bossbar add boss:folded_threnodist {"color":"dark_purple","text":"Folded Threnodist","italic":true}
bossbar set boss:folded_threnodist color green
bossbar set boss:folded_threnodist max 180
bossbar set boss:folded_threnodist value 180
bossbar set boss:folded_threnodist visible true
bossbar add boss:fs {"color":"aqua","text":"Frostbyte","bold":true}
bossbar set boss:fs color green
bossbar set boss:fs style notched_10
bossbar set boss:fs max 10
bossbar set boss:fs value 10
bossbar set boss:fs visible true
bossbar add boss:icelorn_choir {"color":"aqua","text":"Icelorn Choir","italic":true}
bossbar set boss:icelorn_choir color green
bossbar set boss:icelorn_choir max 130
bossbar set boss:icelorn_choir value 130
bossbar set boss:icelorn_choir visible true
bossbar add boss:knotfire {"color":"green","text":"Knotfire","italic":true}
bossbar set boss:knotfire color green
bossbar set boss:knotfire max 150
bossbar set boss:knotfire value 150
bossbar set boss:knotfire visible true
bossbar add boss:lod {"color":"gold","text":"Bookwyrm","bold":true}
bossbar set boss:lod color green
bossbar set boss:lod style notched_6
bossbar set boss:lod max 6
bossbar set boss:lod value 6
bossbar set boss:lod visible true
bossbar add boss:memory_contagion {"color":"green","text":"Memory Contagion","italic":true}
bossbar set boss:memory_contagion color green
bossbar set boss:memory_contagion max 150
bossbar set boss:memory_contagion value 150
bossbar set boss:memory_contagion visible true
bossbar add boss:mime {"color":"white","text":"The Mime in Charge","italic":true}
bossbar set boss:mime color green
bossbar set boss:mime max 180
bossbar set boss:mime value 180
bossbar set boss:mime visible true
bossbar add boss:mind_contagion {"color":"dark_aqua","text":"Mind Contagion","italic":true}
bossbar set boss:mind_contagion color green
bossbar set boss:mind_contagion max 180
bossbar set boss:mind_contagion value 180
bossbar set boss:mind_contagion visible true
bossbar add boss:morbex {"color":"dark_aqua","text":"Lord Morbex","italic":true}
bossbar set boss:morbex color red
bossbar set boss:morbex visible true
bossbar add boss:pretzel {"color":"red","text":"Pretzel Jenkins","italic":true}
bossbar set boss:pretzel color green
bossbar set boss:pretzel value 100
bossbar set boss:pretzel visible true
bossbar add boss:prophet {"color":"blue","text":"Crackling Prophet Wahrog","italic":true}
bossbar set boss:prophet color green
bossbar set boss:prophet max 160
bossbar set boss:prophet value 160
bossbar set boss:prophet visible true
bossbar add boss:secret {"color":"dark_purple","text":"God of Keys","bold":true}
bossbar set boss:secret color green
bossbar set boss:secret style notched_6
bossbar set boss:secret max 6
bossbar set boss:secret value 6
bossbar set boss:secret visible true
bossbar add boss:sh {"color":"light_purple","text":"Slubwart the Yucky","bold":true}
bossbar set boss:sh color green
bossbar set boss:sh style notched_10
bossbar set boss:sh max 10
bossbar set boss:sh value 10
bossbar set boss:sh visible true
bossbar add boss:skt {"color":"dark_green","text":"Shade of the Serpent King","bold":true}
bossbar set boss:skt color green
bossbar set boss:skt style notched_6
bossbar set boss:skt max 6
bossbar set boss:skt value 6
bossbar set boss:skt visible true
bossbar add boss:sop {"color":"light_purple","text":"Monarch Rose","bold":true}
bossbar set boss:sop color green
bossbar set boss:sop style notched_10
bossbar set boss:sop max 10
bossbar set boss:sop value 10
bossbar set boss:sop visible true
bossbar add boss:st {"color":"gray","text":"Hollow Watcher","bold":true}
bossbar set boss:st color green
bossbar set boss:st style notched_6
bossbar set boss:st max 6
bossbar set boss:st value 6
bossbar set boss:st visible true
bossbar add boss:ta {"color":"yellow","text":"The Allsoul","bold":true}
bossbar set boss:ta color green
bossbar set boss:ta style notched_6
bossbar set boss:ta max 6
bossbar set boss:ta value 6
bossbar set boss:ta visible true
bossbar add boss:teddybear {"color":"gold","text":"Naptime Guardian","italic":true}
bossbar set boss:teddybear color green
bossbar set boss:teddybear max 180
bossbar set boss:teddybear value 180
bossbar set boss:teddybear visible true
bossbar add boss:vesperal_paladin {"color":"aqua","text":"Vesperal Paladin","italic":true}
bossbar set boss:vesperal_paladin color green
bossbar set boss:vesperal_paladin max 150
bossbar set boss:vesperal_paladin value 150
bossbar set boss:vesperal_paladin visible true
bossbar add boss:wm {"color":"blue","text":"Aquamentra","bold":true}
bossbar set boss:wm color green
bossbar set boss:wm style notched_6
bossbar set boss:wm max 6
bossbar set boss:wm value 6
bossbar set boss:wm visible true
bossbar add boss:zalvorn {"color":"gold","text":"Zalvorn the Evil Puppet Guy","italic":true}
bossbar set boss:zalvorn color green
bossbar set boss:zalvorn max 120
bossbar set boss:zalvorn value 120
bossbar set boss:zalvorn visible true
schedule function floaty:sched/game/advancement/sidequest 10t replace
