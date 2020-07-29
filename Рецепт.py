def printRecept(itemsD,leftWidth,rightWidth):
    print('Рецепт'. center(leftWidth + rightWidth,'-'))
    for k, v in itemsD.items():
        print(k.ljust(leftWidth,'.')+str(v).rjust(rightWidth))
Ingredients = {'Орурец':4, 'Помилор':2}
printRecept(Ingredients,12,5)
print('Нажмите Enter для завершения программы')
input()