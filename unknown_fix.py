import sys  
import xml.etree.ElementTree as ET  
  
def process_xml(file_path):  
    tree = ET.parse(file_path)  
    root = tree.getroot()  
   
    for artist_name in root.findall('.//artist_name[@__type="str"]'):  
        if artist_name.text is None or artist_name.text.strip() == '':  
            artist_name.text = 'unknown'  
  
    new_file_path = file_path.rsplit('.', 1)[0] + '_unknown_fix.xml'  
    tree.write(new_file_path, encoding='utf-8', xml_declaration=True)  
  
if __name__ == "__main__":  
    if len(sys.argv) > 1:  
        process_xml(sys.argv[1])  