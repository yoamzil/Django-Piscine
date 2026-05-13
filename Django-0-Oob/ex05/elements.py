from elem import Elem, Text


class html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag="html", attr=attr, content=content)


class body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag="body", attr=attr, content=content)


class head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag="head", attr=attr, content=content)


class title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag="title", attr=attr, content=content)


class meta(Elem):
    def __init__(self, attr={}):
        super().__init__(tag="meta", attr=attr, tag_type="simple")


class img(Elem):
    def __init__(self, attr={}):
        super().__init__(tag="img", attr=attr, tag_type="simple")


class table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag="table", attr=attr, content=content)


class th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag="th", attr=attr, content=content)


class tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag="tr", attr=attr, content=content)


class td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag="td", attr=attr, content=content)


class ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag="ul", attr=attr, content=content)


class li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag="li", attr=attr, content=content)


class ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag="ol", attr=attr, content=content)


class h1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag="h1", attr=attr, content=content)


class h2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag="h2", attr=attr, content=content)


class p(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag="p", attr=attr, content=content)


class div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag="div", attr=attr, content=content)


class span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag="span", attr=attr, content=content)


class hr(Elem):
    def __init__(self, attr={}):
        super().__init__(tag="hr", attr=attr, tag_type="simple")


class br(Elem):
    def __init__(self, attr={}):
        super().__init__(tag="br", attr=attr, tag_type="simple")

def main():
    doc = html([
        head([
            title(Text('"Hello ground!"'))
        ]),
        body([
            h1(Text('"Oh no, not again!"')),
            img(attr={"src": "http://i.imgur.com/pfp3T.jpg"})
        ])
    ])
    print(doc)

if __name__ == "__main__":
    main()