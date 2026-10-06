# 8 idées de mots différentes → mg:bb sug
data modify storage mg:bb tmp set from storage mg:bb words
data modify storage mg:bb sug set value []
execute store result score $bbsl mg.st run data get storage mg:bb words
scoreboard players set $bbsk mg.st 8
function mg:bb/sug_step
