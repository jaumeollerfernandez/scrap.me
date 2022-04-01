<!DOCTYPE html>
<html>
  <head>
  <style>
    table, th, td {
    border: 1px solid;
    border-color:blue;
    }
    table {  
    border-collapse: collapse;
    }
  </style>
    <title>PRECIOS</title>
  </head>
  <body>


<?php 

$productos = array();
$producto = array("nombre"=>"pc","precio"=>"<div id='oferta'>3.423$</div>","poferta"=>"<div id='sin'>None</div>");
array_push($productos, $producto);
$producto = array("nombre"=>"<div id='nombre'>SSD</div>","precio"=>"<span id='product-price' data-price-amount='34' data-price-type='finalPrice' class'price-wrapper '>34&nbsp;€</span>","poferta"=>"23 €");
array_push($productos, $producto);
$producto = array("nombre"=>"disco duro","precio"=>"<div id='precio_sin_oferta' class='precios_' datos='sin_oferta'><span>34_34</span></div>","poferta"=>"<span id='ofertaza'>23_23</span>");
array_push($productos, $producto);
$producto = array("nombre"=>"disco duro","precio"=>"<div id='precio_sin_oferta' class='precios_' datos='sin_oferta'><span>".rand(10,40)."</span></div>","poferta"=>"<span id='ofertaza'>".rand(10,50)."</span>");
array_push($productos, $producto);

echo "<table>";
echo "<th>Nombre producto</th><th>Precio</th><th>Precio Oferta</th>";

foreach ( $productos as $p) {
    echo "<tr><td>".$p['nombre']."</td><td>".$p['precio']."</td><td>". $p['poferta'] . "</td><tr>";
}

echo "</table>";

?>
   
  </body>
</html>

