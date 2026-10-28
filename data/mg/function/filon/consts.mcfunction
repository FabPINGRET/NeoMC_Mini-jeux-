# Constantes, cours de départ, équipe et barre du Filon (chargement)
scoreboard players set #fn100 mg.st 100
scoreboard players set #fn1000 mg.st 1000
scoreboard players set #fn10 mg.st 10
scoreboard players set #fn64 mg.st 64
scoreboard players set #fn2 mg.st 2
scoreboard players set #fb0 mg.st 2
scoreboard players set #fb1 mg.st 2
scoreboard players set #fb2 mg.st 2
scoreboard players set #fb3 mg.st 2
scoreboard players set #fb4 mg.st 2
scoreboard players set #fb5 mg.st 2
scoreboard players set #fb6 mg.st 2
scoreboard players set #fb7 mg.st 20
scoreboard players set #fb8 mg.st 10
scoreboard players set #fb9 mg.st 10
scoreboard players set #fb10 mg.st 40
scoreboard players set #fb11 mg.st 10
scoreboard players set #fb12 mg.st 70
scoreboard players set #fb13 mg.st 140
scoreboard players set #fb14 mg.st 20
scoreboard players set #fb15 mg.st 30
scoreboard players set #fb16 mg.st 500
scoreboard players set #fb17 mg.st 700
scoreboard players set #fb18 mg.st 50
scoreboard players set #fb19 mg.st 80
scoreboard players set #fb20 mg.st 1400
scoreboard players set #fb21 mg.st 700
scoreboard players set #fb22 mg.st 3000
scoreboard players set #fb23 mg.st 5000
execute unless score $fm0 mg.st matches 1.. run scoreboard players set $fm0 mg.st 100
execute unless score $fm1 mg.st matches 1.. run scoreboard players set $fm1 mg.st 100
execute unless score $fm2 mg.st matches 1.. run scoreboard players set $fm2 mg.st 100
execute unless score $fm3 mg.st matches 1.. run scoreboard players set $fm3 mg.st 100
execute unless score $fm4 mg.st matches 1.. run scoreboard players set $fm4 mg.st 100
execute unless score $fm5 mg.st matches 1.. run scoreboard players set $fm5 mg.st 100
execute unless score $fm6 mg.st matches 1.. run scoreboard players set $fm6 mg.st 100
execute unless score $fm7 mg.st matches 1.. run scoreboard players set $fm7 mg.st 100
execute unless score $fm8 mg.st matches 1.. run scoreboard players set $fm8 mg.st 100
execute unless score $fm9 mg.st matches 1.. run scoreboard players set $fm9 mg.st 100
execute unless score $fm10 mg.st matches 1.. run scoreboard players set $fm10 mg.st 100
execute unless score $fm11 mg.st matches 1.. run scoreboard players set $fm11 mg.st 100
execute unless score $fm12 mg.st matches 1.. run scoreboard players set $fm12 mg.st 100
execute unless score $fm13 mg.st matches 1.. run scoreboard players set $fm13 mg.st 100
execute unless score $fm14 mg.st matches 1.. run scoreboard players set $fm14 mg.st 100
execute unless score $fm15 mg.st matches 1.. run scoreboard players set $fm15 mg.st 100
execute unless score $fm16 mg.st matches 1.. run scoreboard players set $fm16 mg.st 100
execute unless score $fm17 mg.st matches 1.. run scoreboard players set $fm17 mg.st 100
execute unless score $fm18 mg.st matches 1.. run scoreboard players set $fm18 mg.st 100
execute unless score $fm19 mg.st matches 1.. run scoreboard players set $fm19 mg.st 100
execute unless score $fm20 mg.st matches 1.. run scoreboard players set $fm20 mg.st 100
execute unless score $fm21 mg.st matches 1.. run scoreboard players set $fm21 mg.st 100
execute unless score $fm22 mg.st matches 1.. run scoreboard players set $fm22 mg.st 100
execute unless score $fm23 mg.st matches 1.. run scoreboard players set $fm23 mg.st 100
execute unless score $fo0 mg.st matches 1.. run scoreboard players set $fo0 mg.st 100
execute unless score $fo1 mg.st matches 1.. run scoreboard players set $fo1 mg.st 100
execute unless score $fo2 mg.st matches 1.. run scoreboard players set $fo2 mg.st 100
execute unless score $fo3 mg.st matches 1.. run scoreboard players set $fo3 mg.st 100
execute unless score $fo4 mg.st matches 1.. run scoreboard players set $fo4 mg.st 100
execute unless score $fo5 mg.st matches 1.. run scoreboard players set $fo5 mg.st 100
execute unless score $fo6 mg.st matches 1.. run scoreboard players set $fo6 mg.st 100
execute unless score $fo7 mg.st matches 1.. run scoreboard players set $fo7 mg.st 100
execute unless score $fo8 mg.st matches 1.. run scoreboard players set $fo8 mg.st 100
execute unless score $fo9 mg.st matches 1.. run scoreboard players set $fo9 mg.st 100
execute unless score $fo10 mg.st matches 1.. run scoreboard players set $fo10 mg.st 100
execute unless score $fo11 mg.st matches 1.. run scoreboard players set $fo11 mg.st 100
execute unless score $fo12 mg.st matches 1.. run scoreboard players set $fo12 mg.st 100
execute unless score $fo13 mg.st matches 1.. run scoreboard players set $fo13 mg.st 100
execute unless score $fo14 mg.st matches 1.. run scoreboard players set $fo14 mg.st 100
execute unless score $fo15 mg.st matches 1.. run scoreboard players set $fo15 mg.st 100
execute unless score $fo16 mg.st matches 1.. run scoreboard players set $fo16 mg.st 100
execute unless score $fo17 mg.st matches 1.. run scoreboard players set $fo17 mg.st 100
execute unless score $fo18 mg.st matches 1.. run scoreboard players set $fo18 mg.st 100
execute unless score $fo19 mg.st matches 1.. run scoreboard players set $fo19 mg.st 100
execute unless score $fo20 mg.st matches 1.. run scoreboard players set $fo20 mg.st 100
execute unless score $fo21 mg.st matches 1.. run scoreboard players set $fo21 mg.st 100
execute unless score $fo22 mg.st matches 1.. run scoreboard players set $fo22 mg.st 100
execute unless score $fo23 mg.st matches 1.. run scoreboard players set $fo23 mg.st 100
execute unless score $fnsea mg.st matches 1.. run scoreboard players set $fnsea mg.st 1
execute unless score $fnt mg.st matches 0.. run scoreboard players set $fnt mg.st 0
execute unless score $fnsc mg.st matches 0.. run scoreboard players set $fnsc mg.st 0
execute unless score $fnpr mg.st matches 1.. run scoreboard players set $fnpr mg.st 1500
execute unless score $fnpend mg.st matches 0.. run scoreboard players set $fnpend mg.st 1
team add mg_fn
team modify mg_fn friendlyFire false
team modify mg_fn color gold
team modify mg_fn seeFriendlyInvisibles false
bossbar add mg:filon ""
bossbar set mg:filon max 2700
bossbar set mg:filon style notched_10
scoreboard players set #fn60 mg.st 60
scoreboard players set #fnmk mg.st 900
