#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: xml_text
    @Auther: changchun_wu
    @Date: 2019/4/26 17:34
    @Version: 1.0 
"""

import xml.etree.ElementTree as ET

if __name__ == '__main__':
    # 解析xml
    # tree = ET.parse("./file/rank_country.xml")
    # 获取xml的根节点信息
    # root = tree.getroot()
    # for item in root:
        # 获取节点下的标签信息
        # print(item,item.tag)
        # 获取节点下的属性信息
        # print(item.attrib)
        # for i in item:
            # print(i.tag)
            # print(i.attrib)
            # 获取节点下的文本信息
            # print(i.text)

    # 遍历某个节点
    # for item in root.iter("year"):
    #     print(item.tag,item.attrib,item.text)

    # 修改year节点的数据
    # tree = ET.parse("./file/rank_country.xml")
    # root = tree.getroot()
    # for node in root.iter("year"):
    #     new_year = int(node.text)+100
    #     node.text = new_year.__str__()
    #     node.set("updated","yes")
    # tree.write("./file/rank_country.xml")

    # 删除gdp排名大于50的国家的信息
    tree = ET.parse("./file/rank_country.xml")
    root = tree.getroot()

    for country in root.findall("country"):
        rank = int(country.find("rank").text)
        if rank > 50:
            root.remove(country)
    tree.write("./file/rank_country.xml")

    # 创建xml文件
    # <namelist></namelist>
    root_element = ET.Element("namelist")
    # <name arrtib="{'enrolled': 'yse'}"></name>
    name = ET.SubElement(root_element, "name",attrib={"enrolled":"yes"})
    name_alex = ET.SubElement(name, "alex")
    age = ET.SubElement(name_alex, "age")
    age.text = "18"
    address = ET.SubElement(name_alex, "address")
    address.text = "ShangHai"

    element_tree = ET.ElementTree(root_element)
    element_tree.write("new_xml.xml",encoding="utf-8",xml_declaration=True)
