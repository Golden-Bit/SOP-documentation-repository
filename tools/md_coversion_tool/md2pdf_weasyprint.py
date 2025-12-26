from markdown_it import MarkdownIt
from weasyprint import HTML, CSS

def md_to_pdf_weasyprint(md_text: str, pdf_path: str, css_text: str | None = None) -> None:
    html = MarkdownIt("commonmark").render(md_text)

    if css_text:
        HTML(string=html).write_pdf(pdf_path, stylesheets=[CSS(string=css_text)])
    else:
        HTML(string=html).write_pdf(pdf_path)

css = """
@page { margin: 2.5cm; }
body { font-family: sans-serif; line-height: 1.4; }
"""

with open("C:\\Users\\info\\Desktop\\work_space\\repositories\\SOP-documentation-repository\\sop_docs\\SOP-DOC\\SOP-DOC-03_attachments\\Allegato_SOP-DOC-03-A00_INBOX.md", "r", encoding="utf-8") as f:
    md_to_pdf_weasyprint(f.read(), "C:\\Users\\info\\Desktop\\work_space\\repositories\\SOP-documentation-repository\\sop_docs\\SOP-DOC\\SOP-DOC-03_attachments\\Allegato_SOP-DOC-03-A00_INBOX.pdf", css_text=css)
