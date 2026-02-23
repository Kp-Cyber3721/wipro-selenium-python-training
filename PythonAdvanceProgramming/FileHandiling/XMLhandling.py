import xml.etree.ElementTree as ET
#read xml file

#parsed XML file into a variable tree
tree = ET.parse("C://Users//priya//PycharmProjects//PythonAdvanceProgramming//Dataformats//employee.xml")
root = tree.getroot() #get the root element
print(root.tag)
#get the first child node / tag
print(root[0].tag)
print(root[1].tag)

#get the attribute of the child node/tag
print(root[0].attrib)
print(root[1].attrib)

#fetch all the attribute in the child node
for employee in root.findall("employee"):
     emp_id=employee.get("id")
     print(emp_id)
     emp_name=employee.find("name").text
     print(emp_name)

for emp in root.findall("employee"):
    name = emp.find("name").text
    role = emp.find("role").text
    exp  = emp.find("experience").text
    print(name, role,exp)

#flow root- child nodes-----> attributes of the child nodes -----> text of the attributes

#write the data to xml file
#create the child node

#create the root element
root = ET.Element("employees")

#create the child elements
emp1 = ET.SubElement(root, "employee", id = "101")
ET.SubElement(emp1, "name").text = "Harsha"
ET.SubElement(emp1, "role").text = "Tester"
ET.SubElement(emp1, "experience").text = "5"

#create the child node 2
emp1 = ET.SubElement(root, "employee", id = "102")
ET.SubElement(emp1, "name").text = "Amit"
ET.SubElement(emp1, "role").text = "Developer"
ET.SubElement(emp1, "experience").text = "3"


#write to the file
tree= ET.ElementTree(root)
tree.write("C://Users//priya//PycharmProjects//PythonAdvanceProgramming//Dataformats//write.xml", encoding ="utf-8",xml_declaration=True)

#updating the xml
tree = ET.parse("C://Users//priya//PycharmProjects//PythonAdvanceProgramming//Dataformats//update.xml")
root = tree.getroot()
for emp in root.findall("employee"):
    if emp.get("id") == "101":
        emp.find("experience").text="16"

#convert to string
ET.indent(tree, space="    ",level=0)


tree.write("C://Users//priya//PycharmProjects//PythonAdvanceProgramming//Dataformats//update.xml",encoding ="utf-8",xml_declaration=True)



