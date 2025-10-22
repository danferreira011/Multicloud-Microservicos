import json

def lambda_handler(event, context):
    try:
        # 1. O API Gateway envia os dados dentro do 'body' como uma string.
        # Precisamos "carregar" essa string como um JSON.
        
        # Verificamos se 'body' existe no evento
        if 'body' not in event or event['body'] is None:
            raise ValueError("Corpo da requisição está vazio ou ausente.")
            
        body = json.loads(event['body'])
        
        # 2. Pegamos o valor 'celsius' de dentro do body.
        # Usamos .get() para evitar erros se a chave não existir.
        celsius_str = body.get('celsius')
        
        if celsius_str is None:
            raise ValueError("Chave 'celsius' não encontrada no corpo da requisição.")
            
        celsius = float(celsius_str)
        
        # 3. A fórmula de conversão
        fahrenheit = (celsius * 9/5) + 32
        
        # 4. Preparamos o corpo da resposta
        response_body = {
            "fahrenheit_calculado": fahrenheit,
            "celsius_recebido": celsius
        }
        
        # 5. Retornamos a resposta formatada para o API Gateway
        return {
            "statusCode": 200,
            "headers": {
                # ESSENCIAL: Permite que seu navegador acesse a API
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "GET, POST, OPTIONS"
            },
            "body": json.dumps(response_body)
        }
        
    except Exception as e:
        # Em caso de erro (ex: 'celsius' não é um número)
        return {
            "statusCode": 400,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "GET, POST, OPTIONS"
            },
            "body": json.dumps({"erro": str(e)})
        }