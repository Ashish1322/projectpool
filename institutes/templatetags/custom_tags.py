from django import template

register = template.Library()

# Creating filetr to use the forloop counter as a index. posoting is the forloop.counter starts form 1
@register.filter(name='index')
def index(sequence, position):
    return sequence[position-1]