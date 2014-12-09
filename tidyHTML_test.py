#Tidy HTML Test
#Eitan Goldberger and Kelley Loder

import unittest
from tidyHTML import *
import tidyHTML

class TestTidyHTML(unittest.TestCase):

    def test_give_tags_new_line(self):
        content = ['<html><head>\n', \
                   '<title>Gensler &amp; Zudans Family Dentistry</title>\n', \
                   '<style></style></head>\n', '<body>\n', '\n', '\n', \
                   '<area><base>\n', \
                   'sdfdf<h1>WELCOME TO GENSLER &amp; ZUDANS FAMILY DENTISTRY!</h1>\n', \
                   '<img src="gensler_and_zudans_family_dentistry.jpg">\n', \
                   '\n', '<hello>\n', '\n', 'asfasf</hello>\n', '\n', '\n', \
                   '<p>Address:<br>\n', '1303 Mount Holly Rd.<br>\n', \
                   'Burlington, NJ 08016\n', \
                   '<h2> whats up with cats???!?!?!!?\n', '\n', \
                   '</h2></p>\n', '\n', \
                   '<h3> sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg </h3>\n', '\n', \
                   '</body>  </endtagwithnostarttag>    </html>']
        content_after_give_tags_new_line = ['<html>\n', '<head>\n', \
                   '<title>Gensler &amp; Zudans Family Dentistry</title>\n', \
                   '<style></style>\n', '</head>\n', '<body>\n', '\n', '\n', \
                   '<area><base>\n', \
                   'sdfdf<h1>WELCOME TO GENSLER &amp; ZUDANS FAMILY DENTISTRY!</h1>\n', \
                   '<img src="gensler_and_zudans_family_dentistry.jpg">\n', \
                   '\n', '<hello>\n', '\n', 'asfasf\n', '</hello>\n', '\n', '\n', \
                   '<p>Address:<br>\n', '1303 Mount Holly Rd.<br>\n', \
                   'Burlington, NJ 08016\n', \
                   '<h2> whats up with cats???!?!?!!?\n', '\n', \
                   '</h2>\n', '</p>\n', '\n', \
                   '<h3> sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg </h3>\n', '\n', \
                   '</body>  \n', '</endtagwithnostarttag>    \n', '</html>']
        self.assertEqual(give_tags_new_line(content), content_after_give_tags_new_line)

        content = ['<html><head>\n', 'cats cats cats</head>\n', '<h1>caaaaaaaats</h1>\n']
        content_after_give_tags_new_line = ['<html>\n', '<head>\n', 'cats cats cats\n', '</head>\n', '<h1>caaaaaaaats</h1>\n']
        self.assertEqual(give_tags_new_line(content), content_after_give_tags_new_line)
        
    def test_strip_all(self):
        content = ['       <head> i love cats! </head>      cat cat!   ', \
                   '   still love cats.... why are cats so cool?     ']
        content_after_strip_all = ['<head> i love cats! </head>      cat cat!', \
                                   'still love cats.... why are cats so cool?']
        self.assertEqual(strip_all(content), content_after_strip_all)

        content = ['      <html><head>\n', \
                   '<TITLE>Gensler &amp; Zudans Family Dentistry</title>\n', \
                   '<style></style></head>\n', '  <body>\n', '\n', '\n', \
                   '<area><base>\n', \
                   'sdfdf<h1>WELCOME TO GENSLER &amp; ZUDANS FAMILY DENTISTRY!</H1>\n', \
                   '          <img src="gensler_and_zudans_family_dentistry.jpg">\n', \
                   '\n', '<hello>\n', '\n', '    asfasf</HELLO>\n', '\n', '           \n', \
                   '       <p>Address:<br>\n', '1303 Mount Holly Rd.<br>\n', \
                   '   Burlington, NJ 08016\n', \
                   '              <h2> whats up with cats???!?!?!!?\n', '\n', \
                   '                    </h2></p>\n', '\n', \
                   '<h3> sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg </h3>\n', '\n', \
                   '</BODY>  </endtagwithnostarttag>    </html>']
        content_after_strip_all = ['<html><head>\n', \
                   '<TITLE>Gensler &amp; Zudans Family Dentistry</title>\n', \
                   '<style></style></head>\n', '<body>\n', '\n', '\n', \
                   '<area><base>\n', \
                   'sdfdf<h1>WELCOME TO GENSLER &amp; ZUDANS FAMILY DENTISTRY!</H1>\n', \
                   '<img src="gensler_and_zudans_family_dentistry.jpg">\n', \
                   '\n', '<hello>\n', '\n', 'asfasf</HELLO>\n', '\n', '\n', \
                   '<p>Address:<br>\n', '1303 Mount Holly Rd.<br>\n', \
                   'Burlington, NJ 08016\n', \
                   '<h2> whats up with cats???!?!?!!?\n', '\n', \
                   '</h2></p>\n', '\n', \
                   '<h3> sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg </h3>\n', '\n', \
                   '</BODY>  </endtagwithnostarttag>    </html>']
        self.assertEqual(strip_all(content), content_after_strip_all)

    def test_find_tags(self):
         content = ['<html>\n', '<head>\n', \
                   '<title>Gensler &amp; Zudans Family Dentistry</title>\n', \
                   '<style></style></head>\n', '<body>\n', '\n', '\n', \
                   '<area><base>\n', \
                   '<h1>WELCOME TO GENSLER &amp; ZUDANS FAMILY DENTISTRY!</h1>\n', \
                   '<img src="gensler_and_zudans_family_dentistry.jpg">\n', \
                   '</body>\n', '</endtagwithnostarttag>\n', '</html>']
         tags = [{'start_ndx': 0, 'stop_ndx': 5, 'line': 0, 'type': 'start'}, \
                 {'start_ndx': 0, 'stop_ndx': 5, 'line': 1, 'type': 'start'}, \
                 {'start_ndx': 0, 'stop_ndx': 6, 'line': 2, 'type': 'start'}, \
                 {'start_ndx': 44, 'stop_ndx': 51, 'line': 2, 'type': 'end'}, \
                 {'start_ndx': 0, 'stop_ndx': 6, 'line': 3, 'type': 'start'}, \
                 {'start_ndx': 7, 'stop_ndx': 14, 'line': 3, 'type': 'end'}, \
                 {'start_ndx': 15, 'stop_ndx': 21, 'line': 3, 'type': 'end'}, \
                 {'start_ndx': 0, 'stop_ndx': 5, 'line': 4, 'type': 'start'}, \
                 {'start_ndx': 0, 'stop_ndx': 5, 'line': 7, 'type': 'empty'}, \
                 {'start_ndx': 6, 'stop_ndx': 11, 'line': 7, 'type': 'empty'}, \
                 {'start_ndx': 0, 'stop_ndx': 3, 'line': 8, 'type': 'start'}, \
                 {'start_ndx': 53, 'stop_ndx': 57, 'line': 8, 'type': 'end'}, \
                 {'start_ndx': 0, 'stop_ndx': 50, 'line': 9, 'type': 'empty'}, \
                 {'start_ndx': 0, 'stop_ndx': 6, 'line': 10, 'type': 'end'}, \
                 {'start_ndx': 0, 'stop_ndx': 22, 'line': 11, 'type': 'end'}, \
                 {'start_ndx': 0, 'stop_ndx': 6, 'line': 12, 'type': 'end'}]
         self.assertEqual(find_tags(content), tags)
        
    def test_classify(self):
        self.assertEqual(classify('<head>'), 'start')
        self.assertEqual(classify('<basefont>'), 'empty')
        self.assertEqual(classify('</span>'), 'end')
        self.assertEqual(classify('<img src="gensler_and_zudans_family_dentistry.jpg">'), 'empty')
        self.assertEqual(classify('<isindex>'), 'empty')
    
    def test_same_line_tags(self):
        content = ['<html>\n', '<head>\n', \
                   '<title>Gensler &amp; Zudans Family Dentistry</title>\n', \
                   '<style></style></head>\n', '<body>\n', '\n', '\n', \
                   '<area><base>\n', \
                   '<h1>WELCOME TO GENSLER &amp; ZUDANS FAMILY DENTISTRY!</h1>\n', \
                   '<img src="gensler_and_zudans_family_dentistry.jpg">\n', \
                   '</body>\n', '</endtagwithnostarttag>\n', '</html>']
        tags = [{'start_ndx': 0, 'stop_ndx': 5, 'line': 0, 'type': 'start'}, \
                 {'start_ndx': 0, 'stop_ndx': 5, 'line': 1, 'type': 'start'}, \
                 {'start_ndx': 0, 'stop_ndx': 6, 'line': 2, 'type': 'start'}, \
                 {'start_ndx': 44, 'stop_ndx': 51, 'line': 2, 'type': 'end'}, \
                 {'start_ndx': 0, 'stop_ndx': 6, 'line': 3, 'type': 'start'}, \
                 {'start_ndx': 7, 'stop_ndx': 14, 'line': 3, 'type': 'end'}, \
                 {'start_ndx': 15, 'stop_ndx': 21, 'line': 3, 'type': 'end'}, \
                 {'start_ndx': 0, 'stop_ndx': 5, 'line': 4, 'type': 'start'}, \
                 {'start_ndx': 0, 'stop_ndx': 5, 'line': 7, 'type': 'empty'}, \
                 {'start_ndx': 6, 'stop_ndx': 11, 'line': 7, 'type': 'empty'}, \
                 {'start_ndx': 0, 'stop_ndx': 3, 'line': 8, 'type': 'start'}, \
                 {'start_ndx': 53, 'stop_ndx': 57, 'line': 8, 'type': 'end'}, \
                 {'start_ndx': 0, 'stop_ndx': 50, 'line': 9, 'type': 'empty'}, \
                 {'start_ndx': 0, 'stop_ndx': 6, 'line': 10, 'type': 'end'}, \
                 {'start_ndx': 0, 'stop_ndx': 22, 'line': 11, 'type': 'end'}, \
                 {'start_ndx': 0, 'stop_ndx': 6, 'line': 12, 'type': 'end'}]
        tags_after_same_line_tags = [{'start_ndx': 0, 'stop_ndx': 5, 'line': 0, 'type': 'start'}, \
                 {'start_ndx': 0, 'stop_ndx': 5, 'line': 1, 'type': 'start'}, \
                 {'start_ndx': 15, 'stop_ndx': 21, 'line': 3, 'type': 'end'}, \
                 {'start_ndx': 0, 'stop_ndx': 5, 'line': 4, 'type': 'start'}, \
                 {'start_ndx': 0, 'stop_ndx': 5, 'line': 7, 'type': 'empty'}, \
                 {'start_ndx': 6, 'stop_ndx': 11, 'line': 7, 'type': 'empty'}, \
                 {'start_ndx': 0, 'stop_ndx': 50, 'line': 9, 'type': 'empty'}, \
                 {'start_ndx': 0, 'stop_ndx': 6, 'line': 10, 'type': 'end'}, \
                 {'start_ndx': 0, 'stop_ndx': 22, 'line': 11, 'type': 'end'}, \
                 {'start_ndx': 0, 'stop_ndx': 6, 'line': 12, 'type': 'end'}]
        self.assertEqual(same_line_tags(tags, content), tags_after_same_line_tags)

    def test_tags_match(self):
        self.assertTrue(tags_match('<head>', '</head>'))
        self.assertFalse(tags_match('<h1>', '</h2>'))
        self.assertTrue(tags_match('<p>', '</p>'))
        self.assertFalse(tags_match('<head>', '<head>'))
        self.assertTrue(tags_match('<ul>', '</ul>'))
        self.assertFalse(tags_match('</head>', '<head>'))

    def test_find_end_tag(self):
        content = ['<html>\n', '<head>\n', \
                   '<title>Gensler &amp; Zudans Family Dentistry</title>\n', \
                   '<style></style></head>\n', '<body>\n', '\n', '\n', \
                   '<area><base>\n', \
                   '<h1>WELCOME TO GENSLER &amp; ZUDANS FAMILY DENTISTRY!</h1>\n', \
                   '<img src="gensler_and_zudans_family_dentistry.jpg">\n', \
                   '</body>\n', '</endtagwithnostarttag>\n', '</html>']
        tags = [{'start_ndx': 0, 'stop_ndx': 5, 'line': 0, 'type': 'start'}, \
                 {'start_ndx': 0, 'stop_ndx': 5, 'line': 1, 'type': 'start'}, \
                 {'start_ndx': 0, 'stop_ndx': 6, 'line': 2, 'type': 'start'}, \
                 {'start_ndx': 44, 'stop_ndx': 51, 'line': 2, 'type': 'end'}, \
                 {'start_ndx': 0, 'stop_ndx': 6, 'line': 3, 'type': 'start'}, \
                 {'start_ndx': 7, 'stop_ndx': 14, 'line': 3, 'type': 'end'}, \
                 {'start_ndx': 15, 'stop_ndx': 21, 'line': 3, 'type': 'end'}, \
                 {'start_ndx': 0, 'stop_ndx': 5, 'line': 4, 'type': 'start'}, \
                 {'start_ndx': 0, 'stop_ndx': 5, 'line': 7, 'type': 'empty'}, \
                 {'start_ndx': 6, 'stop_ndx': 11, 'line': 7, 'type': 'empty'}, \
                 {'start_ndx': 0, 'stop_ndx': 3, 'line': 8, 'type': 'start'}, \
                 {'start_ndx': 53, 'stop_ndx': 57, 'line': 8, 'type': 'end'}, \
                 {'start_ndx': 0, 'stop_ndx': 50, 'line': 9, 'type': 'empty'}, \
                 {'start_ndx': 0, 'stop_ndx': 6, 'line': 10, 'type': 'end'}, \
                 {'start_ndx': 0, 'stop_ndx': 22, 'line': 11, 'type': 'end'}, \
                 {'start_ndx': 0, 'stop_ndx': 6, 'line': 12, 'type': 'end'}]
        self.assertEqual(find_end_tag(tags, 0, content), 15)
        self.assertEqual(find_end_tag(tags, 2, content), 3)
        self.assertEqual(find_end_tag(tags, 1, content), 6)

    def test_how_many_indents(self):
        self.assertEqual(how_many_indents('\t\t\t\t<html><head>\t\t\n'), 4)
        self.assertEqual(how_many_indents('\t\t\n'), 2)
        self.assertEqual(how_many_indents('\t'), 1)
        self.assertEqual(how_many_indents('<html>\t\t<head>\t\t'), 0)
        self.assertEqual(how_many_indents('\t<html>\t\t<head>\t\t\n'), 1)

    def test_make_lower(self):
        content = ['      <htmL><heAd>\n', \
                   '<TITLE>Gensler &amp; Zudans Family Dentistry</title>\n', \
                   '<STYLE></style></head>\n', '  <body>\n', '\n', '\n', \
                   '<area><BASE>\n', \
                   'sdfdf<H1>WELCOME TO GENSLER &amp; ZUDANS FAMILY DENTISTRY!</H1>\n', \
                   '          <img src="gensler_and_zudans_family_dentistry.jpg">\n', \
                   '\n', '<helLO>\n', '\n', '    asfasf</HELLO>\n', '\n', '           \n', \
                   '       <p>Address:<br>\n', '1303 Mount Holly Rd.<BR>\n', \
                   '   Burlington, NJ 08016\n', \
                   '              <h2> whats up with cats???!?!?!!?\n', '\n', \
                   '                    </h2></P>\n', '\n', \
                   '<h3> sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg </h3>\n', '\n', \
                   '</BODY>  </endtagwithnostarttag>    </HTML>']
        content_after_make_lower = ['      <html><head>\n', \
                   '<title>Gensler &amp; Zudans Family Dentistry</title>\n', \
                   '<style></style></head>\n', '  <body>\n', '\n', '\n', \
                   '<area><base>\n', \
                   'sdfdf<h1>WELCOME TO GENSLER &amp; ZUDANS FAMILY DENTISTRY!</h1>\n', \
                   '          <img src="gensler_and_zudans_family_dentistry.jpg">\n', \
                   '\n', '<hello>\n', '\n', '    asfasf</hello>\n', '\n', '           \n', \
                   '       <p>Address:<br>\n', '1303 Mount Holly Rd.<br>\n', \
                   '   Burlington, NJ 08016\n', \
                   '              <h2> whats up with cats???!?!?!!?\n', '\n', \
                   '                    </h2></p>\n', '\n', \
                   '<h3> sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg </h3>\n', '\n', \
                   '</body>  </endtagwithnostarttag>    </html>']
        self.assertEqual(make_lower(content), content_after_make_lower)

        content = ['cats <HEAD> cats cats cats </hEAd>' \
                   '    <BR/> cat cat kitty cat </END>']
        content_after_make_lower = ['cats <head> cats cats cats </head>' \
                   '    <br/> cat cat kitty cat </end>']
        self.assertEqual(make_lower(content), content_after_make_lower)
        
    def test_delete_blank_lines(self):
        content = ['      <htmL><heAd>\n', \
                   '<TITLE>Gensler &amp; Zudans Family Dentistry</title>\n', \
                   '<STYLE></style></head>\n', '  <body>\n', '\n', '\n', \
                   '<area><BASE>\n', \
                   'sdfdf<H1>WELCOME TO GENSLER &amp; ZUDANS FAMILY DENTISTRY!</H1>\n', \
                   '          <img src="gensler_and_zudans_family_dentistry.jpg">\n', \
                   '\n', '<helLO>\n', '\n', '    asfasf</HELLO>\n', '\n', '           \n', \
                   '       <p>Address:<br>\n', '1303 Mount Holly Rd.<BR>\n', \
                   '   Burlington, NJ 08016\n', \
                   '              <h2> whats up with cats???!?!?!!?\n', '\n', \
                   '                    </h2></P>\n', '\n', \
                   '<h3> sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg </h3>\n', '\n', \
                   '</BODY>  </endtagwithnostarttag>    </HTML>']
        content_after_delete_blank_lines = ['      <htmL><heAd>\n', \
                   '<TITLE>Gensler &amp; Zudans Family Dentistry</title>\n', \
                   '<STYLE></style></head>\n', '  <body>\n', \
                   '<area><BASE>\n', \
                   'sdfdf<H1>WELCOME TO GENSLER &amp; ZUDANS FAMILY DENTISTRY!</H1>\n', \
                   '          <img src="gensler_and_zudans_family_dentistry.jpg">\n', \
                   '<helLO>\n', '    asfasf</HELLO>\n', \
                   '       <p>Address:<br>\n', '1303 Mount Holly Rd.<BR>\n', \
                   '   Burlington, NJ 08016\n', \
                   '              <h2> whats up with cats???!?!?!!?\n', \
                   '                    </h2></P>\n', \
                   '<h3> sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg </h3>\n', \
                   '</BODY>  </endtagwithnostarttag>    </HTML>']
        self.assertEqual(delete_blank_lines(content), content_after_delete_blank_lines)

        content = [' cats cats cats ', '\n', '     \n    ', '<h1>  \n', \
                   '    ', '     </h1>  \n', '     \n']
        content_after_delete_blank_lines =  [' cats cats cats ', '<h1>  \n', \
                   '    ', '     </h1>  \n']
        self.assertEqual(delete_blank_lines(content), content_after_delete_blank_lines)
        
    def test_add_blank_lines(self):
        content = ['      <htmL><heAd>\n', \
                   '<TITLE>Gensler &amp; Zudans Family Dentistry</title>\n', \
                   '<STYLE></style></head>\n', '  <body>\n', '\n', '\n', \
                   '<area><BASE>\n', \
                   'sdfdf<H1>WELCOME TO GENSLER &amp; ZUDANS FAMILY DENTISTRY!</H1>\n', \
                   '          <img src="gensler_and_zudans_family_dentistry.jpg">\n', \
                   '\n', '<helLO>\n', '\n', '    asfasf</HELLO>\n', '\n', '           \n', \
                   '       <p>Address:<br>\n', '1303 Mount Holly Rd.<BR>\n', \
                   '   Burlington, NJ 08016\n', \
                   '              <h2> whats up with cats???!?!?!!?\n', '\n', \
                   '                    </h2></P>\n', '\n', \
                   '<h3> sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg </h3>\n', '\n', \
                   '</BODY>  </endtagwithnostarttag>    </HTML>']

        content_after_add_blank_lines = ['      <htmL><heAd>\n', \
                   '<TITLE>Gensler &amp; Zudans Family Dentistry</title>\n', \
                   '<STYLE></style></head>\n', '\n', '  <body>\n', '\n', '\n', \
                   '<area><BASE>\n', \
                   'sdfdf<H1>WELCOME TO GENSLER &amp; ZUDANS FAMILY DENTISTRY!</H1>\n', \
                   '          <img src="gensler_and_zudans_family_dentistry.jpg">\n', \
                   '\n', '<helLO>\n', '\n', '    asfasf</HELLO>\n', '\n', '           \n', \
                   '       <p>Address:<br>\n', '1303 Mount Holly Rd.<BR>\n', \
                   '   Burlington, NJ 08016\n', '\n', \
                   '              <h2> whats up with cats???!?!?!!?\n', '\n', \
                   '                    </h2></P>\n', '\n', '\n', \
                   '<h3> sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg ' \
                   'sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg sdgsdgdsgdsg </h3>\n', '\n', \
                   '</BODY>  </endtagwithnostarttag>    </HTML>']
        self.assertEqual(add_blank_lines(content), content_after_add_blank_lines)

        content = ['<head> cats are so cute</head>', '<body>', '<h1>cats cats cats</h1></body>']
        content_after_add_blank_lines = ['\n', '<head> cats are so cute</head>', \
                                         '\n', '<body>', '\n', '<h1>cats cats cats</h1></body>']
        self.assertEqual(add_blank_lines(content), content_after_add_blank_lines)

    def test_line_length(self):
        content = ['<head>\n', \
                   'sdgsgdsgsdgdsgdsggs sdgsdgdgsdgdsgsdgdssdgsdgsdg sdfsd sdfsdf ' \
                   'sddgsdgdsgsdgsdgsdgsdgsdg sdgsdgsdgsdgsdgsdg\n', \
                   'sdgsdgdsgdsgdsg sdgsdgsdgdsgdsgdsgsdgsdgdsgsdgdsgsdgdsgsdg ' \
                   'sasgsdgdgsdgsdgsdgsdgsdgsdgsdgsdgsdsdg\n', \
                   'sddgsdgsdgsdgsdgdsgdsgsdgsdgsdgdsgsdgsdgdsgsdgsdgsdgsdgsdg ' \
                   'sdfsdgdsgdsgsdgsgdsgdsgdsgdsdsgdsgsdgsdgsdgsdgdsgsdgsd\n']
        content_after_line_length = ['<head>\n', \
                   'sdgsgdsgsdgdsgdsggs sdgsdgdgsdgdsgsdgdssdgsdgsdg sdfsd sdfsdf\n', \
                   'sddgsdgdsgsdgsdgsdgsdgsdg sdgsdgsdgsdgsdgsdg\n', \
                   'sdgsdgdsgdsgdsg sdgsdgsdgdsgdsgdsgsdgsdgdsgsdgdsgsdgdsgsdg\n', \
                   'sasgsdgdgsdgsdgsdgsdgsdgsdgsdgsdgsdsdg\n', \
                   'sddgsdgsdgsdgsdgdsgdsgsdgsdgsdgdsgsdgsdgdsgsdgsdgsdgsdgsdg\n', \
                   'sdfsdgdsgdsgsdgsgdsgdsgdsgdsdsgdsgsdgsdgsdgsdgdsgsdgsd\n']
        self.assertEqual(line_length(content), content_after_line_length)

    def test_find_first_space_before_80(self):
        line = '<head> catscatscatscatscatscatscatscats</head>'
        line = line * 2
        self.assertEqual(find_first_space_before_80(line), 52)
        line = line * 2
        self.assertEqual(find_first_space_before_80(line), 52)
        line = '<head>catscatscatscatscatscatscatscats</head>'
        line = line * 2
        self.assertEqual(find_first_space_before_80(line), -1)

    '''was unable to finish the following unit tests in time:

    def test_indent_lines(self):

    def test_indent_all_tags(self):

    def test_start_tag_exists(self):
        
    def test_fix_nesting(self):

    def test_delete_xtra_end_tags(self):'''

unittest.main()
