from django.shortcuts import render
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def get_recipes_tool(request, recipes_name):
    food_name = DATA.get(recipes_name)
    food_cnt = request.GET.get('serving', 1)
    data_dict = {}
    for key, value in food_name.items():
        data_dict[key] = value * int(food_cnt)
    context = {'recipes_name': data_dict}
    return render(request, 'calculator/ingredients.html', context)


def get_main(request):
    return HttpResponse('ДОБРО ПОЖАЛОВАТЬ И ПРИЯТНОГО АППЕТИТА')
