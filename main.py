import re as regex
import os

get_translate = regex.compile('Yii::t\(\W*\'[\w-]+\'\W*,\W*\'[\w\s!:?\(\)\. ]*\'\s*\)')

main_dir = '/var/www/sites/site/modules'
main_array = []


def findAllMatches(file_name):
    file = open(file_name, 'r')
    match_result = get_translate.findall(file.read())
    for row in match_result:
        print(row)
        if row not in main_array:
            main_array.append(row)
    file.close()


def findAllFile(main_path):
    for path in os.listdir(main_path):
        if os.path.isdir(os.path.join(main_path, path)):
            findAllFile(os.path.join(main_path, path))
        if os.path.isfile(os.path.join(main_path, path)):
            findAllMatches(os.path.join(main_path, path))


findAllFile(main_dir)

file_list = []
get_category = regex.compile('(?<=\(\')\w+(?=\')')
get_value = regex.compile('\'[\w\s!:?\(\)\. ]*\'\s*(?=\))')
for row in main_array:
    translate_category = get_category.findall(row)[0]
    translate_value = get_value.findall(row)[0]
    file = open(translate_category + '.php', 'a')
    file.write(translate_value + ' => ,\n')
    file.close()
