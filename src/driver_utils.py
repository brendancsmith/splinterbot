#------------------------------ imports --------------------------------

# standard modules
# N/A

# intra-project modules
# N/A

# external libraries
# N/A

#-----------------------------------------------------------------------


def option_values_of_select(selectEl):
    """Retrieves the value attributes of the option nodes within a
    select tag"""

    optionEls = selectEl.find_by_tag('option')
    optionValues = [el.value for el in optionEls]

    return optionValues
