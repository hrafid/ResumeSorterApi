
import torch

'''


# this function extractss text data from pdf
def extract_text(pdf_source):
    text = ''
    file = BytesIO(requests.get(pdf_source).content) if not is_local_file else open(pdf_source, 'rb')
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        text += page.extract_text()
    return text
'''
'''

def extract_text(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
        return text
    
'''
def extract_text(pdf_bytes):
    from io import BytesIO
    import PyPDF2

    text = ''
    try:
        # Use BytesIO to treat binary data as a file object
        with BytesIO(pdf_bytes) as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
        if not text.strip():
            raise ValueError("No text could be extracted from the PDF.")
        return text
    except Exception as e:
        raise RuntimeError(f"Failed to extract text from the PDF: {e}")

### function for classifying resume category
def categorize_resume(resume_text,model,tokenizer,device,reverse_label_map):
    #inputs = tokenizer(resume_text, padding='max_length', truncation=True,return_tensors='pt')# appplying tokenizer to text
    #inputs = tokenizer(resume_text, return_tensors='pt', truncation=True, padding=True)
    inputs = tokenizer(resume_text, return_tensors='pt', truncation=True, padding='max_length')
    inputs = {key: value.to(device) for key, value in inputs.items()}
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_label = torch.argmax(logits, dim=1).item()# model prediction on resume data
    category = reverse_label_map[predicted_label] # translating prediction into category 
    return category



# function for processing resumes

def process_resumes(pdfFile,model,tokenizer,device,reverse_label_map):

    
    resume_text = extract_text(pdfFile)# extracting resume text 
    category = categorize_resume(resume_text,model,tokenizer,device,reverse_label_map)# classifying resume
    return category

