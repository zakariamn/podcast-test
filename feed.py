import yaml
import xml.etree.ElementTree as xml_tree

# Open and read the YAML file
with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

# Create the root RSS element with attributes
rss_element = xml_tree.Element('rss', {
    'version': '2.0',
    'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'
    # Add other attributes as needed
})

# Create the channel element inside rss
channel_element = xml_tree.SubElement(rss_element, 'channel')

# Add title element inside channel with text from YAML
title_element = xml_tree.SubElement(channel_element, 'title')
title_element.text = yaml_data['title']

# Create the XML tree and write to podcast.xml
output_tree = xml_tree.ElementTree(rss_element)
output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)