"""
    Name: Allen Keettikkal
    NSID: alk423
    Student Number: 11278995
    Instructor: Jeffrey Long
"""


def to_string(node_chain):
    """
    Purpose:
        Create a string representation of the node chain.  E.g.,
        [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]

    Pre-conditions:
        :param node_chain:  A node-chain, possibly empty (None)

    Post_conditions:
        None

    Return: A string representation of the nodes.
    """
    # If there is an empty node chain:
    if node_chain is None:
        return 'EMPTY'

    # If there is one node in the node chain:
    if node_chain.get_next() is None:
        return '[ {} |'.format(str(node_chain.get_data())) + ' / ]'

    # Otherwise:
    else:
        return '[ {} | *-]-->'.format(str(node_chain.get_data())) + to_string(node_chain.get_next())
