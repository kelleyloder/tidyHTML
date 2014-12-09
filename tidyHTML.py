#Tidy HTML
#Eitan Goldberger and Kelley Loder

import os
import random
import sys
import re

def copy_to_new_file():
    '''copies content from file to new file w/ .bak extension'''
    file, filename = open_file()
    new_file = open(filename + '.bak', 'w')
    content = file.readlines()
    new_file.write(''.join(content))
    file.close()
    return new_file, content

def open_file():
    '''asks user for file, and open it'''
    filename = raw_input("Enter a file to read: ")
    file = open(filename, 'r')
    return file, filename

def strip_all(content):
    '''strips all whitespace at beginning and end of lines'''
    return [line.strip(' \t') for line in content]	

def make_lower(content):
    '''identifies all tags and makes them all lowercase'''
    for line in range(len(content)):
        ndx = 0
        while '<' in content[line][ndx : ]:
            start = content[line].find('<', ndx)
            stop = content[line].find('>', start)
            header_name = content[line][start + 1 :stop]
            content[line] = content[line][: start + 1] + header_name.lower() + content[line][stop : ]
            ndx = stop
    return content

def fix_nesting(content):
    '''fixes nesting errors'''
    line = 0
    start_tags = []
    extra_end_tags = []
    while line < len(content):
        ndx = 0
        while '<' in content[line][ndx : ]:
            start = content[line].find('<', ndx)
            stop = content[line].find('>', ndx)
            if classify(content[line][start : stop + 1]) == 'start':
                start_tags.append({ 'line': line, 'start_ndx' : start, 'stop_ndx' : stop })
            elif classify(content[line][start : stop + 1]) == 'end':
                if start_tag_exists(content, line, start, stop, start_tags):
                    end_tag_content = content[line][start : stop + 1]
                    last_start = start_tags.pop()
                    last_start_content = content[last_start['line']][ last_start['start_ndx'] : last_start['stop_ndx'] + 1 ]
                    if not tags_match(last_start_content, end_tag_content):
                        content[line] = content[line][ : start] + '</' + last_start_content[1 : ] + content[line][start : ]
                        start += len ('</' + last_start_content[1 : ])
                        stop += len ('</' + last_start_content[1 : ])
                else:
                    extra_end_tags.append({'line': line, 'start_ndx': start, 'stop_ndx': stop})
            ndx = stop + 1
        line += 1
    return content, extra_end_tags
                                          
def classify(str_tag):
    '''classifies a tag as start, end, or emtpy and returns this as a string'''
    list = ['area', 'base', 'basefont', 'br', 'col', 'frame', 'hr', 'img', 'input', 'isindex', 'link', 'meta', 'param']
    if str_tag[1] == '/':
        return 'end'
    for type in list:
        if type in str_tag:
            return 'empty'
    return 'start'
    
def tags_match(start_tag, end_tag):
    '''checks if start and end tag provided are the same, returns true or false'''
    return start_tag[1:-1] == end_tag[2:-1]
    
def start_tag_exists(content, line, start, stop, start_tags):
    '''checks if end tag has matching start tag in start_tags'''
    end_tag = content[line][start : stop + 1]
    for tag in start_tags:
        start_tag = content[tag['line']][ tag['start_ndx'] : tag['stop_ndx'] + 1 ]
        if tags_match(start_tag, end_tag):
            return True
    return False

def delete_xtra_end_tags(xtra_end_tags, content):
    for tag in reversed(xtra_end_tags):
        content[tag['line']] = content[tag['line']] [ : tag['start_ndx']] + content[tag['line']] [tag['stop_ndx'] + 1 : ]
    return content

def give_tags_new_line(content):
    '''returns new content w/ new lines for start and end tags'''
    line = 0
    while line < len(content):
        ndx = 0
        while '<' in content[line][ndx : ]:
            start = content[line].find('<', ndx)
            stop = content[line].find('>', start)
            type = classify(content[line][start : stop + 1])
            if type == 'start':
                if '</' + content[line][start + 1 : stop] in content[line]:
                    ndx = content[line].find('</' + content[line][start + 1 : stop]) + 1
                else:
                    if start != 0:
                        content[line], new_line = content[line][ : start] + '\n', content[line][start : ]
                        content.insert(line + 1, new_line)
                        ndx = start - 1
                    else:
                        ndx = stop
            elif type == 'end' and start != 0:
                content[line], new_line = content[line][ : start] + '\n', content[line][start : ]
                content.insert(line + 1, new_line)
                ndx = start - 1
            elif type == 'end' and start == 0:
                ndx = stop
            elif type == 'empty':
                ndx = stop
        line += 1
    return content

def delete_blank_lines(content):
    '''deletes any blank lines'''
    line = 0
    while line < len(content):
        temp_line = content[line]
        if temp_line.strip('\t ') == "\n":
            content.pop(line)
        else:
            line += 1
    return content

