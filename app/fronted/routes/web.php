<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::view('/', 'home')->name('home');
Route::view('inspected', 'inspected')->name('inspected');
Route::view('show_expeditions', 'show_expeditions')->name('show_expeditions');
Route::view('fix_expedition', 'fix_expedition')->name('fix_expedition');

