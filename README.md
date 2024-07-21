
<img align="left" width="340px" src="https://github.com/ftdot/pyrolog/blob/master/banner.png?raw=true" />
<h1><strong>🔥 Pyrolog</strong></h1>
<p>Pretty logging — Pretty project</p>

---

[![Issues](https://img.shields.io/github/issues/ftdot/pyrolog?style=for-the-badge)](https://github.com/ftdot/pyrolog/issues)
[![Latest release](https://img.shields.io/github/v/release/ftdot/pyrolog?style=for-the-badge)](https://github.com/ftdot/pyrolog/releases)
[![PyPI](https://img.shields.io/pypi/v/pyrolog?style=for-the-badge)](https://pypi.org/project/pyrolog)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pyrolog?style=for-the-badge)
[![Documentation](https://img.shields.io/readthedocs/pyrolog?style=for-the-badge)](https://pyrolog.readthedocs.io)

---

### Contents

[![Installation](https://img.shields.io/badge/%23-Installation-green?style=for-the-badge)](#installation)

[![Basic example](https://img.shields.io/badge/%23-Basic_example-blue?style=for-the-badge)](#basic-example)

[![Most all the features](https://img.shields.io/badge/%23-Most_all_the_features-blue?style=for-the-badge)](#most-all-the-features-example)

[![License](https://img.shields.io/badge/%23-License-blue?style=for-the-badge)](#-license)

---

🇺🇦 Made with ❤️ in Ukraine!

## Installation

You can install\update by using this command:

```shell
$ pip install -U pyrolog
```

If you want to contribute: just fork, commit you changes and create PR [there](https://github.com/ftdot/pyrolog/pulls).
Don't forget to comment your changes while contributing!

## Basic example

After you installed the library, you can create your first logger:

```python

import pyrolog

# You can use debug, exception, info, warn, error, critical log levels.
# exception - is log level that recommended to use by default, if you don't want to log debug information
logger = pyrolog.get_colored_logger('exception')

x = 12

# loggers supports formatting. With colored loggers it will be pretty colored
logger.info('x is {}', x)

```

There is only 1% of all the features.
See the example below for more features

## Most all the features example

<img align="center" src="https://github.com/ftdot/pyrolog/blob/master/presentation.png?raw=true" />

There is not all the features. See the [docs](https://pyrolog.readthedocs.org/)

### 📃 License

- Pyrolog library source code is under LGPL-2.1 license.
- Build utilities (utils/ directory) source code is under MIT license.

By copying, distributing and modification this library, you agree with
[GNU LGPL 2.1 Terms](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).
License is applies to all source files of the library.
Is the python files, reStructured files, etc.
License also provides NO WARRANTY for this library!

```
    Pyrolog. Pretty logging library
    Copyright (C) 2023  ftdot

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
    USA
```

```
MIT License

Copyright (c) 2023 ftdot (https://github.com/ftdot)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
