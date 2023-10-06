
These files give a demonstration of the visitor patterns used in the
SCIL compiler for the many traversals of the AST.

In this example, we do not use an AST, but a simple binary tree
structure with two types of nodes representing internal nodes (Node)
and leaves (Leaf).

The main idea is to implement recursive traversals once, so that
repeated traversals with different purposes only specify the code
that actually does something. Note in particular that if for some
node types nothing needs to be done, no code has to be specified,
but the recursive traversal still proceeds through those nodes.

For this little example, there is very little or no savings, but
for ASTs with 20-100 difference node types and many traversals
(symbol collection, type checking, code generation, etc.), the
savings are significant and - not less important - code maintenance
significantly easier.
