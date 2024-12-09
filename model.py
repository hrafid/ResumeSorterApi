
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

def load_model():
    label_map = {
        'AGRICULTURE': 0, 'SALES': 1, 'ACCOUNTANT': 2, 'AVIATION': 3, 'BANKING': 4, 'CONSULTANT': 5, 'FINANCE': 6, 'PUBLIC-RELATIONS': 7, 
        'BUSINESS-DEVELOPMENT': 8, 'CHEF': 9, 'AUTOMOBILE': 10, 'INFORMATION-TECHNOLOGY': 11, 'DIGITAL-MEDIA': 12, 'ENGINEERING': 13, 
        'ARTS': 14, 'HR': 15, 'APPAREL': 16, 'HEALTHCARE': 17, 'FITNESS': 18, 'CONSTRUCTION': 19, 'TEACHER': 20, 'ADVOCATE': 21, 'BPO': 22, 'DESIGNER': 23
    }
    reverse_label_map = {v: k for k, v in label_map.items()}

    # 
    ### initializing and loading model from saved .pt file
    #device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    device = torch.device("cpu")
    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=24)
    model.to(device) 

    ### load model weights from file
    model.load_state_dict(torch.load('state_dict_model.pt', weights_only=True, map_location=device))
    model.eval()

    return model,tokenizer,device,reverse_label_map

