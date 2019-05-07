#!/usr/bin/env python3
"""

local_mpl_config.py

requirements:
  - matplotlib-3.x.x+ requires python3
  - Helvetica*.ttf fonts installed in matplotlib fonts directory

    if you're using MacPorts, the fonts directory is here:

      /opt/local/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf

    the following guide is very helpful:

      https://olgabotvinnik.com/blog/how-to-set-helvetica-as-the-default-sans-serif-font-in/

usage:

  We generally use one directory or script per figure generated.
  Easiest way to get started is to copy this file somewhere,
  then create a symlink in each figure's directory:

    figures/sample-plot/plot.py
    figures/sample-plot/local_mpl_config.py -> ../local_mpl_config.py
    figures/local_mpl_config.py

some useful resources:

  - anatomy of a figure: https://matplotlib.org/_images/anatomy.png
  - matplotlib for papers: https://github.com/jbmouret/matplotlib_for_papers

a lot of credit for various functions in this file goes to those who
answered questions on stackoverflow.
"""

__version__ = '1.1'

import cycler
import inspect
import matplotlib
import os
import sys

def initialize():
  """
  Initializes the figure with reasonably sane settings--the most
  important of which is telling matplotlib to use Type1 fonts (the ACM
  paper format checker will complain endlessly if using Type3).
  """
  matplotlib.rcParams.update({
      'pdf.fonttype'         : 42 # use Type1 fonts instead of Type3
      ,'ps.fonttype'         : 42

      ,'figure.figsize'      : [10, 10]

      ,'axes.linewidth'      : 0.75

      ,'font.size'           : 13
      ,'axes.titlesize'      : 13
      ,'ytick.labelsize'     : 13
      ,'xtick.labelsize'     : 13

      ,'font.sans-serif'     : ['Helvetica']
      ,'font.family'         : 'sans-serif'
      ,'font.style'          : 'normal'
      ,'font.weight'         : 'normal'
      ,'mathtext.fontset'    : 'cm'
      ,'text.usetex'         : False

      ,'legend.frameon'      : False

      ,'xtick.direction'     : 'out'
      ,'xtick.major.pad'     : 2
      ,'xtick.major.size'    : 4
      ,'xtick.major.width'   : 0.75
      ,'xtick.minor.pad'     : 2
      ,'xtick.minor.size'    : 2

      ,'ytick.direction'     : 'out'
      ,'ytick.major.pad'     : 2
      ,'ytick.major.size'    : 4
      ,'ytick.major.width'   : 0.75
      ,'ytick.minor.pad'     : 2
      ,'ytick.minor.size'    : 2

      ,'savefig.dpi'         : 600
    })

# TODO move the palettes outside of this function so we can use them
# individually.

# solarized: https://ethanschoonover.com/solarized/
SOLARIZED = {
  "base03"  : "#002B36",
  "base02"  : "#073642",
  "base01"  : "#586e75",
  "base00"  : "#657b83",
  "base0"   : "#839496",
  "base1"   : "#93a1a1",
  "base2"   : "#eee8d5",
  "base3"   : "#fdf6e3",
  "yellow"  : "#b58900",
  "orange"  : "#cb4b16",
  "red"     : "#dc322F",
  "magenta" : "#d33682",
  "violet"  : "#6c71c4",
  "blue"    : "#268bd2",
  "cyan"    : "#2aa198",
  "green"   : "#859900"
}

SOLARIZED_CYCLER = cycler.cycler(color=[
  SOLARIZED["blue"],
  SOLARIZED["green"],
  SOLARIZED["red"],
  SOLARIZED["cyan"],
  SOLARIZED["magenta"],
  SOLARIZED["yellow"],
  SOLARIZED["base00"]])

# the following schemes are from https://personal.sron.nl/~pault
BRIGHT = {
  "blue"   : "#4477aa",
  "cyan"   : "#66ccee",
  "green"  : "#228833",
  "yellow" : "#ccbb44",
  "red"    : "#ee6677",
  "purple" : "#aa3377",
  "grey"   : "#bbbbbb"
}

