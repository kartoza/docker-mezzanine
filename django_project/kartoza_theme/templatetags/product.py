import datetime
from django import template

register = template.Library()


@register.filter
def sort_product_options(value):
    # sorting option1
    old_list = list()
    ref_list = {}
    for label, choice in value.fields['option1'].choices:
        # strip out %B %d-%d %Y into %B %d %Y
        temp_choice = choice.split('-')
        temp_year = temp_choice[1].split(' ')
        # ref_list is called with the format %B %d
        ref_list[temp_choice[0]] = choice
        old_list.append(temp_choice[0] + "," + temp_year[1])
    # new_list new format: %B %d,%Y
    # add comma so it can be fetched easily for the ref_list
    new_list = sorted(old_list, key=lambda x: datetime.datetime.strptime(x, '%B %d,%Y'))
    # construct the new list based on the original content %B %d-%d %Y
    new_sorted_list = list()
    for new_sorted_choice in new_list:
        stripped_new_sorted_choice = new_sorted_choice.split(",")
        new_sorted_list.append(ref_list[stripped_new_sorted_choice[0]])

    field1 = list()
    for nsl in new_sorted_list:
        field1.append((nsl, nsl))
    value.fields['option1'].choices = field1

    # sorting option2
    new_option2 = list()
    for label, choice in value.fields['option2'].choices:
        new_option2.append(label)

    new_option2 = sorted(new_option2)
    field2 = list()
    for nsl in new_option2:
        field2.append((nsl, nsl))
    value.fields['option2'].choices = field2

    return value
