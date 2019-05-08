
# -*- coding: utf-8 -*-

from xml.dom.minidom import Document
# 将self.sizeDict中的信息写入本地xml文件，参数filename是xml文件名
def writeInfoToXml(xml_path,c_filename,c_path,c_xmin,c_ymin,c_xmax,c_ymax,c_width,c_height,c_depth):
        # 创建dom文档
        doc = Document()

        # 创建根节点
        annotation = doc.createElement('annotation')
        # 根节点插入dom树
        doc.appendChild(annotation)

        # 依次将sizeDict中的每一组元素提取出来，创建对应节点并插入dom树

        folder = doc.createElement('folder')
        folder_text = doc.createTextNode("train_imgs")
        folder.appendChild(folder_text)
        annotation.appendChild(folder)
        
        filename = doc.createElement('filename')
        filename_text = doc.createTextNode(c_filename+'.jpg')
        filename.appendChild(filename_text)
        annotation.appendChild(filename)

        path = doc.createElement('path')
        path_text = doc.createTextNode(c_path)
        path.appendChild(path_text)
        annotation.appendChild(path)


        # 每一组信息先创建节点<source>，然后插入到父节点<annotation>下
        source = doc.createElement('source')
        annotation.appendChild(source)

        # 将姓名插入<size>中
        # 创建节点<width>
        database = doc.createElement('database')
        # 创建<width>下的文本节点
        database_text = doc.createTextNode("Unknown")
        # 将文本节点插入到<width>下
        database.appendChild(database_text)
        # 将<width>插入到父节点<size>下
        source.appendChild(database)



        # 每一组信息先创建节点<size>，然后插入到父节点<annotation>下
        size = doc.createElement('size')
        annotation.appendChild(size)





        # 将姓名插入<size>中
        # 创建节点<width>
        width = doc.createElement('width')
        # 创建<width>下的文本节点
        width_text = doc.createTextNode(c_width)
        # 将文本节点插入到<width>下
        width.appendChild(width_text)
        # 将<width>插入到父节点<size>下
        size.appendChild(width)

        # 将电话插入<size>中，处理同上
        height = doc.createElement('height')
        height_text = doc.createTextNode(c_height)
        height.appendChild(height_text)
        size.appendChild(height)

        # 将地址插入<size>中，处理同上
        depth = doc.createElement('depth')
        depth_text = doc.createTextNode(c_depth)
        depth.appendChild(depth_text)
        size.appendChild(depth)

        segmented = doc.createElement('segmented')
        segmented_text = doc.createTextNode("0")
        segmented.appendChild(segmented_text)
        annotation.appendChild(segmented)


        object = doc.createElement('object')
        annotation.appendChild(object)


        name = doc.createElement('name')
        name_text = doc.createTextNode("4")
        name.appendChild(name_text)
        object.appendChild(name)

        pose = doc.createElement('pose')
        pose_text = doc.createTextNode("Unspecified")
        pose.appendChild(pose_text)
        object.appendChild(pose)

        truncated = doc.createElement('truncated_text')
        truncated_text = doc.createTextNode("0")
        truncated.appendChild(truncated_text)
        object.appendChild(truncated)

        difficult = doc.createElement('difficult')
        difficult_text = doc.createTextNode("0")
        difficult.appendChild(difficult_text)
        object.appendChild(difficult)

        bndbox = doc.createElement('bndbox')
        object.appendChild(bndbox)

        xmin = doc.createElement('xmin')
        xmin_text = doc.createTextNode(c_xmin)
        xmin.appendChild(xmin_text)
        bndbox.appendChild(xmin)

        ymin = doc.createElement('ymin')
        ymin_text = doc.createTextNode(c_ymin)
        ymin.appendChild(ymin_text)
        bndbox.appendChild(ymin)

        xmax = doc.createElement('xmax')
        xmax_text = doc.createTextNode(c_xmax)
        xmax.appendChild(xmax_text)
        bndbox.appendChild(xmax)

        ymax = doc.createElement('ymax')
        ymax_text = doc.createTextNode(c_ymax)
        ymax.appendChild(ymax_text)
        bndbox.appendChild(ymax)

        allinfo=xml_path+c_filename+'.xml'

        # 将dom对象写入本地xml文件
        with open(allinfo, 'wb+') as f:
            f.write(doc.toprettyxml(indent='\t', encoding='utf-8'))
        return


# <?xml version="1.0" encoding="utf-8"?>
# <annotation>
# 	<size>
# 		<width>000</width>
# 		<height>111</height>
# 		<depth>222</depth>
# 		<count>4444</count>
# 	</size>
# </annotation>
