from Node import Node
import bisect
import itertools
import operator

class BTree(object):
    BRANCH = LEAF = Node

    def __init__(self, order):
        self.order = order
        self._root = self._bottom = self.LEAF(self)

    def _path_to(self, item):
        current = self._root
        ancestry = []

        while getattr(current, "children", None):
            index = bisect.bisect_left(current.contents, item)
            ancestry.append((current, index))
            if index < len(current.contents) \
                    and current.contents[index] == item:
                return ancestry
            current = current.children[index]

        index = bisect.bisect_left(current.contents, item)
        ancestry.append((current, index))
        present = index < len(current.contents)
        present = present and current.contents[index] == item

        return ancestry

    def _present(self, item, ancestors):
        last, index = ancestors[-1]
        return index < len(last.contents) and last.contents[index] == item

    def insert(self, item):
        current = self._root
        ancestors = self._path_to(item)
        node, index = ancestors[-1]
        while getattr(node, "children", None):
            node = node.children[index]
            index = bisect.bisect_left(node.contents, item)
            ancestors.append((node, index))
        node, index = ancestors.pop()
        node.insert(index, item, ancestors)

    def remove(self, item):
        current = self._root
        ancestors = self._path_to(item)

        if self._present(item, ancestors):
            node, index = ancestors.pop()
            node.remove(index, ancestors)
        else:
            raise ValueError("%r not in %s" % (item, self.__class__.__name__))

    def __contains__(self, item):
        return self._present(item, self._path_to(item))

    def __iter__(self):
        def _recurse(node):
            if node.children:
                for child, item in zip(node.children, node.contents):
                    for child_item in _recurse(child):
                        yield child_item
                    yield item
                for child_item in _recurse(node.children[-1]):
                    yield child_item
            else:
                for item in node.contents:
                    yield item

        for item in _recurse(self._root):
            yield item

    def __repr__(self):
        def recurse(node, accum, depth):
            accum.append(("  " * depth) + repr(node))
            for node in getattr(node, "children", []):
                recurse(node, accum, depth + 1)

        accum = []
        recurse(self._root, accum, 0)
        return "\n".join(accum)

    @classmethod
    def bulkload(cls, items, order):
        tree = object.__new__(cls)
        tree.order = order

        leaves = tree._build_bulkloaded_leaves(items)
        tree._build_bulkloaded_branches(leaves)

        return tree

    def _build_bulkloaded_leaves(self, items):
        minimum = self.order // 2
        leaves, seps = [[]], []

        for item in items:
            if len(leaves[-1]) < self.order:
                leaves[-1].append(item)
            else:
                seps.append(item)
                leaves.append([])

        if len(leaves[-1]) < minimum and seps:
            last_two = leaves[-2] + [seps.pop()] + leaves[-1]
            leaves[-2] = last_two[:minimum]
            leaves[-1] = last_two[minimum + 1:]
            seps.append(last_two[minimum])

        return [self.LEAF(self, contents=node) for node in leaves], seps

    def _build_bulkloaded_branches(self, (leaves, seps)):
        minimum = self.order // 2
        levels = [leaves]

        while len(seps) > self.order + 1:
            items, nodes, seps = seps, [[]], []

            for item in items:
                if len(nodes[-1]) < self.order:
                    nodes[-1].append(item)
                else:
                    seps.append(item)
                    nodes.append([])

            if len(nodes[-1]) < minimum and seps:
                last_two = nodes[-2] + [seps.pop()] + nodes[-1]
                nodes[-2] = last_two[:minimum]
                nodes[-1] = last_two[minimum + 1:]
                seps.append(last_two[minimum])

            offset = 0
            for i, node in enumerate(nodes):
                children = levels[-1][offset:offset + len(node) + 1]
                nodes[i] = self.BRANCH(self, contents=node, children=children)
                offset += len(node) + 1

            levels.append(nodes)

        self._root = self.BRANCH(self, contents=seps, children=levels[-1])