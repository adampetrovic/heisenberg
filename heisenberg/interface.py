import texttable
import os


class AsciiTable(object):

    def __init__(self, header):
        alignment = {
            'horizontal': ['l' for _ in header],
            'vertical': ['m' for _ in header],
        }

        self.table = texttable.Texttable(max_width=300)
        self.table.set_deco(
            (texttable.Texttable.BORDER |
             texttable.Texttable.HEADER |
             texttable.Texttable.VLINES)
        )
        self.rows = []
        self.rows.append(header)

    def add_rows(self, data):
        for row in data:
            self.rows.append(row)

    def draw(self):
        self.table.add_rows(self.rows)
        print self.table.draw()
