import xml.etree.ElementTree as ET  
  
def extract_music_info(xml_file_path):  
    tree = ET.parse(xml_file_path)  
    root = tree.getroot()  
    all_info = []  
    for music_elem in root.findall('.//music'):  
        music_id = music_elem.get('id')  
        if music_id:  
            info_elem = music_elem.find('info')  
            if info_elem:  
                title_name = info_elem.find('title_name').text if info_elem.find('title_name') is not None else ''  
                artist_name = info_elem.find('artist_name').text if info_elem.find('artist_name') is not None else ''  
                bpm_max_str = info_elem.find('bpm_max').text if info_elem.find('bpm_max') is not None else '' 
            info_df = music_elem.find('difficulty')  
            info_df222 = info_df.find('fumen_1b')  
            if  info_df222:  
                fumen_1b = info_df222.find('difnum').text if info_df222.find('difnum') is not None else '' 
            info_df333 = info_df.find('fumen_1a')  
            if  info_df333:  
                fumen_1a = info_df333.find('difnum').text if info_df333.find('difnum') is not None else '' 
            all_info.append([music_id, title_name, artist_name, bpm_max_str, fumen_1b, fumen_1a])
    return all_info  

def write_all_info(all_info, output_file_path):  
    with open(output_file_path, 'w', encoding='utf-8') as file:  
        for info in all_info:  
            for item in info:  
                file.write(item + '\n')  
            file.write('\n')
  
def main():  
    import sys  
    if len(sys.argv) != 2:  
        print("Use python .py .xml")  
        sys.exit(1)  
  
    xml_file_path = sys.argv[1]  
    all_info = extract_music_info(xml_file_path)  
  
    output_file_path = 'SongMenuDRS2020.txt'  
    write_all_info(all_info, output_file_path)  
  
if __name__ == "__main__":  
    main()