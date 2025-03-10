<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\LibroController;

Route::get('/buscar-precio/{isbn}', [LibroController::class, 'mostrarPrecio']);


Route::get('/', function () {
    return view('welcome');
});
