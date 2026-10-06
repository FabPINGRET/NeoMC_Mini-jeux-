# Objectif « points de vie » visible par tous (isolé pour ne jamais casser le chargement)
scoreboard objectives add mg.hp health [{"text":"♥","color":"red"}]
scoreboard objectives modify mg.hp rendertype hearts
function mg:core/hp_display
