from docling.document_converter import DocumentConverter


def extract_text_from_pdf(pdf_path: str):
    converter = DocumentConverter()

    result = converter.convert(pdf_path)

    document = result.document

    print(type(document))
    print(dir(document))

    return document