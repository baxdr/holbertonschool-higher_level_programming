#!/usr/bin/python3
"""Serialization and deserialization using XML format."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The data to serialize (key: tag name, value: text).
        filename (str): Path to the output XML file.
    """
    # Create root element
    root = ET.Element('data')
    # Add child elements for each key-value pair
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    # Write XML tree to file with declaration
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file back into a Python dictionary.

    Args:
        filename (str): Path to the input XML file.

    Returns:
        dict: The deserialized data (all values as strings).
    """
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()
    # Build and return the dictionary from child elements
    result = {}
    for child in root:
        result[child.tag] = child.text
    return result
