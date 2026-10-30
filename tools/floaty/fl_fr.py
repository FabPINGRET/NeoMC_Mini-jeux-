r"""Traduction française de la carte Floaty dans gen_floaty : clés protégées, table, passe de traduction (aucune écriture sous data/).

    pr = fl_fr.protect(fns, tree_keys, fr_dir)         # clés protégées = section MANUELLE de fr/protected.txt + clés CALCULÉES sur les lignes
                                                       # déjà réécrites (fl_rewrite) et sur les critères des advancements (tree_keys)
    tb = fl_fr.load_table(fr_dir, pr)                  # fl_tr.Table : fr/*.json + fr/ctx.json ; dossier absent : table vide
    st = fl_fr.translate(fns, files, install, tb)      # EN PLACE ; fl_tr.Stats (translated, missing, refused, errors...)
    fl_fr.save(fr_dir, pr)                             # fr/protected.txt, et ctx.json / GLOSSAIRE.md s'ils manquent (jamais écrasés)

L'ordre compte : les clés protégées se calculent sur TOUTES les lignes réécrites AVANT la moindre traduction (traduire un nom d'objet casserait le
verrou ou le test qui le compare). Les identifiants de contexte (fr/ctx.json : {"ns:chemin": {anglais: français}}) sont `ns:chemin` pour une
fonction, `ns:advancement/chemin` pour un advancement (`main_quest:advancement/q1`), `floaty:install` pour les barres de boss de l'installation.
fr/protected.txt : une chaîne JSON par ligne ; au-dessus de la ligne repère MARK, la section manuelle (conservée telle quelle) ; en dessous,
les clés calculées, régénérées à chaque passage. Un commentaire commence par #.
Entrées de translate : fns [(ns, nom, lignes)] ; files [(chemin sous data/, texte ou advancement chargé (dict))] ; install : lignes de floaty:install
(seules les lignes `bossbar` sont lues). probe (extraction) : probe.at(ctx_id, numéro de ligne ou None) puis probe.slot(ligne, composant, nom).
"""
import json
from collections import namedtuple
from pathlib import Path

import fl_tr as T

MARK = '# --- clés calculées par gen_floaty.py (régénérées à chaque passage : ne rien ajouter sous cette ligne) ---'
HEAD = ('# Clés protégées : textes que la carte COMPARE (nom d\'objet, verrou, test d\'entité...) et qui ne doivent JAMAIS être traduits.\n'
        '# Une chaîne JSON par ligne. Au-dessus de la ligne repère : section MANUELLE (conservée) ; en dessous : clés calculées (régénérées).\n')
STUB_GLOSSARY = '# Glossaire de la traduction française de Floaty\n\n(à écrire : conventions, noms propres conservés, termes récurrents)\n'
Protected = namedtuple('Protected', 'keys auto manual text warns')     # keys = auto | manual ; text = section manuelle ; warns = [(motif, ligne)]


def read_protected(fr_dir):
    """fr/protected.txt -> (texte de la section manuelle, clés manuelles normalisées) ; fichier absent : (en-tête, aucune)."""
    p = Path(fr_dir) / 'protected.txt'
    if not p.is_file():
        return HEAD, set()
    text = p.read_text(encoding='utf-8').replace('\r\n', '\n')
    manual = text.split(MARK, 1)[0]
    keys = set()
    for n, line in enumerate(manual.split('\n'), 1):
        if not line.strip() or line.startswith('#'):
            continue
        try:
            k = json.loads(line)
        except ValueError:
            raise ValueError(f'{p.name} ligne {n} : une chaîne JSON est attendue') from None
        if not isinstance(k, str):
            raise ValueError(f'{p.name} ligne {n} : une chaîne JSON est attendue')
        keys.add(T.norm(k)[1])
    return manual, keys


def protect(fns, tree_keys, fr_dir):
    """Lignes réécrites (fns) et clés des critères d'advancements (tree_keys) -> Protected (voir l'en-tête)."""
    text, manual = read_protected(fr_dir)
    auto, st0 = T.protected_keys(l for _, _, lines in fns for l in lines)
    auto |= set(tree_keys)
    return Protected(frozenset(auto | manual), auto, manual, text, st0.warns)


def load_table(fr_dir, pr):
    """fl_tr.Table de fr_dir (clés protégées refusées) ; dossier absent : table vide. ValueError : conflit ou valeur invalide."""
    fr_dir = Path(fr_dir)
    return T.Table.load(fr_dir, fr_dir / 'ctx.json', pr.keys) if fr_dir.is_dir() else T.Table(pr.keys)


def _lines(lines, ctx_id, st, probe):
    for i, line in enumerate(lines):
        if probe:
            probe.at(ctx_id, i + 1)
        lines[i] = T.translate_line(line, ctx_id, st)


def translate(fns, files, install, table, probe=None):
    """Traduit EN PLACE les lignes de fns, les advancements de files (display) et les lignes `bossbar` d'install -> fl_tr.Stats."""
    st = T.Stats(table)
    st.on_slot = probe.slot if probe else None
    for ns, name, lines in fns:
        _lines(lines, f'{ns}:{name}', st, probe)
    for rel, doc in files:
        if isinstance(doc, dict):                                   # advancement de la carte : ns/advancement/chemin.json
            ns, _, rest = rel.partition('/')
            ctx_id = f'{ns}:{rest[:-len(".json")]}'
            if probe:
                probe.at(ctx_id, None)
            T.translate_tree(doc, ctx_id, st)
    bars = [(i, l) for i, l in enumerate(install) if l.startswith('bossbar ')]
    for i, l in bars:
        if probe:
            probe.at('floaty:install', i + 1)
        install[i] = T.translate_line(l, 'floaty:install', st)
    return st


def save(fr_dir, pr):
    """Écrit fr/protected.txt (section manuelle conservée + clés calculées) ; crée fr_dir, ctx.json et GLOSSAIRE.md s'ils manquent."""
    fr_dir = Path(fr_dir)
    fr_dir.mkdir(parents=True, exist_ok=True)
    body = pr.text.rstrip('\n') + '\n' + MARK + '\n' + ''.join(json.dumps(k, ensure_ascii=False) + '\n' for k in sorted(pr.auto - pr.manual))
    for name, text in (('protected.txt', body), ('ctx.json', '{}\n'), ('GLOSSAIRE.md', STUB_GLOSSARY)):
        dest = fr_dir / name
        if name == 'protected.txt' or not dest.exists():
            with open(dest, 'w', encoding='utf-8', newline='\n') as f:
                f.write(text)
