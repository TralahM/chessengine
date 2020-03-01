
[![Build Status](https://travis-ci.com/TralahM/chessengine.svg?branch=master)](https://travis-ci.com/TralahM/chessengine)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)
[![Organization](https://img.shields.io/badge/Org-TralahTek-blue.svg)](https://github.com/TralahTek)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![HitCount](http://hits.dwyl.io/TralahM/chessengine.svg)](http://dwyl.io/TralahM/chessengine)
[![Inline Docs](http://inch-ci.org/github/TralahM/chessengine.svg?branch=master)](http://inch-ci.org/github/TralahM/chessengine)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/TralahM/pull/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/Naereen/StrapDown.js.svg)](https://gitHub.com/TralahM/chessengine/pull/)
[![GitHub version](https://badge.fury.io/gh/Naereen%2FStrapDown.js.svg)](https://github.com/TralahM/chessengine).

# chessengine.

# Description

[![TralahM](https://img.shields.io/badge/Engineer-TralahM-blue.svg?style=for-the-badge)](https://github.com/TralahM)
[![TralahM](https://img.shields.io/badge/Maintainer-TralahM-green.svg?style=for-the-badge)](https://github.com/TralahM)

# Documentation

[Read the Docs](https://chessengine.readthedocs.io)
# Chess and Bitboards
## Information to be Stored
- Board Position (location of all pieces)
- En-passant square if any
- Castling Permissions
- Draw by repetion/ 50-move stats (often stored outside the board structure)
- Side to move
### Expectated size
- 12 Bitboards (12*64 bits)
- Castling (4 bits)
- Side to move (1 bit)
- E-P square (6 bits)

Total 779 bits (98 bytes)
## Representation

Bitboards are an interesting method of representing a chess board invented in Russia (with the program Kaissa, circa 1977). They were made widely popular by Robert Hyatt and his program Crafty, a direct derivatve of "Cray Blitz" written circa 1985, which he had made open source. The basic idea is that we are going to be exploiting the coincidental fact that a chess board has 64 squares and that modern computers can easily manipulate 64-bit integers.

So what are the motivations of bitboards? One of them is memory compaction of the state of the board and of possible future boards.
Another is that many questions about movement and capturing of pieces can be answered "in parallel" by __OR__ing, __AND__ing, __XOR__ing, and __shifting__ various bitboards instead of building _complex_ _data_ _structures_ in memory to hold views of the board by certain pieces and valid movement spaces and then _sets_ of those data structures for __AI__ exploration of the movement space.

When I went looking for _bitboard_ _algorithms_ on the web, I found a lot of material. However, I did not find satisfaction in the explanations of most of these pages and no one really had enough knowledge or sufficient detail in one spot to actually write a _chess_ _engine_ based on the concept of bitboards.
So, these pages are an attempt to condense the knowledge I've learned along with numerous detailed visual explanations of the concepts involved as to help not only myself, but others, to intuitively understand bitboards.
I've specifically written the material towards clarity and a full blown chess engine might very well optimize many steps or bit operations away.
Also, the default language I will write various statements and expressions in will be __C__.
[Read More about
Bitboards](http://pages.cs.wisc.edu/~psilord/blog/data/chess-pages/)

# How to Install


## Building from Source for Developers

```Bash
git clone https://github.com/TralahM/chessengine.git
cd chessengine
```

# Contributing
[See the Contributing File](CONTRIBUTING.rst)


[See the Pull Request File](PULL_REQUEST_TEMPLATE.md)


# Support

# LICENCE
[Read the license here](LICENSE)


# Acknowledgements


