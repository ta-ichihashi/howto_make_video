# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from enum import Enum
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

class Author(Enum):
    organization: str = ''
    author_native: str = '市橋 卓'
    author_en: str = 'Takashi Ichihashi'

    @classmethod
    def get_strings(cls, delimiter=' '):
        return delimiter.join([e.value for e in cls])


# -- Project information -----------------------------------------------------

titles = ['DVD Blu-ray 作成手順']

project = ' '.join(titles)
copyright = '市橋　卓'
author = Author.author_native.value

# The full version, including alpha/beta/rc tags
release = '第1版'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'japanesesupport',
    'docxsphinx',
    'sphinx.ext.githubpages',
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.seqdiag',
    'sphinxcontrib.actdiag',
    'sphinxcontrib.nwdiag',
    'sphinxcontrib.youtube',
    'sphinxcontrib.applehelp'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

suppress_warnings = ["myst.header"]

docx_template = '_templates/template.docx'
exclude_patterns = []

language = 'ja'


# Config for plugins

numfig = True

# Fontpath for blockdiag (truetype font)
# blockdiag_fontpath = 'C:/Windows/fonts/YuGothM.ttc'
# Fontpath for blockdiag (truetype font)
blockdiag_fontpath = './source/assets/ipaexg.ttf'
actdiag_fontpath = './source/assets/ipaexg.ttf'
seqdiag_fontpath = './source/assets/ipaexg.ttf'
nwdiag_fontpath = './source/assets/ipaexg.ttf'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
# html_static_path = ['_static']
html_sidebars = {
    "**": [
        "search-field.html",
        "sbt-sidebar-nav.html"
        ]
}

html_theme_options = {
    "repository_url": "https://github.com/ta-ichihashi/howto_make_video",
    "use_repository_button": True,
    "home_page_in_toc": True,
}

myst_enable_extensions = [
    "amsmath",
    "attrs_image",
    "colon_fence",
    "deflist",
    "dollarmath",
    "amsmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "inv_link",
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

docx_documents = [
    ('index', 'howto_make_video.docx', {'title': 'Music method documents',
     'creator': 'Takashi Ichihashi', 'subject': 'How to make music video', }, True),
]

docx_style = '_templates/template.docx'

docx_coverpage = True
docx_pagebreak_before_section = 1
docx_pagebreak_after_table_of_contents = 0
docx_table_options = {
    'landscape_columns': 6,      #
    'in_single_page': True,      #
    'row_splittable': True,      #
    'header_in_all_page': True,  #
}


# latex_docclass = {'manual': 'jsbook'}

latex_elements = {
    # Latex figure (float) alignment
    #
    'figure_align': 'H',
    'sphinxsetup': "verbatimforcewraps, verbatimmaxunderfull=0"
}


latex_engine = 'lualatex'

latex_docclass = {'manual': 'ltjsbook'}

# 改行コマンド `\\` を挟んで連結する(A)
my_latex_title_lines = '\\\\'.join(titles)

latex_elements = {
    # (C) Polyglossiaパッケージを読み込まないようにする
    'polyglossia': '',
    'fontpkg': r'''
        \setmainfont{DejaVu Serif}
        \setsansfont{DejaVu Sans}
        \setmonofont{DejaVu Sans Mono}
        ''',
    'preamble': r'''

        % my_latex_title_linesをLaTeXの世界に持ち込む
        \newcommand{\mylatextitlelines}{''' + my_latex_title_lines + r'''}
        \newcommand{\mylatexauthorlines}{''' + Author.get_strings('\\\\') + r'''}

        % 表紙テンプレート内でアットマークが使われているため、アットマークを通常の文字として扱う
        \makeatletter

        % 表紙テンプレートを再定義(B)
        \renewcommand{\sphinxmaketitle}{%
            \let\sphinxrestorepageanchorsetting\relax
            \ifHy@pageanchor\def\sphinxrestorepageanchorsetting{\Hy@pageanchortrue}\fi
            \hypersetup{pageanchor=false}% avoid duplicate destination warnings
            \begin{titlepage}%
                \let\footnotesize\small
                \let\footnoterule\relax
                \noindent\rule{\textwidth}{1pt}\par
                \begingroup % for PDF information dictionary
                \def\endgraf{ }\def\and{\& }%
                \pdfstringdefDisableCommands{\def\\{, }}% overwrite hyperref setup
                \hypersetup{pdfauthor={\@author}, pdftitle={\@title}}%
                \endgroup
                \begin{flushright}%
                \sphinxlogo
                \py@HeaderFamily
                {\Huge \mylatextitlelines \par} % <--- ここで\mylatextitlelinesを使用(C)
                {\itshape\LARGE \py@release\releaseinfo \par}
                \vfill
                {\LARGE
                    \begin{tabular}[t]{l}
                    \mylatexauthorlines
                    %\@author
                    \end{tabular}\kern-\tabcolsep
                    \par}
                \vfill\vfill
                {\large
                \@date \par
                \vfill
                \py@authoraddress \par
                }%
                \end{flushright}%\par
                \@thanks
            \end{titlepage}%
            \setcounter{footnote}{0}%
            \let\thanks\relax\let\maketitle\relax
            %\gdef\@thanks{}\gdef\@author{}\gdef\@title{}
            \clearpage
            \ifdefined\sphinxbackoftitlepage\sphinxbackoftitlepage\fi
            \if@openright\cleardoublepage\else\clearpage\fi
            \sphinxrestorepageanchorsetting
        } % 表紙スタイル終わり
        % アットマークを特殊文字に戻す
        \makeatother

        \setcounter{tocdepth}{1}
        \usepackage[titles]{tocloft}
        %\usepackage[OT1]{fontenc}
        \cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
        \setlength{\cftchapnumwidth}{1.5cm}
        \setlength{\cftsecindent}{\cftchapnumwidth}
        \setlength{\cftsecnumwidth}{1.25cm}
        \addtolength{\footskip}{0mm}
        ''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex'
}


latex_show_urls = 'footnote'


# for epub


epub_title = project
epub_author = author
epub_basename = 'twincat_howto'
epub_language = 'ja'
epub_publisher = author
# epub_identifier = u'http://ascii.asciimw.jp/books/books/detail/978-4-04-868629-7.shtml'
epub_scheme = 'URL'
epub_tocdepth = 3
