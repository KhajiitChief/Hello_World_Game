
class Cart():
    def __init__(self):
        self.items = {}

    def append(self, item):
        self.items[item.name] = item

    def __str__(self):
        print("""
                              /_`()
                             //
|```|```|```|````|```|```|```|
|```|```|```|Cart|```|```|```|
|```|```|```|````|```|```|```|
`||````````````````````````||`
 ||________________________||
/``\                      /``\ 
\__/                      \__/
""")
        out = '\t'.join(["Name    ", "        Use"])
        for item in self.items.values():
            out += '\n' + '\t'.join([str(c) for c in [item.name, "   ", item.use]])
        return out
cart = Cart()
