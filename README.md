# xor_encryption
Xor шифрование на python

Утилита для поблочного преобразования файлов с помощью xor.
Исходный файл делится на блоки. Каждый блок обрабатывается независимо от остальных в своем потоке.

#### Установка проекта на Ubuntu
```
git clone https://github.com/FedorovVladimir/xor_encryption
cd xor_encryption
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py --help
```

#### Установка проекта на Windows
```
git clone https://github.com/FedorovVladimir/xor_encryption
cd xor_encryption
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python main.py --help 
```
