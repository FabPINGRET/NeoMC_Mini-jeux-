# Plus personne : zone déchargée (sauf construction en cours : build_wait la décharge)
scoreboard players set $fnw mg.st 0
scoreboard players set $fnok mg.st 0
schedule clear mg:filon/session_ready
execute unless score $fnb mg.st matches 1 run forceload remove -30 45970 46 46046
bossbar set mg:filon players
