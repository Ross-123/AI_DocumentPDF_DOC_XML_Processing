
# https://www.youtube.com/watch?v=B5XD-qpL0FU&t=287s
import base64 
import textwrap
from io import BytesIO
from pathlib import Path
import numpy as np
from docling.backend.pypdfium2_backend import PyPdfiumDocumentBackend
from docling.datamodel.base_models import InputFormat
from docling.datamodel.options.picture_description_options import PictureDescriptionOptions
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.pipeline.simple_pipeline import SimplePipeline
from docling.pipeline.standard_pdf_pipeline import StandardPdfPipeline
from docling.document_converter import DocumentConverter, PdfFormatOption, WordFormatOption
from dotenv import load_dotenv
from IPython.display import HTML, display
from ollama import chat
from PIL import Image
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics. pairwise import cosine_similarity

load_dotenv()

# Convert PDF to Markdown

granite_picture_description = PictureDescriptionOptions(
    provider="ollama",
    model="llava:latest",  # NOTE: Using 'llava' as an example. Replace with your granite model if available in Ollama.
    prompt="Describe the picture in detail.",
)


pipeline_options = PdfPipelineOptions(
    generate_page_images=True,
    images_scale=1.00,
    do_ocr=True,
    do_picture_description=True,
    picture_description_options=granite_picture_description,
    do_table_structure=True,
    do_text_extraction=True,
    do_cell_matching=True,
    do_text_matching=True,
    do_text_matching_with_ocr=True,
    do_text_matching_with_ocr_and_table_structure=True,
)

converter = DocumentConverter(
    format_options={InputFormat. PDF: PdfFormatOption(pipeline_options=pipeline_options)}
)

document_path = Path(r"C:\Users\Roshan\Desktop\Data_visualization\AI_Build_Apps\AI_DocumentPDF_DOC_XML_Processing_RAG_Docling_OCR_Chunking_Images\NVIDIAAn.pdf")
document_path

result = converter.convert(document_path)