def add_blank_lines(content):
    '''adds needed blank lines'''
    line = 0
    start_tag_list = ['<head>', '<body>', '<h1>', '<h2>', '<h3>', '<h4>', '<h5>', '<h6>']
    while line < len(content):
        for name in start_tag_list:
            if name in content[line]:
                content.insert(line, '\n')
                line += 1
        line += 1
    return content
        
def find_tags(content):
    '''finds all the tags in content, and returns their indeces'''
    line = 0
    tags = []
    while line < len(content):
        ndx = 0
        while '<' in content[line][ndx : ]:
            start = content[line].find('<', ndx)
            stop = content[line].find('>', ndx)
            tags.append({'start_ndx': start, 'stop_ndx': stop, 'line':line, \
                         'type': classify(content[line][start : stop + 1])})
            ndx = content[line].find('>', ndx) + 1
        line += 1
    return tags

def same_line_tags(tags, content):
    '''removes from tags list the tags that have start/end on same line'''
    ndx = 0
    while ndx < len(tags):
        sec_tag_text = content[tags[ndx]['line']] [tags[ndx]['start_ndx'] : tags[ndx]['stop_ndx']]
        first_tag_text =  content[tags[ndx - 1]['line']] [tags[ndx - 1]['start_ndx'] : tags[ndx - 1]['stop_ndx']]
        if (tags[ndx]['type'] == 'end' and tags[ndx-1]['type'] == 'start') \
           and (tags_match(first_tag_text, sec_tag_text) \
                and tags[ndx-1]['line'] == tags[ndx]['line']):
            tags.pop(ndx)
            tags.pop(ndx-1)
        else:
            ndx += 1
    return tags

def indent_all_tags(tags, content):
    '''loops through tags, and indents content'''
    ndx = 0
    while ndx < len(tags):
        if tags[ndx]['type'] == 'start':
            line = tags[ndx]['line']
            end_ndx = find_end_tag(tags, ndx, content)
            end_line = tags[end_ndx]['line']
            content, tags = indent_lines(line + 1, end_line - 1, how_many_indents(content[line]) + 1, content, tags)
        ndx += 1
    return content, tags    

def find_end_tag(tags, start_tag_ndx, content):
    '''returns the ndx of the end tags in tags that matches start tag'''
    ndx = start_tag_ndx
    start_tag_text = content[tags[ndx]['line']] [tags[ndx]['start_ndx'] : \
    tags[ndx]['stop_ndx'] + 1]
    while (ndx < len(tags)):
        sec_tag_text = content[tags[ndx]['line']][tags[ndx]['start_ndx'] : \
        tags[ndx]['stop_ndx'] + 1]
        if tags[ndx]['type'] == 'end' and tags_match(start_tag_text, sec_tag_text):
            return ndx
        else:
            ndx += 1
    return None                                                 

def indent_lines(start_line, last_line, num_indents, content, tags):
    '''indents content from content[start_line : last_line] num_indents indentations'''
    for line in range(start_line, last_line + 1):
        content[line] = '\t' * num_indents + content[line].lstrip('\t ')
        for tag in filter(lambda tg: tg['line'] == line, tags):
            tag['start_ndx'] += 1
            tag['stop_ndx'] += 1
    return content,tags

def how_many_indents(line):
    '''returns how many \ts there are at beginning of line'''
    return len(line) - len(line.lstrip('\t'))

def line_length(content):
    '''ensures all lines are 80 characters or less'''
    line = 0
    while line < len(content):
        if len(content[line]) > 80:
            num_indents = how_many_indents(content[line])
            space_ndx = find_first_space_before_80(content[line])
            if space_ndx != -1:
                content[line], new_line = content[line][ : space_ndx] + '\n', content[line][space_ndx + 1: ]
                new_line = '\t' * num_indents + new_line
                content.insert(line + 1, new_line)
            else:
                line += 1
        else:
            line += 1
    return content

def find_first_space_before_80(line):
    '''finds first space before line is at 80 characters and returns the ndx'''
    ndx = 79
    while ndx > 0:
        ndx -= 1
        if line[ndx] == ' ':
            return ndx
    return -1

def create_output_file(content):
    '''uses random int generator to create new output file'''
    file_name = str(random.randint(1, sys.maxint)) + '.html'
    new_file = open(file_name, 'w')
    new_file.write(''.join(content))
    new_file.close()

def main():
    nf, content = copy_to_new_file()
    content = strip_all(content)
    content = make_lower(content)
    content, xtra = fix_nesting(content)
    content = delete_xtra_end_tags(xtra, content)
    content = give_tags_new_line(content)
    content = delete_blank_lines(content)
    content = add_blank_lines(content)
    tags = find_tags(content)
    tags = same_line_tags(tags, content)
    content, tags = indent_all_tags(tags, content)
    content = line_length(content)
    create_output_file(content)
    
if (__name__ == '__main__'):
    main()
