"""
SWORD exception generator

A slightly hacky script to generate exception definitions from the specification for inclusion in
sword3common/exceptions.py.

If the spec changes, use this script to regenerate all the SwordException subclasses.
"""

import textwrap
from http import HTTPStatus

import requests
import lxml.etree

response = requests.get('https://swordapp.github.io/swordv3/swordv3.html')

page = lxml.etree.fromstring(response.content, parser=lxml.etree.HTMLParser())

table = page.xpath("//a[@name='9.8.1.']/parent::*/following-sibling::table")[0]
for row in table.xpath('tbody/tr'):
    name = row[0].text
    status_code = HTTPStatus(int(row[1].text))
    reason = ''.join(row[2].itertext()).strip()

    block = textwrap.dedent(f"""
        class {name}(SwordException):
            status_code = HTTPStatus.{status_code.name}
            name = {repr(name)}
            reason = {repr(reason)}
    """)

    print(block)