BRIGHT_CYCLER = cycler.cycler(color=[
  BRIGHT["blue"],
  BRIGHT["red"],
  BRIGHT["green"],
  BRIGHT["yellow"],
  BRIGHT["cyan"],
  BRIGHT["purple"],
  BRIGHT["grey"]])

HIGH_CONTRAST = {
  "white"  : "#ffffff",
  "yellow" : "#ddaa33",
  "red"    : "#bb5566",
  "blue"   : "#004488",
  "black"  : "#000000"
}

HIGH_CONTRAST_CYCLER = cycler.cycler(color=[
  HIGH_CONTRAST["blue"],
  HIGH_CONTRAST["yellow"],
  HIGH_CONTRAST["red"]])

VIBRANT = {
  "blue": "#0077BB",
  "cyan": "#33bbee",
  "teal": "#009988",
  "orange": "#ee7733",
  "red": "#cc3311",
  "magenta": "#ee3377",
  "grey": "#bbbbbb"
}

VIBRANT_CYCLER = cycler.cycler(color=[
  VIBRANT["orange"],
  VIBRANT["blue"],
  VIBRANT["cyan"],
  VIBRANT["magenta"],
  VIBRANT["red"],
  VIBRANT["teal"],
  VIBRANT["grey"] ])

MUTED = {
  "indigo"    : "#332288",
  "cyan"      : "#88ccee",
  "teal"      : "#44aa99",
  "green"     : "#117733",
  "olive"     : "#999933",
  "sand"      : "#ddcc77",
  "rose"      : "#cc6677",
  "wine"      : "#882255",
  "purple"    : "#aa4499",
  "pale grey" : "#dddddd"
}

MUTED_CYCLER = cycler.cycler(color=[
  MUTED["rose"],
  MUTED["indigo"],
  MUTED["sand"],
  MUTED["green"],
  MUTED["cyan"],
  MUTED["wine"],
  MUTED["teal"],
  MUTED["olive"],
  MUTED["purple"],
  MUTED["pale grey"] ])

PALE = {
  "pale blue"   : "#bbccee",
  "pale cyan"   : "#cceeff",
  "pale green"  : "#ccddaa",
  "pale yellow" : "#eeeebb",
  "pale red"    : "#ffcccc",
  "pale grey"   : "#dddddd"
}

DARK = {
  "dark blue"   : "#222255",
  "dark cyan"   : "#225555",
  "dark green"  : "#225522",
  "dark yellow" : "#666633",
  "dark red"    : "#663333",
  "dark grey"   : "#555555"
}

LIGHT = {
  "light blue"   : "#77aadd",
  "light cyan"   : "#99ddff",
  "mint"         : "#44bb99",
  "pear"         : "#bbcc33",
  "olive"        : "#aaaa00",
  "light yellow" : "#eedd88",
  "orange"       : "#ee8866",
  "pink"         : "#ffaabb",
  "pale grey"    : "#dddddd"
}

LIGHT_CYCLER = cycler.cycler(color=[
  LIGHT["light blue"],
  LIGHT["orange"],
  LIGHT["light yellow"],
  LIGHT["pink"],
  LIGHT["light cyan"],
  LIGHT["mint"],
  LIGHT["pear"],
  LIGHT["olive"],
  LIGHT["pale grey"] ])

def set_colors(colorset='solarized'):
  """
  Set the color cycle to one of the following: ['solarized', 'bright',
  'high contrast', 'vibrant', 'muted', 'light']

  If no colorset is specified, the default is 'solarized'.
  """
  params = { "axes.prop_cycle": get_color_cycle(colorset) }
  matplotlib.rcParams.update(params)

def get_color_cycle(colorset='solarized'):
  """
  Get a particular color cycle.

  If no colorset is specified, the default is 'solarized'.
  """
  COLOR = {
            'solarized'     : SOLARIZED_CYCLER,
            'bright'        : BRIGHT_CYCLER,
            'high contrast' : HIGH_CONTRAST_CYCLER,
            'vibrant'       : VIBRANT_CYCLER,
            'muted'         : MUTED_CYCLER,
            'light'         : LIGHT_CYCLER
          }.get(colorset, SOLARIZED_CYCLER)

  return COLOR

