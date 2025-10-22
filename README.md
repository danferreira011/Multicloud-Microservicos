# 🌡️ Conversor de Temperatura Multicloud Serverless

Este projeto é uma aplicação web simples que demonstra o uso de uma arquitetura de microserviços serverless, distribuída entre os três maiores provedores de nuvem: **AWS**, **Azure** e **GCP**. O objetivo principal é ilustrar a interoperabilidade entre diferentes plataformas e linguagens de programação em um cenário prático.

A aplicação consiste em um conversor de temperaturas com um frontend em HTML/CSS/JavaScript que consome três APIs distintas, cada uma hospedada em um provedor de nuvem diferente.


## ✨ Funcionalidades

- **Converter Celsius para Fahrenheit**: Utiliza um microserviço na **AWS**.
- **Converter Celsius para Kelvin**: Utiliza um microserviço na **GCP**.
- **Converter Fahrenheit para Celsius**: Utiliza um microserviço na **Azure**.

## 🏛️ Arquitetura

A arquitetura é composta por uma interface de frontend e três endpoints de backend independentes.

### Frontend

- Uma página web estática (`index.html`) construída com **HTML5**, **CSS3** e **JavaScript** puro (vanilla).
- A interface é dividida em blocos lógicos para cada tipo de conversão.
- O JavaScript realiza chamadas `fetch` (POST) para as APIs serverless, enviando a temperatura a ser convertida e exibindo o resultado na tela.

### Backend (Microserviços Serverless)

Cada funcionalidade de conversão é implementada como um microserviço independente em uma plataforma de nuvem diferente, demonstrando uma abordagem multicloud e multilíngue.

1.  **AWS: Celsius → Fahrenheit**

    - **Serviço**: AWS Lambda + Amazon API Gateway.
    - **Linguagem**: Python.
    - **Endpoint**: `https://.../converteCelsiusParaFahrenheit`
    - **Lógica**: Recebe um valor em Celsius, calcula `(C * 9/5) + 32` e retorna o resultado em Fahrenheit.

2.  **GCP: Celsius → Kelvin**

    - **Serviço**: Google Cloud Run (ou Cloud Functions).
    - **Linguagem**: PHP.
    - **Endpoint**: `https://.../convertecelsiusparakelvin`
    - **Lógica**: Recebe um valor em Celsius, calcula `C + 273.15` e retorna o resultado em Kelvin.

3.  **Azure: Fahrenheit → Celsius**
    - **Serviço**: Azure Functions.
    - **Linguagem**: PowerShell (Shell Script).
    - **Endpoint**: `https://.../converteFahrenheitParaCelsius`
    - **Lógica**: Recebe um valor em Fahrenheit, calcula `(F - 32) * 5/9` e retorna o resultado em Celsius.

## 🚀 Tecnologias Utilizadas

- **Frontend**:

  - HTML5
  - CSS3
  - JavaScript (ES6+)

- **Cloud & Serverless**:

  - !AWS (Lambda & API Gateway)
  - !Google Cloud (Cloud Run)
  - !Microsoft Azure (Azure Functions)

- **Linguagens (Backend)**:
  - !Python
  - !PHP
  - !PowerShell

## 🔧 Configuração e Uso

Para rodar este projeto, você precisa ter os backends (funções serverless) já implantados em suas respectivas nuvens.

### 1. Configurar os Endpoints da API

Abra o arquivo `index.html` e localize a seção de configuração de URLs no início da tag `<script>`:

```javascript
// --- CONFIGURAÇÃO DAS URLs ---

// 1. Cole a URL da sua API AWS (REST API)
const awsApiUrl = "SUA_URL_AWS_AQUI";

// 2. Cole a URL da sua Azure Function
const azureApiUrl = "SUA_URL_AZURE_AQUI";

// 3. Cole a URL da sua GCP Cloud Run
const gcpApiUrl = "SUA_URL_GCP_AQUI";
```

Substitua `"SUA_URL_..._AQUI"` pelas URLs reais dos seus endpoints implantados.

### 2. Rodar o Frontend

Como o frontend é um arquivo HTML estático, você pode simplesmente abri-lo em um navegador web.

Se você usa o Visual Studio Code com a extensão "Live Server", pode clicar com o botão direito no arquivo `index.html` e selecionar "Open with Live Server". Isso iniciará um servidor local, geralmente em `http://127.0.0.1:5500`.

Após abrir a página, você poderá inserir os valores de temperatura e clicar nos botões para ver a mágica multicloud acontecer!
