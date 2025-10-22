<?php

// --- MANIPULAÇÃO DE CORS ---
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type");

// 1. Responde ao "preflight" (requisição OPTIONS)
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204); // No Content
    exit;
}
// ----------------------------

// 2. Garante que só aceitamos POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405); // Method Not Allowed
    echo json_encode(['erro' => 'Método não permitido. Use POST.']);
    exit;
}

// 3. Pega o corpo JSON da requisição
$json_data = file_get_contents('php://input');
$data = json_decode($json_data, true); // O 'true' converte para array associativo

if ($data === null || !isset($data['celsius'])) {
    http_response_code(400); // Bad Request
    echo json_encode(['erro' => "Chave 'celsius' não encontrada ou JSON inválido no corpo da requisição."]);
    exit;
}

$celsius_str = $data['celsius'];

// 4. Valida e converte para float
if (!is_numeric($celsius_str)) {
    http_response_code(400); // Bad Request
    echo json_encode(['erro' => "Valor 'celsius' não é um número válido."]);
    exit;
}

$celsius = (float)$celsius_str;

// 5. A fórmula de conversão
$kelvin = $celsius + 273.15;

// 6. Prepara a resposta de sucesso
$responseBody = [
    'kelvin_calculado' => $kelvin,
    'celsius_recebido' => $celsius,
];

// 7. Retorna a resposta
http_response_code(200); // OK
header('Content-Type: application/json');
echo json_encode($responseBody);

?>