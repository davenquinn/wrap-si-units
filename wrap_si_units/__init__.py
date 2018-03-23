from os import path
from re import sub
from click import command, option, Path, get_text_stream

def filter_SI_units(text, si_units=None):
    __dirname = path.dirname(__file__)
    if si_units is None:
        si_units = path.join(__dirname, 'default-si-units.txt')
    with open(si_units) as f:
        units = [u.rstrip() for u in f]

    for unit in units:
        unit = unit.replace("^","\^")
        text = sub("((?:(?<=\s)-)?[\d,]+((\.[\d]*)+)?) ({})([\s\-\.,:;\)])".format(unit),r"\SI{\1}{\4}\5",text)
    return text

replacements = [
    (u"ºC",r"$^{\circ}$C")
]

@command(name='wrap-si-units')
@option('--si-units', type=Path(exists=True),
    help="A file containing one SI unit definition per line")
def cli(**kwargs):
    text = get_text_stream('stdin').read()
    for t in replacements:
        text = text.replace(*t)
    text = filter_SI_units(text, **kwargs)
    get_text_stream('stdout').write(text)

