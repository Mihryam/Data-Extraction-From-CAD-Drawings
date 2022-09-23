pop_path='C:\\Users\Mnesoma\\Desktop\MORNINR\\poppler-22.04.0\\Library\\bin'
pdff_path = 'C:\\Users\Mnesoma\\Desktop\\MORNINR\\TestInputFile.pdf'

from pdf2image import convert_from_path
pages = convert_from_path(pdf_path = pdff_path,poppler_path=pop_path)

import os
saving_folder = 'C:\\Users\\Mnesoma\\Desktop\MORNINR'

c = 1
for page in pages:
    img_name = f'img-{c}.bmp'
    page.save(os.path.join(saving_folder, img_name), 'bmp')
    c += 1
