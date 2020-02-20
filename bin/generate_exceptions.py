"""
SWORD exception generator

A slightly hacky script to generate exception definitions from the specification for inclusion in
sword3common/exceptions.py.

If the spec changes, use this script to regenerate all the SwordException subclasses.
"""

import collections
import textwrap
from http import HTTPStatus

import requests
import lxml.etree

exception_subclassing = {
    "Gone": ("NotFound",),
}

response = requests.get("https://swordapp.github.io/swordv3/swordv3.html")

page = lxml.etree.fromstring(response.content, parser=lxml.etree.HTMLParser())

ExceptionDefinition = collections.namedtuple(
    "ExceptionDefinition", ("name", "status_code", "reason", "bases")
)


table = page.xpath("//a[@name='9.8.1.']/parent::*/following-sibling::table")[0]

exception_definitions = [
    ExceptionDefinition(
        name=row[0].text,
        status_code=HTTPStatus(int(row[1].text)),
        reason="".join(row[2].itertext()).strip(),
        bases=exception_subclassing.get(row[0].text, ("SwordException",)),
    )
    for row in table.xpath("tbody/tr")
]

i, seen_names = 0, {"SwordException"}
while i < len(exception_definitions):
    missing_bases = set(exception_definitions[i].bases) - seen_names
    if missing_bases:
        j = max(
            j for j, e in enumerate(exception_definitions) if e.name in missing_bases
        )
        exception_definitions.insert(j, exception_definitions.pop(i))
    else:
        seen_names.add(exception_definitions[i].name)
        i += 1


for exception_definition in exception_definitions:
    block = textwrap.dedent(
        f"""
        class {exception_definition.name}({', '.join(exception_definition.bases)}):
            status_code = HTTPStatus.{exception_definition.status_code.name}
            name = {repr(exception_definition.name)}
            reason = {repr(exception_definition.reason)}
        """
    )

    print(block)
