from elem import Elem, Text
from elements import (
    body,
    br,
    div,
    h1,
    h2,
    head,
    hr,
    html,
    img,
    li,
    meta,
    ol,
    p,
    span,
    table,
    td,
    th,
    title,
    tr,
    ul,
)

rules = {
    "html": {
        "allowed": [head, body],
        "min": 2,
        "order": [head, body],
        "max": 2,
    },
    "head": {
        "allowed": [title],
        "min": 1,
        "order": None,
        "max": 1,
    },
    "body": {
        "allowed": [h1, h2, div, table, ul, ol, span, Text],
        "min": 0,
        "order": None,
        "max": None,
    },
    "div": {
        "allowed": [h1, h2, div, table, ul, ol, span, Text],
        "min": 0,
        "order": None,
        "max": None,
    },
    "title": {
        "allowed": [Text],
        "min": 1,
        "order": None,
        "max": 1,
    },
    "h1": {
        "allowed": [Text],
        "min": 1,
        "order": None,
        "max": 1,
    },
    "h2": {
        "allowed": [Text],
        "min": 1,
        "order": None,
        "max": 1,
    },
    "li": {
        "allowed": [Text],
        "min": 1,
        "order": None,
        "max": 1,
    },
    "th": {
        "allowed": [Text],
        "min": 1,
        "order": None,
        "max": 1,
    },
    "td": {
        "allowed": [Text],
        "min": 1,
        "order": None,
        "max": 1,
    },
    "p": {
        "allowed": [Text],
        "min": 1,
        "order": None,
        "max": 1,
    },
    "span": {
        "allowed": [Text, p],
        "min": 0,
        "order": None,
        "max": None,
    },
    "ul": {
        "allowed": [li],
        "min": 1,
        "order": None,
        "max": None,
    },
    "ol": {
        "allowed": [li],
        "min": 1,
        "order": None,
        "max": None,
    },
    "tr": {
        "allowed": [td, th],
        "min": 1,
        "order": None,
        "max": None,
        "child": [td, th],
    },
    "table": {
        "allowed": [tr],
        "min": 0,
        "order": None,
        "max": None,
    },
    # self closing tags
    "img": {
        "allowed": [],
        "min": 0,
        "order": None,
        "max": 0,
    },
    "br": {
        "allowed": [],
        "min": 0,
        "order": None,
        "max": 0,
    },
    "hr": {
        "allowed": [],
        "min": 0,
        "order": None,
        "max": 0,
    },
    "meta": {
        "allowed": [],
        "min": 0,
        "order": None,
        "max": 0,
    },
}


class Page:
    def __init__(self, instance: Elem):
        self.instance = instance

    def is_valid(self):
        if isinstance(self.instance, Text):
            return True
        if self.instance.tag not in rules:
            return False
        for child in self.instance.content:
            if not Page(child).is_valid():
                return False

            allowed = rules[self.instance.tag]["allowed"]
            if allowed and not isinstance(child, tuple(allowed)):
                return False

        if (
            rules[self.instance.tag]["max"] is not None
            and len(self.instance.content) > rules[self.instance.tag]["max"]
            or rules[self.instance.tag]["min"] is not None
            and len(self.instance.content) < rules[self.instance.tag]["min"]
        ):
            return False

        if rules[self.instance.tag]["order"] is not None and not all(
            isinstance(child, expected)
            for child, expected in zip(
                self.instance.content, rules[self.instance.tag]["order"]
            )
        ):
            return False
        if self.instance.tag == "tr" and self.instance.content:
            first_child = self.instance.content[0]
            if isinstance(first_child, th):
                for child in self.instance.content[1:]:
                    if not isinstance(child, th):
                        return False
            if isinstance(first_child, td):
                for child in self.instance.content[1:]:
                    if not isinstance(child, td):
                        return False
        return True

    def __str__(self) -> str:
        if isinstance(self.instance, html):
            return "<!DOCTYPE html>\n" + str(self.instance)
        return str(self.instance)

    def write_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(str(self))


def main():
    # --- Valid full HTML document ---
    doc = html([head([title(Text("Hello"))]), body([h1(Text("World"))])])
    print("Valid HTML doc:", Page(doc).is_valid())  # True

    # --- __str__ with doctype ---
    print(Page(doc))  # should start with <!DOCTYPE html>

    # --- Non-html root: no doctype ---
    print(Page(h1(Text("hi"))))  # no doctype

    # --- Wrong tag ---
    bad = Elem("custom", content=[])
    print("Unknown tag:", Page(bad).is_valid())  # False

    # --- html with wrong order (body before head) ---
    wrong_order = html([body([h1(Text("oops"))]), head([title(Text("late"))])])
    print("Wrong order:", Page(wrong_order).is_valid())  # False

    # --- head with two titles ---
    two_titles = html([head([title(Text("one")), title(Text("two"))]), body([])])
    print("Two titles:", Page(two_titles).is_valid())  # False

    # --- ul with no li ---
    empty_ul = ul([])
    print("Empty ul:", Page(empty_ul).is_valid())  # False

    # --- tr mixing td and th ---
    mixed_tr = tr([td(Text("a")), th(Text("b"))])
    print("Mixed tr:", Page(mixed_tr).is_valid())  # False

    # --- Valid tr with only td ---
    valid_tr = tr([td(Text("a")), td(Text("b"))])
    print("Valid tr:", Page(valid_tr).is_valid())  # True

    # --- Text sneaking into html ---
    text_in_html = html([head([title(Text("ok"))]), body([Text("sneak")])])
    print("Text in body:", Page(text_in_html).is_valid())  # True (body allows Text)

    # Unknown tag deep in tree
    bad_deep = body([Elem("custom", content=[])])
    print("Unknown tag deep:", Page(bad_deep).is_valid())  # Should be False

    # --- write_to_file ---
    Page(doc).write_to_file("output.html")
    print("File written!")


if __name__ == "__main__":
    main()
