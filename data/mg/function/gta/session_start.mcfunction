# Premier joueur à Neo City : chargement de la ville, entités dans 1,5 s
scoreboard players set $gtw mg.st 1
scoreboard players set $gtt mg.st 0
execute in mg:gta run forceload add -88 32312 88 32488
execute in mg:gta run forceload add -44 32224 54 32312
schedule function mg:gta/session_setup 30t
