"""
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
"""

import pyrolog

from typing import Any

from pathlib import Path

templates_path = Path('utils/templates')

files = [
    (Path('setup.cfg'), templates_path / 'setup.cfg'),
    (Path('pyrolog/version.py'), templates_path / 'pyrolog_version.py'),
    (Path('pyproject.toml'), templates_path / 'pyproject.toml'),
]

default_format_dict = {
    'version': '1.0.0',
    'version_major': '1',
    'version_minor': '0',
    'version_patch': '0',
    'version_release_level': 'release',
    'last_commit': '1234abc',
}

logger = pyrolog.get_colored_logger()


def format_template(template: str, format_dict: dict[str, Any]):

    output = template

    for k, v in format_dict.items():
        output = output.replace(f'{{{{ {k} }}}}', v)

    return output


def format_all_files(files_list: list[tuple[Path, Path]], format_dict: dict[str, str]):

    for output_path, template_path in files_list:

        logger.info('Formatting template {} to {}', template_path, output_path)

        template = template_path.read_text(encoding='utf8')
        output_path.write_text(format_template(template, format_dict))

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Helps with updating version of the library')

    parser.add_argument('version',
                        help='New version value. (Must be formatted as x.x.x)')
    parser.add_argument('release_level',
                        help='Level of the release. (Available: release, beta, alpha)')
    parser.add_argument('last_commit',
                        help='Last commit hash with the library code changes.')

    args = parser.parse_args()

    try:
        format_all_files(
            files,
            dict(
                version=args.version,
                version_release_level=args.release_level,
                last_commit=args.last_commit,
                **{k: v for k, v in zip(['version_major', 'version_minor', 'version_patch'], args.version.split('.'))}
            )
        )
    except Exception as e:
        logger.error('Cannot to format files!')
        logger.exception('Exception has occurred', exc=e)
