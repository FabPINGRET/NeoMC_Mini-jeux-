execute as @n[tag=st_boss_face_ref_guide,distance=0..] at @s positioned ^ ^ ^2 as @n[tag=st_boss_face_ref,distance=0..] if entity @s[tag=adj] run function boss:7/body_frame/rotate/execute