def set_suptitle(plot_title):
  """
  Set the title of the figure when there are multiple subplots.

  The title is placed a bit higher and in a smaller font than default,
  because we generally crop it when including the graphic in a paper
  written with LaTeX:

    \includegraphics[trim=0 0 0 17px, clip=true]{figure.pdf}

  It's useful to include some metadata or some other information
  in this title when reviewing multiple graphs or figures for
  analysis or discussion.
  """
  matplotlib.pyplot.suptitle(plot_title, y=1.05, fontsize=10)

def set_title(plot_title,twiny=False):
  """
  The title is placed a bit higher and in a smaller font than default,
  because we generally crop it when including the graphic in a paper
  written with LaTeX:

    \includegraphics[trim=0 0 0 17px, clip=true]{figure.pdf}

  It's useful to include some metadata or some other information
  in this title when reviewing multiple graphs or figures for
  analysis or discussion.
  """
  ax = matplotlib.pyplot.gca()

  y = 1.05
  if twiny == True:
    y = 1.17 # move it up a bit

  t = matplotlib.pyplot.text(
        x                   = 0.5,
        y                   = y,
        s                   = plot_title,
        horizontalalignment = 'center',
        transform           = ax.transAxes,
        fontsize            = 10)

def adjust_spines(ax, spines, position='outward', amounts=None):
  """
  ax: the axis to adjust spines on

  spines: a list of spine locations to set visible, e.g., ['left',
  'right', 'bottom', 'top']

  position: position of spine. currently supported: 'zero', 'outward'
  (default)

  amounts: A dictionary containing spine locations and points. When used
  in conjunction with position='outward', place the spine out a number
  of points (or in, if negative).

  Default: {'left': 0, 'bottom': 0 }

  Example: {'left': -2, 'bottom': 0 }
  """
  for loc, spine in ax.spines.items():
    if loc in spines:
      if position == 'zero':
        spine.set_position('zero')
      elif position == 'outward':
        if loc == 'left':
          spine.set_position(('outward', amounts.get('left', 0) if amounts else 0))
        if loc == 'bottom':
          spine.set_position(('outward', amounts.get('bottom', 0) if amounts else 0))
      else:
        spine.set_position(('outward', 0))
      spine.set_smart_bounds(True)
      #spine.set_position('center')
      #pass
    else:
      spine.set_visible(False)

  # turn off ticks where there is no spine
  if 'left' in spines:
    ax.yaxis.set_ticks_position('left')
  else:
    # no yaxis ticks
    ax.yaxis.set_ticks([])

  if 'bottom' in spines:
    ax.xaxis.set_ticks_position('bottom')
  else:
    # no xaxis ticks
    ax.xaxis.set_ticks([])

def adjust_ticks(ax):
  """
  Given an axis 'ax', set some defaults.
  """
  ax.minorticks_off()      # turn off all minor ticks
  ax.tick_params(
    axis        = 'both',  # changes apply to the x-axis
    which       = 'minor', # both major and minor ticks are affected
    bottom      = False,   # ticks along the bottom edge are off
    top         = False,   # ticks along the top edge are off
    labelbottom = True)    # labels along the bottom edge are off

def _savefig(filename=None, format=None):
  if filename == None or format == None:
    raise ValueError('no filename or format specified')
  matplotlib.pyplot.savefig(filename, format=format, bbox_inches="tight")

def savepng():
  """
  We generally write one Python script per figure.
  Save the PNG to the currently executing filename (without extension).
  """
  frame = inspect.stack()[1]
  filename = frame[0].f_code.co_filename

  _savefig(os.path.basename(filename)[:-3] + ".png", format="png")

def savepdf():
  """
  We generally write one Python script per figure.
  Save the PDF to the currently executing filename (without extension).
  """
  frame = inspect.stack()[1]
  filename = frame[0].f_code.co_filename

  _savefig(os.path.basename(filename)[:-3] + ".pdf", format="pdf")

if __name__ == '__main__':
  print("import me, don't use me directly!")
  sys.exit(0)
