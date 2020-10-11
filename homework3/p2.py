import os
import xml.etree.ElementTree as elementTree
import json


def read_xml_file():
    xml_file = os.path.abspath(os.path.join('./data', 'menu.xml'))
    return elementTree.ElementTree(file=xml_file)


def convert_xml_2_json(xml):
    def convert_sub(xml_element):
        if len(xml_element) < 0:
            return None
        xml_element_dict = dict()
        for sub_xml_element in xml_element:
            if sub_xml_element.tag not in xml_element_dict:
                xml_element_dict[sub_xml_element.tag] = dict()
            values = [value for (key, value) in sub_xml_element.attrib.items()]
            xml_element_dict[sub_xml_element.tag][sub_xml_element.text] = ''.join(values)
            convert_inner = convert_sub(sub_xml_element)
            if convert_inner is not None and len(convert_inner) > 0:
                xml_element_dict.update(convert_inner)
        return xml_element_dict
    root_dict = dict()
    xml_root = xml.getroot()
    for child in xml_root:
        root_dict[child.tag] = child.attrib
        convert_child = convert_sub(child)
        if convert_child is not None and len(convert_child) > 0:
            root_dict[child.tag].update(convert_child)
    return json.dumps(root_dict)


def write_json_file(content):
    new_file = open('./data/menu.json', 'w')
    for line in content:
        new_file.write(line)
    new_file.close()


xml_content = read_xml_file()
print('xml content:', xml_content)

json_content = convert_xml_2_json(xml_content)
print('json content:', json_content)

write_json_file(json_content)
