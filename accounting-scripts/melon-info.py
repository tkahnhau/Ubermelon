"""
Prints out all the melons in our inventory
"""

from melons import all_melons


def print_melon(melons):
    """Print the name and attributes of melons on offer at Ubermelon"""

    for name, attributes in melons.iteritems():

        print name

        for index, data in attributes.iteritems():
            print "{}: {}".format(index, data)

        print "\n"


print_melon(all_melons)


# def add_attribute(attribute):
#     """Inable seamless addition of new attributes to our master melon list"""

#     print "Please enter new data for each melon:"

#     for melon in all_melons:
#         new_fact = raw_input("{}: ".format(melon))

#         all_melons[melon][attribute] = new_fact
