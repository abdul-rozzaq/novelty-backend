from django import template

register = template.Library()


def format_number(number):
    number_str = str(number)[::-1]
    formatted_number_list = []
    for i in range(0, len(number_str), 3):
        chunk = number_str[i:i + 3]
        formatted_number_list.append(chunk)
    formatted_number = ','.join(formatted_number_list)
    return formatted_number[::-1]



@register.simple_tag
def calculate_total_price(books):
    total_price = sum(book.price for book in books if book.price)
    return format_number(total_price)



@register.simple_tag
def calculate_total_count(books):
    return sum(book.count for book in books if book.count)