execute as @n[tag=sc_boss_pos,distance=0..] at @s run summon marker ~ ~ ~ {NoGravity:1b,Silent:1b,Tags:["sc_keyring_pos"]}
execute as @n[tag=sc_boss_pos,distance=0..] at @s run function boss:secret/model/keyring
tag @e[tag=sc_boss_model_keyring,tag=new,distance=0..] add 1
tag @e[tag=sc_boss_model_keyring,tag=new,distance=0..] remove new
execute as @n[tag=sc_boss_pos,distance=0..] at @s run function boss:secret/model/keyring
tag @e[tag=sc_boss_model_keyring,tag=new,distance=0..] add 2
tag @e[tag=sc_boss_model_keyring,tag=new,distance=0..] remove new
execute as @n[tag=sc_boss_pos,distance=0..] at @s run function boss:secret/model/keyring
tag @e[tag=sc_boss_model_keyring,tag=new,distance=0..] add 3
tag @e[tag=sc_boss_model_keyring,tag=new,distance=0..] remove new
execute as @n[tag=sc_boss_pos,distance=0..] at @s run function boss:secret/model/keyring
tag @e[tag=sc_boss_model_keyring,tag=new,distance=0..] add 4
tag @e[tag=sc_boss_model_keyring,tag=new,distance=0..] remove new
execute as @n[tag=sc_boss_pos,distance=0..] at @s run function boss:secret/model/keyring
tag @e[tag=sc_boss_model_keyring,tag=new,distance=0..] add 5
tag @e[tag=sc_boss_model_keyring,tag=new,distance=0..] remove new
execute as @n[tag=sc_boss_pos,distance=0..] at @s run function boss:secret/model/keyring
tag @e[tag=sc_boss_model_keyring,tag=new,distance=0..] add 6
tag @e[tag=sc_boss_model_keyring,tag=new,distance=0..] remove new
