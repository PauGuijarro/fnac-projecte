<?php
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class LibroController extends Controller
{
    public function mostrarPrecio($isbn)
    {
        // Llamar al script Python
        $output = null;
        $resultCode = null;

        // Llamada al script Python usando exec
        exec("python3 /ruta/a/tu/proyecto/fnac.py $isbn", $output, $resultCode);

        if ($resultCode === 0) {
            // El script se ejecutó correctamente, pasamos los resultados a la vista
            $resultado = implode("\n", $output);  // Unir el array de salida en un solo string
            return view('precio_libro', ['resultado' => $resultado]);
        } else {
            // En caso de error
            return view('precio_libro', ['error' => 'Hubo un problema al ejecutar el script']);
        }
    }
}
