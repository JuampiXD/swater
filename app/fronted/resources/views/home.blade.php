@extends('layouts\layout')

@section('content')
    @php
        $expedition = json_decode(file_get_contents("http://127.0.0.1:5000"), true);
        echo "<p>&nbsp;&bull;&nbsp; LONGITUD: " . $expedition["length"] . " &nbsp;&bull;&nbsp; LATITUD: " . $expedition["latitude"] .
            " &nbsp;&bull;&nbsp; TAMAÑO: " . $expedition["size"]. "</p><br>";
        if($expedition["potable"] == 1){
            echo "<p>El pozo de agua si es potable </p>";
        }else{
            echo "<p>El pozo de agua no es potable </p>";
        }
    @endphp
@endsection
