import torch
from preprocess.preprocess import load_dataset, compute_label_agg, select_data, get_data_loaders
# from models.transformer import MVMNet_Transformer
from models.transformer2 import Transformer
from utils.trainer import trainer
from torchinfo import summary

# Use GPU if available, else use CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

# path = './data/ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.3/'
batch_size = 256
# print("Start loading")    
# data, raw_labels = load_dataset(path)
# print("done loading")    
# labels = compute_label_agg(raw_labels, path)

# data, labels, Y = select_data(data, labels)

# train_loader, valid_loader, test_loader = get_data_loaders(data, labels, Y, batch_size)

model = Transformer(d_model=120, vocab_size=250, num_layers=6, heads=12).to(device)
print(model)
summary(model, input_size=(256, 12, 250))

# lr = 0.007

# train_accs, valid_accs, test_acc = trainer(model, train_loader, test_loader, valid_loader, lr = lr)

# torch.save(model.state_dict(), f'./ckpt/CNN_lr_{lr}_test_acc_{test_acc:.4f}.pt')