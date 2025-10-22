param($Request, $TriggerMetadata)

# 1. O Azure já "converteu" o JSON para nós porque viu o "Content-Type".
# O $Request.Body JÁ É um objeto PowerShell.
$data = $Request.Body

# 2. Pega o valor 'fahrenheit' diretamente do objeto
$fahrenheit_str = $data.fahrenheit
if (-not $fahrenheit_str) {
    # Se a chave 'fahrenheit' não for encontrada...
    Push-OutputBinding -Name Response -Value ([HttpResponseContext]@{
        StatusCode = 400
        Body = "Chave 'fahrenheit' não encontrada no corpo da requisição."
    })
    return
}

# 3. A fórmula de conversão
try {
    $fahrenheit = [float]$fahrenheit_str
    $celsius = ($fahrenheit - 32) * 5/9
}
catch {
    # Se 'fahrenheit' não for um número (ex: "abc")
    Push-OutputBinding -Name Response -Value ([HttpResponseContext]@{
        StatusCode = 400
        Body = "Valor 'fahrenheit' não é um número válido."
    })
    return
}


# 4. Prepara o corpo da resposta
$responseBody = @{
    celsius_calculado = $celsius
    fahrenheit_recebido = $fahrenheit
} | ConvertTo-Json

# 5. Retorna a resposta de sucesso (200)
Push-OutputBinding -Name Response -Value ([HttpResponseContext]@{
    StatusCode = 200
    Body = $responseBody
    Headers = @{
        'Content-Type' = 'application/json'
    }
})