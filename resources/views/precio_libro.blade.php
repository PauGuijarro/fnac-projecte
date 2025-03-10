<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Precio del Libro</title>
</head>
<body>
    <h1>Resultado de la búsqueda</h1>
    
    @if(isset($resultado))
        <p>Resultado: {!! nl2br(e($resultado)) !!}</p>  <!-- Imprime el resultado con salto de línea -->
    @elseif(isset($error))
        <p>Error: {{ $error }}</p>
    @else
        <p>No se encontraron resultados.</p>
    @endif
</body>
</html>
