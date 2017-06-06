# wrap-si-units
A filter that wraps SI units for better typography in LaTeX.
This should probably be reworked and generalized into a pandoc filter but this
will do for now.

### Install

> pip install "git+https://github.com/davenquinn/wrap-si-units.git"

### Use

This filter should be applied to text that will become LaTex; it adds the `\SI{100}{W/m^2}` shorthand
used by the `siunitx` filter to input such as `100 W/m^2`. This filter can be applied either before
or after `pandox` in a typical Markdown-to-LaTeX workflow.

`\usepackage{siunitx}` must be specified in LaTeX before using this module.
