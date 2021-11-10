from pprint import pprint
from xml.dom import minidom
import dealing_json


def get_all_news_from_xml(file):
    """Parse an xml file and return data in description tag into
    a list of words

    Args:
        file: An xml file or path to the file

    Returns: A list of words

    """
    my_doc = minidom.parse(file)
    items = my_doc.getElementsByTagName('description')

    box = []
    for item in items:
        box.extend(item.firstChild.data.split())
    return box


if __name__ == '__main__':
    words = get_all_news_from_xml('newsafr.xml')
    most_common = dealing_json.n_most_common_words_length_greater_m(words, 10, 6)

    pprint(most_common)
