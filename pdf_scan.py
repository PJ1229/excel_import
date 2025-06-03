from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar

# Path to your PDF file
pdf_path = r"C:\Users\10817992\Downloads\CSTR3T-70000-A_DRC503_Final_DCV_v5_20240809_8052312_8067208.pdf"

for page_num, page_layout in enumerate(extract_pages(pdf_path), start=1):
    print(f"\n--- Page {page_num} ---")

    for element in page_layout:
        if isinstance(element, LTTextContainer):
            for text_line in element:
                word = ""
                x0 = y0 = x1 = y1 = None

                for char in text_line:
                    if isinstance(char, LTChar):
                        # Start new word
                        if word == "":
                            x0, y0 = char.bbox[0], char.bbox[1]
                        word += char.get_text()
                        x1, y1 = char.bbox[2], char.bbox[3]

                    elif char.get_text().isspace() and word:
                        print(f"Word: '{word.strip()}' Page: {page_num} Box: ({x0:.1f}, {y0:.1f}, {x1:.1f}, {y1:.1f})")
                        word = ""
                        x0 = y0 = x1 = y1 = None

                # Print last word in line if any
                if word:
                    print(f"Word: '{word.strip()}' Page: {page_num} Box: ({x0:.1f}, {y0:.1f}, {x1:.1f}, {y1:.1f})")
