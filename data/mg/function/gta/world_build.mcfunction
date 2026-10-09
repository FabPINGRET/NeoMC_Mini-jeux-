# Première construction de Neo City (ou reconstruction complète)
execute in mg:gta run forceload add -88 32312 88 32488
execute in mg:gta run forceload add -44 32211 54 32312
scoreboard players set $gwb mg.st 0
scoreboard players set $gwfull mg.st 1
schedule function mg:gta/wb_step 40t
