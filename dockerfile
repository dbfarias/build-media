# Usa Python 3.11 como base
FROM python:3.11

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instala dependências do sistema necessárias para OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    ffmpeg

# Atualiza pip antes de instalar dependências
RUN pip install --upgrade pip setuptools

# Copia o arquivo de dependências primeiro para garantir cache eficiente
COPY requirements.txt .

# Instala todas as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos do projeto
COPY . .

# Comando padrão do contêiner
CMD ["python", "src/main.py"]