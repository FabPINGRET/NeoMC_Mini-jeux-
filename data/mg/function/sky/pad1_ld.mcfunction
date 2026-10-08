# 1 si la plateforme est chargée
execute unless loaded -8 235 27632 run return fail
execute unless loaded -8 235 27648 run return fail
execute unless loaded 8 235 27632 run return fail
execute unless loaded 8 235 27648 run return fail
return 1
