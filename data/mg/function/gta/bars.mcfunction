# Étoiles de recherche : une barre de boss par niveau (1 à 5), haut de l'écran
bossbar add mg:gtaw1 ""
bossbar set mg:gtaw1 color white
bossbar set mg:gtaw1 max 1
bossbar set mg:gtaw1 value 0
execute if score $rp mg.st matches 1 run bossbar set mg:gtaw1 name {"text":"","font":"mg:gta","color":"white"}
execute unless score $rp mg.st matches 1 run bossbar set mg:gtaw1 name [{"text":"★","color":"gold","bold":true},{"text":"☆☆☆☆","color":"dark_gray","bold":true}]
bossbar add mg:gtaw2 ""
bossbar set mg:gtaw2 color white
bossbar set mg:gtaw2 max 1
bossbar set mg:gtaw2 value 0
execute if score $rp mg.st matches 1 run bossbar set mg:gtaw2 name {"text":"","font":"mg:gta","color":"white"}
execute unless score $rp mg.st matches 1 run bossbar set mg:gtaw2 name [{"text":"★★","color":"gold","bold":true},{"text":"☆☆☆","color":"dark_gray","bold":true}]
bossbar add mg:gtaw3 ""
bossbar set mg:gtaw3 color white
bossbar set mg:gtaw3 max 1
bossbar set mg:gtaw3 value 0
execute if score $rp mg.st matches 1 run bossbar set mg:gtaw3 name {"text":"","font":"mg:gta","color":"white"}
execute unless score $rp mg.st matches 1 run bossbar set mg:gtaw3 name [{"text":"★★★","color":"gold","bold":true},{"text":"☆☆","color":"dark_gray","bold":true}]
bossbar add mg:gtaw4 ""
bossbar set mg:gtaw4 color white
bossbar set mg:gtaw4 max 1
bossbar set mg:gtaw4 value 0
execute if score $rp mg.st matches 1 run bossbar set mg:gtaw4 name {"text":"","font":"mg:gta","color":"white"}
execute unless score $rp mg.st matches 1 run bossbar set mg:gtaw4 name [{"text":"★★★★","color":"gold","bold":true},{"text":"☆","color":"dark_gray","bold":true}]
bossbar add mg:gtaw5 ""
bossbar set mg:gtaw5 color white
bossbar set mg:gtaw5 max 1
bossbar set mg:gtaw5 value 0
execute if score $rp mg.st matches 1 run bossbar set mg:gtaw5 name {"text":"","font":"mg:gta","color":"white"}
execute unless score $rp mg.st matches 1 run bossbar set mg:gtaw5 name [{"text":"★★★★★","color":"gold","bold":true},{"text":"","color":"dark_gray","bold":true}]
