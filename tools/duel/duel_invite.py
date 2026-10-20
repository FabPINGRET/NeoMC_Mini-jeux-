"""Duel sniper : liste des adversaires et invitations (défi, accepter, refuser, annuler, expirer), écrites par gen_duel.py.

Un défi = le défieur (tag mg.dlrq, numéro mg.dlid) pose sur l'invité mg.dlto = son numéro et mg.dlx = 600 ticks.
Tags temporaires : mg.dltg adversaire visé (challenge, expire, refuse), mg.dlt2 invité retrouvé par rq_check,
mg.dlca défieur retrouvé par accept / cancel, mg.dlq demandeur de la liste.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lib'))
import mcfn

INV = 600      # ticks de validité d'une invitation
js = mcfn.js


def tx(text, color='gray', **kw):
    return {'text': text, 'color': color, **kw}


def btn(label, color, n, hover):
    return {'text': label, 'color': color, 'bold': True,
            'click_event': {'action': 'run_command', 'command': f'trigger mg.duel set {n}'},
            'hover_event': {'action': 'show_text', 'value': hover}}


def sel(s, color='yellow', **kw):
    return {'selector': s, 'color': color, **kw}


def say(who, *parts):
    return f'tellraw {who} ' + js(list(parts))


def pending_msg():
    """Message quand @s a reçu une invitation : il doit y répondre avant de défier."""
    return say('@s', tx('Tu as reçu une invitation de duel : '), btn('[✔ Accepter]', 'green', 2, 'Relever le défi'),
               tx(' '), btn('[✘ Refuser]', 'red', 3, 'Refuser le défi'), tx(' avant d\'en lancer une.'))


def lists(w):
    w('duel/list', [
        '# Liste cliquable des adversaires libres (@s = joueur) : lien = trigger mg.duel 1000 + id',
        'function mg:duel/busy',
        'execute if score $dlb mg.st matches 1 run return run ' + say('@s', tx('Tu ne peux pas défier maintenant (partie ou activité en cours).')),
        'execute if entity @s[tag=mg.dlrq] run return run ' + say('@s', tx('Tu as déjà une invitation en cours : '), btn('[Annuler]', 'red', 4, 'Annuler l\'invitation')),
        'execute if score @s mg.dlto matches 1.. run return run ' + pending_msg(),
        'execute unless data storage mg:duel {built:1b} run return run ' + say('@s', tx('Les arènes sont en construction, réessaie dans quelques minutes.')),
        say('@s', tx('— Duel sniper 1v1 : clique sur un adversaire —', 'gold')),
        'scoreboard players set $dlc mg.st 0',
        'tag @s add mg.dlq',
        'execute as @a[tag=!mg.dlq,tag=mg.init] run function mg:duel/list_one',
        'tag @s remove mg.dlq',
        'execute if score $dlc mg.st matches 0 run ' + say('@s', tx('Personne n\'est disponible pour un duel pour le moment.')),
    ])
    w('duel/list_one', [
        '# Un candidat (@s = joueur listé ; le demandeur porte mg.dlq) : numéro, occupé ?, ligne cliquable',
        'function mg:duel/busy',
        'execute if score $dlb mg.st matches 1 run return 0',
        'execute if entity @s[tag=mg.dlrq] run return 0',
        'execute if score @s mg.dlto matches 1.. run return 0',
        'execute unless score @s mg.dlid matches 1.. run function mg:duel/new_id',
        'scoreboard players add $dlc mg.st 1',
        'scoreboard players operation #dll mg.st = @s mg.dlid',
        'scoreboard players add #dll mg.st 1000',
        'execute store result storage mg:duel m.v int 1 run scoreboard players get #dll mg.st',
        'function mg:duel/list_line with storage mg:duel m',
    ])
    w('duel/list_line', [
        '# Ligne de la liste (macro : $(v) = 1000 + id ; @s = joueur listé, destinataire = demandeur mg.dlq)',
        '$tellraw @a[tag=mg.dlq] ' + js([tx('  ⚔ ', 'red'),
                                        sel('@s', 'white', click_event={'action': 'run_command', 'command': 'trigger mg.duel set $(v)'},
                                            hover_event={'action': 'show_text', 'value': 'Défier ce joueur en duel sniper'}),
                                        tx('  ← clique pour défier')]),
    ])


def invitations(w):
    w('duel/challenge', [
        '# Défi (@s = défieur ; #dlv = 1000 + id de l\'adversaire)',
        'scoreboard players operation $dlt mg.st = #dlv mg.st',
        'scoreboard players remove $dlt mg.st 1000',
        'execute as @a if score @s mg.dlid = $dlt mg.st run tag @s add mg.dltg',
        'function mg:duel/challenge_chk',
        'tag @a remove mg.dltg',
    ])
    w('duel/challenge_chk', [
        '# Contrôles puis invitation (@s = défieur ; l\'adversaire porte mg.dltg)',
        'execute if entity @s[tag=mg.dlrq] run function mg:duel/rq_check',
        'execute if entity @s[tag=mg.dlrq] run return run ' + say('@s', tx('Tu as déjà une invitation en cours : '), btn('[Annuler]', 'red', 4, 'Annuler l\'invitation')),
        'execute if score @s mg.dlto matches 1.. run return run ' + pending_msg(),
        'function mg:duel/busy',
        'execute if score $dlb mg.st matches 1 run return run ' + say('@s', tx('Tu ne peux pas défier maintenant (partie ou activité en cours).')),
        'execute unless entity @a[tag=mg.dltg] run return run ' + say('@s', tx('Ce joueur n\'est plus là.')),
        'execute if entity @s[tag=mg.dltg] run return run ' + say('@s', tx('Tu ne peux pas te défier toi-même.')),
        'execute as @a[tag=mg.dltg,limit=1] run function mg:duel/busy',
        'execute if score $dlb mg.st matches 1 run return run ' + say('@s', sel('@a[tag=mg.dltg,limit=1]', 'white'), tx(' est occupé (partie ou activité en cours).')),
        'execute if entity @a[tag=mg.dltg,tag=mg.dlrq] run return run ' + say('@s', sel('@a[tag=mg.dltg,limit=1]', 'white'), tx(' a déjà une invitation en cours.')),
        'execute if entity @a[tag=mg.dltg,scores={mg.dlto=1..}] run return run ' + say('@s', sel('@a[tag=mg.dltg,limit=1]', 'white'), tx(' a déjà reçu une invitation.')),
        'function mg:duel/pick',
        'execute if score $dli mg.st matches 0 run return run ' + say('@s', tx('Aucune arène n\'est libre pour le moment (ou elles sont en construction).')),
        'execute unless score @s mg.dlid matches 1.. run function mg:duel/new_id',
        'scoreboard players operation @a[tag=mg.dltg,limit=1] mg.dlto = @s mg.dlid',
        f'scoreboard players set @a[tag=mg.dltg,limit=1] mg.dlx {INV}',
        'tag @s add mg.dlrq',
        say('@a[tag=mg.dltg,limit=1]', sel('@s', 'yellow', bold=True), tx(' te défie en duel sniper 1v1 (30 s) : '),
            btn('[✔ Accepter]', 'green', 2, 'Relever le défi'), tx(' '), btn('[✘ Refuser]', 'red', 3, 'Refuser le défi')),
        say('@s', tx('⚔ Défi envoyé à '), sel('@a[tag=mg.dltg,limit=1]', 'white'), tx(' (30 s) '), btn('[Annuler]', 'red', 4, 'Annuler l\'invitation')),
    ])
    w('duel/cancel', [
        '# Annuler son invitation (@s = défieur) ; ignoré pendant un duel (bouton périmé : l\'abandon est le trigger 5)',
        'execute if entity @s[tag=mg.dl] run return 0',
        'execute unless entity @s[tag=mg.dlrq] run return run ' + say('@s', tx('Tu n\'as aucune invitation à annuler.')),
        'scoreboard players operation $dlt mg.st = @s mg.dlid',
        'tag @s add mg.dlca',
        'execute as @a[scores={mg.dlto=1..}] if score @s mg.dlto = $dlt mg.st run function mg:duel/cancel_t',
        'tag @s remove mg.dlca',
        'tag @s remove mg.dlrq',
        say('@s', tx('⚔ Invitation annulée.')),
    ])
    w('duel/cancel_t', [
        '# L\'invité apprend l\'annulation (@s = invité ; le défieur porte mg.dlca)',
        say('@s', sel('@a[tag=mg.dlca,limit=1]', 'white'), tx(' a annulé son invitation au duel.')),
        'scoreboard players reset @s mg.dlto',
        'scoreboard players reset @s mg.dlx',
    ])
    w('duel/rq_check', [
        '# Le défieur (@s, tag mg.dlrq) a-t-il encore un invité en ligne ? Sinon l\'invitation est périmée',
        'scoreboard players operation $dlt mg.st = @s mg.dlid',
        'execute as @a[scores={mg.dlto=1..}] if score @s mg.dlto = $dlt mg.st run tag @s add mg.dlt2',
        'execute unless entity @a[tag=mg.dlt2] run ' + say('@s', tx('⚔ Invitation annulée : l\'invité s\'est déconnecté.')),
        'execute unless entity @a[tag=mg.dlt2] run tag @s remove mg.dlrq',
        'tag @a remove mg.dlt2',
    ])
    for name, k, to_t, to_c in (
            ('expire', 1, tx('⚔ L\'invitation au duel a expiré.'), [sel('@a[tag=mg.dltg,limit=1]', 'white'), tx(' n\'a pas répondu : invitation expirée.')]),
            ('refuse', 2, tx('⚔ Tu as refusé le duel.'), [sel('@a[tag=mg.dltg,limit=1]', 'white'), tx(' a refusé ton duel.')])):
        w(f'duel/{name}', [
            f'# Invitation {"expirée" if k == 1 else "refusée"} (@s = invité)',
            'execute unless score @s mg.dlto matches 1.. run return run ' + say('@s', tx('Tu n\'as aucune invitation de duel en attente.')),
            'scoreboard players operation $dlt mg.st = @s mg.dlto',
            'tag @s add mg.dltg',
            'execute as @a[tag=mg.dlrq] if score @s mg.dlid = $dlt mg.st run function mg:duel/' + name + '_c',
            'tag @s remove mg.dltg',
            say('@s', to_t),
            'scoreboard players reset @s mg.dlto',
            'scoreboard players reset @s mg.dlx',
        ])
        w(f'duel/{name}_c', ['# (@s = défieur ; l\'invité porte mg.dltg)', 'tag @s remove mg.dlrq', say('@s', *to_c)])
