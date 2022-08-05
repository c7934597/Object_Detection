    # coding:utf-8
from PIL import Image
from xml.dom.minidom import Document
import os
 
 
def main():
    imgpath = 'datasets/coco-text/formatted_dataset/JPEGImages/'
    txtpath = 'datasets/coco-text/formatted_dataset/images.annotations'
    xmlpath_new = 'datasets/coco-text/formatted_dataset/Annotations/'
    coco = {}
 
    # 　得到图像的标注信息
    file_object = open(txtpath, 'rU')
    try:
        for line in file_object:
            line = line.rstrip('\n')
            strs = line.split(' ')
            print (strs[0])
            foldername = 'voc'
 
            # 　用xml替换jpg，得到同名文件
            xmlname = strs[0].replace('.jpg', '.xml')
            info = Image.open(imgpath + strs[0])
            # read image size
            (width, height) = info.size
            strs[2] = max(int(strs[2]), 1)
            strs[3] = max(int(strs[3]), 1)
            strs[4] = min(int(strs[4]), width);
            strs[5] = min(int(strs[5]), height);
 
            # 过滤异常
            if strs[2] >= strs[4] or strs[3] >= strs[5] or strs[2] <= 0 or strs[3] <= 0 or strs[4] > width or strs[
                5] > height:
                continue
 
            if os.path.exists(imgpath + strs[0]):
                if xmlname in coco:
                    Createnode = coco[xmlname]
                    object_node = Createnode.createElement('object')
 
                    Root = Createnode.getElementsByTagName('annotation')[0]
                    Root.appendChild(object_node)
 
                    node = Createnode.createElement('name')
                    node.appendChild(Createnode.createTextNode(strs[1]))
                    object_node.appendChild(node)
 
                    node = Createnode.createElement('pose')
                    node.appendChild(Createnode.createTextNode('Unspecified'))
                    object_node.appendChild(node)
 
                    node = Createnode.createElement('truncated')
                    node.appendChild(Createnode.createTextNode('0'))
                    object_node.appendChild(node)
 
                    node = Createnode.createElement('difficult')
                    node.appendChild(Createnode.createTextNode('0'))
                    object_node.appendChild(node)
 
                    bndbox_node = Createnode.createElement('bndbox')
                    object_node.appendChild(bndbox_node)
 
                    node = Createnode.createElement('xmin')
                    node.appendChild(Createnode.createTextNode(str(strs[2])))
                    bndbox_node.appendChild(node)
 
                    node = Createnode.createElement('ymin')
                    node.appendChild(Createnode.createTextNode(str(strs[3])))
                    bndbox_node.appendChild(node)
 
                    node = Createnode.createElement('xmax')
                    node.appendChild(Createnode.createTextNode(str(strs[4])))
                    bndbox_node.appendChild(node)
 
                    node = Createnode.createElement('ymax')
                    node.appendChild(Createnode.createTextNode(str(strs[5])))
                    bndbox_node.appendChild(node)
                else:
                    Createnode = Document()  # 创建DOM文档对象
 
                    Root = Createnode.createElement('annotation')  # 创建根元素
                    Createnode.appendChild(Root)
 
                    # folder
                    folder = Createnode.createElement('folder')
                    folder.appendChild(Createnode.createTextNode(foldername))
                    Root.appendChild(folder)
 
                    # filename
                    filename = Createnode.createElement('filename')
                    filename.appendChild(Createnode.createTextNode(strs[0]))
                    Root.appendChild(filename)
 
                    # source
                    source_node = Createnode.createElement('source')
                    Root.appendChild(source_node)
 
                    node = Createnode.createElement('database')
                    node.appendChild(Createnode.createTextNode('MS COCO-Text'))
                    source_node.appendChild(node)
 
                    node = Createnode.createElement('annotation')
                    node.appendChild(Createnode.createTextNode('MS COCO-Text 2014'))
                    source_node.appendChild(node)
 
                    node = Createnode.createElement('image')
                    node.appendChild(Createnode.createTextNode('NULL'))
                    source_node.appendChild(node)
 
                    node = Createnode.createElement('flickrid');
                    node.appendChild(Createnode.createTextNode('NULL'));
                    source_node.appendChild(node);
 
                    # owner
                    owner_node = Createnode.createElement('owner')
                    Root.appendChild(owner_node)
 
                    node = Createnode.createElement('flickrid')
                    node.appendChild(Createnode.createTextNode('NULL'))
                    owner_node.appendChild(node)
 
                    node = Createnode.createElement('name')
                    node.appendChild(Createnode.createTextNode('ligen'))
                    owner_node.appendChild(node)
 
                    # size
                    size_node = Createnode.createElement('size')
                    Root.appendChild(size_node)
 
                    node = Createnode.createElement('width')
                    node.appendChild(Createnode.createTextNode(str(width)))
                    size_node.appendChild(node)
 
                    node = Createnode.createElement('height');
                    node.appendChild(Createnode.createTextNode(str(height)))
                    size_node.appendChild(node)
 
                    node = Createnode.createElement('depth')
                    node.appendChild(Createnode.createTextNode('3'))
                    size_node.appendChild(node)
 
                    # segmented
                    node = Createnode.createElement('segmented')
                    node.appendChild(Createnode.createTextNode('0'))
                    Root.appendChild(node)
 
                    # object
                    object_node = Createnode.createElement('object')
                    Root.appendChild(object_node)
 
                    node = Createnode.createElement('name')
                    node.appendChild(Createnode.createTextNode(strs[1]))
                    object_node.appendChild(node)
 
                    node = Createnode.createElement('pose')
                    node.appendChild(Createnode.createTextNode('Unspecified'))
                    object_node.appendChild(node)
 
                    node = Createnode.createElement('truncated')
                    node.appendChild(Createnode.createTextNode('0'))
                    object_node.appendChild(node)
 
                    node = Createnode.createElement('difficult')
                    node.appendChild(Createnode.createTextNode('0'))
                    object_node.appendChild(node)
 
                    bndbox_node = Createnode.createElement('bndbox')
                    object_node.appendChild(bndbox_node)
 
                    node = Createnode.createElement('xmin')
                    node.appendChild(Createnode.createTextNode(str(strs[2])))
                    bndbox_node.appendChild(node)
 
                    node = Createnode.createElement('ymin')
                    node.appendChild(Createnode.createTextNode(str(strs[3])))
                    bndbox_node.appendChild(node)
 
                    node = Createnode.createElement('xmax')
                    node.appendChild(Createnode.createTextNode(str(strs[4])))
                    bndbox_node.appendChild(node)
 
                    node = Createnode.createElement('ymax')
                    node.appendChild(Createnode.createTextNode(str(strs[5])))
                    bndbox_node.appendChild(node)
 
                    coco[xmlname] = Createnode
 
    finally:
        file_object.close()
    print ('begin load xml...')
    for key in coco:
        print (key)
        f = open(xmlpath_new + key, 'w')
        f.write(coco[key].toprettyxml(indent='\t'))
        f.close()
 
 
if __name__ == "__main__":
    main()