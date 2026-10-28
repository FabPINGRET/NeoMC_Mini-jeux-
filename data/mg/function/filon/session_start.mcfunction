# Premier mineur : île chargée ; construite si besoin, régénération en attente faite
scoreboard players set $fnw mg.st 1
scoreboard players set $fnok mg.st 0
forceload add -30 45970 46 46046
schedule function mg:filon/session_ready 40t
