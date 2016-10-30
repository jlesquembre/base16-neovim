# Base16 Vim
See the [Base16 repository](https://github.com/chriskempson/base16) for more information.
This theme was built with [Base16 Builder](https://github.com/chriskempson/base16-builder).

Supports graphical Vim and console Vim.

![Base16 Vim](https://raw.github.com/chriskempson/base16-vim/master/base16-vim.png)


## Supported plugins

* [Startify](https://github.com/mhinz/vim-startify)
* [Fugitive](https://github.com/tpope/vim-fugitive)
* [GitGutter](https://github.com/airblade/vim-gitgutter)
[//]: # * [EasyMotion](https://github.com/Lokaltog/vim-easymotion)
[//]: # * [Sneak](https://github.com/justinmk/vim-sneak)
[//]: # * [Indent Guides](https://github.com/nathanaelkane/vim-indent-guides)
[//]: # * [indentLine](https://github.com/Yggdroot/indentLine)
* [Better Whitespace](https://github.com/ntpeters/vim-better-whitespace)
[//]: # * [Rainbow Parenthesis](https://github.com/kien/rainbow_parentheses.vim)
[//]: # * [Rainbow Parenthesis Improved](https://github.com/oblitum/rainbow)
[//]: # * [vim-notes](https://github.com/xolox/vim-notes)
[//]: # * [Gundo](http://sjl.bitbucket.org/gundo.vim/)
[//]: # * [undotree](https://github.com/mbbill/undotree)
[//]: # * [Tagbar](https://github.com/majutsushi/tagbar)
[//]: # * [vim-plug](https://github.com/junegunn/vim-plug)
* [vim-halo](https://github.com/mhinz/vim-halo)
[//]: # * [gitv](https://github.com/gregsexton/gitv)
[//]: # * [vim-painter](https://github.com/thinca/vim-painter)


## Terminal Themes
For terminal Vim (non-gui) please ensure you are using a base16 terminal theme.

* [iTerm2](https://github.com/chriskempson/base16-iterm2)

## Installation

Add `colorscheme base16-default-dark` to your `~/.vimrc`.

### Vundle
Add the following to your `~/.vimrc` file and run `PluginInstall` in Vim.

    Plugin 'chriskempson/base16-vim'

### Pathogen

    cd ~/.vim/bundle
    git clone https://github.com/chriskempson/base16-vim.git

### Manual

    cd ~/.vim/colors
    git clone git://github.com/chriskempson/base16-vim.git base16
    cp base16/colors/*.vim .

## 256 colorspace
If using a Base16 terminal theme designed to keep the 16 ANSI colors intact (a "256" variation) **and** have sucessfully modified your 256 colorspace with [base16-shell](https://github.com/chriskempson/base16-shell) you'll need to add the following to your `~/.vimrc` **before** the colorsheme declaration.

    let base16colorspace=256  " Access colors present in 256 colorspace

This will cause vim to access the colours in the modified 256 colorspace. Please **do not** enable this simply because you have a 256 color terminal as this will cause colors to be displayed incorrectly.

## Troubleshooting
There is a script to help troubleshoot colour issues called `colortest` available in the [Base16 Shell](https://github.com/chriskempson/base16-shell) repository.

### Green line numbers
![green line numbers screenshot](https://raw.github.com/chriskempson/base16-vim/master/without-base16colorspace-256-with-256-terminal-theme.png)

If your Vim looks like the above image you are using a 256 terminal theme without setting `let base16colorspace=256` in your `~/.vimrc`. Either set `let base16colorspace=256` in your `~/.vimrc` or use a non 256 terminal theme.

### Blue line numbers
![blue line numbers screenshot](https://raw.github.com/chriskempson/base16-vim/master/with-base16colorspace-256-without-base16-shell.png)

If your Vim looks like the above image you are setting `let base16colorspace=256` in your `~/.vimrc` but either not running [Base16 Shell](https://github.com/chriskempson/base16-shell) or [Base16 Shell](https://github.com/chriskempson/base16-shell) is not working for your terminal. Either ensure [Base16 Shell](https://github.com/chriskempson/base16-shell) is working by running the `colortest` available in the [Base16 Shell](https://github.com/chriskempson/base16-shell) repository or not setting `let base16colorspace=256` in your `~/.vimrc`.
