<html>
<head>
<title> Extraindo dados de um Banco de dados</title>
<meta http-equiv="refresh"content="30"/>
<hr widht=60% size=3px color=#ff3700>
</head>
<body bgcolor="#e5e5e6">

<a id="arcelorLogoTopo"> 
   <img src="arcelormittal.gif" alt="ArcelorMittal" title="ArcelorMittal"/>
</a>
<b> Monitoramento | 
<a id="arcelorLogoTopo"> 
   <img src="arcelormittal-brasil.png" alt="ArcelorMittal-Brasil" title="ArcelorMittal-Brasil"/>
</a> </b>
<button type="button" onClick="window.location.reload();">Atualizar Valores</button>
<table border=1 align=left width=1 height=800>
<tr><tdbgcolor=green></td></tr>
</table>
<hr widht=60% size=13px color=#878787>

<?php
//Conexão com o banco de dados
$link = mysql_connect("localhost","root","password");

//Seleciona o Banco de Dados
$conexao = mysql_select_db("dados"); if($conexao){

//query SQL

$strSQL0 = "SELECT tdate,ttime,info,value,ad 
           FROM dados2 
           WHERE ad='[AD0]'
           ORDER BY tdate DESC,ttime DESC LIMIT 1";

$strSQL1 = "SELECT tdate,ttime,info,value,ad 
           FROM dados2 
           WHERE ad='[AD1]'
           ORDER BY tdate DESC,ttime DESC LIMIT 1";

$strSQL3 = "SELECT tdate,ttime,info,value,ad 
           FROM dados2 
           WHERE ad='[AD3]'
           ORDER BY tdate DESC,ttime DESC LIMIT 1";

$strSQL4 = "SELECT tdate,ttime,info,value,ad
           FROM dados2 
           WHERE ad='[AD4]'
           ORDER BY tdate DESC,ttime DESC LIMIT 1";

$strSQL5 = "SELECT tdate,ttime,info,value,ad 
           FROM dados2 
           WHERE ad='[AD5]'
           ORDER BY tdate DESC,ttime DESC LIMIT 1";


//Executa a query(o recordset $rs contém o resultado da query)
$rs0 = mysql_query($strSQL0);
$rs1 = mysql_query($strSQL1);
$rs3 = mysql_query($strSQL3);
$rs4 = mysql_query($strSQL4);
$rs5 = mysql_query($strSQL5);



echo '<table widths="30;60" cellpading="1.5" border="1">';
echo '<tr>';
echo '<td>Data</td>';
echo '<td>Hora</td>';
echo '<td>Informação</td>';
echo '<td>Valor</td>';
echo '<td>AD []</td>';


//Temperatura 0
while ($row0 = mysql_fetch_assoc($rs0)){

// Escreve o valor da coluna Firstname(que está no array $row)
      
   echo '<tr>';
   echo '<td>'.$row0["tdate"].'</td>';
   echo '<td>'.$row0["ttime"].'</td>';   
   echo '<td>'.$row0["info"].'</td>';
   //echo '<td>'.$row0["value"].'</td>';

   if($row0["value"] < 18 || $row0["value"] > 27  ){
   echo'<td style="background:red ; color:black;">'.$row0["value"].'</td>';
   }else{
   echo'<td style="background: #e5e5e6 ; color:black;">'.$row0["value"].'</td>';
   } 

   echo '<td>'.$row0["ad"].'</td>';
   echo '</tr>';

      
}

//Temperatura 1
while ($row1 = mysql_fetch_assoc($rs1)){

 //Escreve o valor da coluna Firstname(que está no array $row1)
      
   echo '<tr>';
   echo '<td>'.$row1["tdate"].'</td>';
   echo '<td>'.$row1["ttime"].'</td>';   
   echo '<td>'.$row1["info"].'</td>';
   //echo '<td>'.$row1["value"].'</td>';

   if($row1["value"] < 18 || $row1["value"] > 27  ){
   echo'<td style="background:red ; color:black;">'.$row1["value"].'</td>';
   }else{
   echo'<td style="background: #e5e5e6 ; color:black;">'.$row1["value"].'</td>';
   }

   echo '<td>'.$row1["ad"].'</td>';
   echo '</tr>';

      
}

//Sensor de água
while ($row3 = mysql_fetch_assoc($rs3)){
echo '<tr>';
   echo '<td>'.$row3["tdate"].'</td>';
   echo '<td>'.$row3["ttime"].'</td>';   
   echo '<td>'.$row3["info"].'</td>';
   //echo '<td>'.$row3["value"].'</td>';

   if($row3["value"] == 1){
   echo'<td style="background:red ; color:black;">'.$row3["value"].'</td>';
   }else{
   echo'<td style="background: #e5e5e6 ; color:black;">'.$row3["value"].'</td>';
   //echo'<td style="background: #e5e5e6 ; color:black;">'Teste'</td>';
   }


   echo '<td>'.$row3["ad"].'</td>';
   echo '</tr>';   

}

//Umidade
while ($row4 = mysql_fetch_assoc($rs4)){
echo '<tr>';
   echo '<td>'.$row4["tdate"].'</td>';
   echo '<td>'.$row4["ttime"].'</td>';   
   echo '<td>'.$row4["info"].'</td>';
   //echo '<td>'.$row4["value"].'</td>';
   
   if($row4["value"] < 35 || $row4["value"] > 60  ){
   echo'<td style="background:red ; color:black;">'.$row4["value"].'</td>';
   }else{
   echo'<td style="background: #e5e5e6 ; color:black;">'.$row4["value"].'</td>';
   }

   echo '<td>'.$row4["ad"].'</td>';
   echo '</tr>';   

}


while ($row5 = mysql_fetch_assoc($rs5)){
echo '<tr>';
   echo '<td>'.$row5["tdate"].'</td>';
   echo '<td>'.$row5["ttime"].'</td>';   
   echo '<td>'.$row5["info"].'</td>';
   echo '<td>'.$row5["value"].'</td>';
   echo '<td>'.$row5["ad"].'</td>';
   echo '</tr>';   

   echo'</table>';

}

}

//Encerra a conexão
mysql_close();

?> 

<a href="index2.html"> Vá para o Gráfico de Temperatura 0</a>
<p>
<a href="index4.html"> Vá para o Gráfico de Temperatura 1</a>
<p>
<a href="index3.html"> Vá para o Gráfico de Humidade </a>


<hr widht=60% size=13px color=#878787>

</body>

</html>

