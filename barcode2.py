import xml.etree.ElementTree as ET
import barcode # type: ignore
from barcode.writer import ImageWriter # type: ignore

# 1. Parse XML
tree = ET.parse('data.xml')
root = tree.getroot()
# say your XML looks like <order><id>12345</id></order>
order_id = root.findtext('id')

# 2. Generate barcode
EAN = barcode.get_barcode_class('code128')
ean = EAN(order_id, writer=ImageWriter())

# 3. Save as PNG
filename = ean.save('order_12345')
print(f'Barcode saved to {filename}.png')
