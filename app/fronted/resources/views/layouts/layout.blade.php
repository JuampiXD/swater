<!DOCTYPE HTML>
<html>
<head>
    <title>Swater</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
    <link rel="stylesheet" href="css/main.css" />
    <noscript>
        <link rel="stylesheet" href="css/noscript.css" />
    </noscript>
</head>
<div Style="position: absolute; width: 100%; z-index: 100">
    <ul class="menu">
        <li><a href="{{route('home')}}">Home</a></li>
        <li><a href="{{route('inspected')}}">Inspected</a></li>
        <li><a href="{{route('show_expeditions')}}">Show Expeditions</a></li>
        <li><a href="{{route('fix_expedition')}}">Fix Expedition</a></li>
    </ul>
</div>
<body class="is-preload">
<div id="wrapper">
    <div id="bg"></div>
    <div id="overlay"></div>
    <div id="main">

        <!-- Header -->
        <header id="header">
            <div class="parent">
                <img class="image1" style="z-index: 1; width: 500px; filter: drop-shadow(0 2px 50px rgba(0, 0, 0, 0.7)" src="{{asset('images/Mars.png')}}" />
                <img class="image2" style="z-index: 1; width: 400px" src="{{asset('images/logo.png')}}" />
            </div>
           @yield('content')
        </header>

        <!-- Footer -->
        <footer id="footer"> <span class="copyright">&copy; Tubaina Funada <a href="https://youtu.be/dQw4w9WgXcQ">FREE DOGE COINS!</a>.</span> </footer>
    </div>
</div>
<script>
    window.onload = function() { document.body.classList.remove('is-preload'); }
    window.ontouchmove = function() { return false; }
    window.onorientationchange = function() { document.body.scrollTop = 0; }
</script>
</body>
</html>
